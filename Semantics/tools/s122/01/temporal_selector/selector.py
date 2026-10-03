"""Population-conditioned selector, specification v1.2. Python 3 standard library."""
import copy
import math

UNITS = ('trace', 'adaptation', 'latch', 'rebound', 'coincidence', 'sequence', 'expectation')

class Selector:
    def __init__(self, k, eligible=None, disabled=()):
        self.k = k
        self.eligible = list(eligible if eligible is not None else (i for i in range(k) if i % 7 != 6))
        if not self.eligible or len(set(self.eligible)) != len(self.eligible):
            raise ValueError('eligible indices must be nonempty and unique')
        if any(i < 0 or i >= k for i in self.eligible):
            raise ValueError('eligible index outside catalog')
        self.disabled = set(disabled)
        if not self.disabled <= set(UNITS):
            raise ValueError('unknown ablation')
        self.state = dict(h=[0.0]*k, hprev=[0.0]*k, q=[0.0]*k,
                          latch=[0]*k, clear=[0]*k, rebound=[0.0]*k,
                          event=[0.0]*k, coincidence=[[0.0]*k for _ in range(k)])

    def load(self, state):
        if set(state) != set(self.state):
            raise ValueError('state schema differs')
        if any(len(v) != self.k for v in state.values()):
            raise ValueError('state catalog size differs')
        self.state = copy.deepcopy(state)
        return self

    def initial_pay(self):
        return [18.0/len(self.eligible) if i in self.eligible else 0.0 for i in range(self.k)]

    def step(self, obs):
        k = self.k
        if len(obs['p']) != k or len(obs['q']) != k or len(obs['cooc']) != k:
            raise ValueError('observation catalog size differs')
        vals = list(obs['p']) + list(obs['q'])
        for row in obs['cooc']:
            if len(row) != k:
                raise ValueError('coincidence shape differs')
            vals.extend(row)
        if any(not math.isfinite(v) or v < 0 or v > 1 for v in vals):
            raise ValueError('shares must be finite in [0,1]')
        if any(obs['q'][j] > obs['p'][j] + 1e-12 for j in range(k)):
            raise ValueError('all-order share exceeds world-order share')
        for j in range(k):
            for i in range(k):
                if obs['cooc'][j][i] > min(obs['q'][j], obs['q'][i]) + 1e-12:
                    raise ValueError('coincidence exceeds marginal')
                if abs(obs['cooc'][j][i]-obs['cooc'][i][j]) > 1e-12:
                    raise ValueError('coincidence matrix is not symmetric')
        allowed = set(self.eligible)
        p = [obs['p'][i] if i in allowed else 0.0 for i in range(k)]
        q = [obs['q'][i] if i in allowed else 0.0 for i in range(k)]
        old = self.state
        h = [math.exp(-.25)*old['h'][i] + (1-math.exp(-.25))*q[i] for i in range(k)]
        if 'trace' in self.disabled:
            h = q[:]
        prediction = [min(1., max(0., 2*old['h'][i]-old['hprev'][i])) for i in range(k)]
        surprise = [abs(q[i]-prediction[i]) if 'expectation' not in self.disabled else 0.0 for i in range(k)]
        latch, clear, release = [], [], []
        for i in range(k):
            L = old['latch'][i]
            streak = old['clear'][i]+1 if q[i] >= .1 else 0
            if 'latch' in self.disabled:
                L, streak, released = 0, 0, 0
            else:
                if L:
                    if streak >= 2:
                        L = 0
                elif (p[i] >= .1 or old['q'][i] >= .1 or old['h'][i] >= .1) and q[i] < .02:
                    L, streak = 1, 0
                released = int(old['latch'][i] == 1 and L == 0)
            latch.append(L)
            clear.append(min(2, streak))
            release.append(released)
        rebound = [math.exp(-.5)*old['rebound'][i]+release[i] if 'rebound' not in self.disabled else 0.0 for i in range(k)]
        C = [[(math.exp(-.5)*old['coincidence'][i][j]+(1-math.exp(-.5))*obs['cooc'][i][j])
              if i != j and i in allowed and j in allowed and 'coincidence' not in self.disabled else 0.0
              for j in range(k)] for i in range(k)]
        coinc = [max(row) for row in C]
        events = [int(old['q'][i] < .1 <= q[i]) for i in range(k)]
        decayed = [math.exp(-1/3)*v for v in old['event']]
        seq = [events[i]*max((decayed[j] for j in self.eligible if j != i), default=0.0)
               if 'sequence' not in self.disabled else 0.0 for i in range(k)]
        event_trace = [1.0 if events[i] else decayed[i] for i in range(k)]
        if 'sequence' in self.disabled:
            event_trace = [0.0]*k
        adapt = [.1 + 1/(1+8*x) if 'adaptation' not in self.disabled else 1.1 for x in h]
        raw = [adapt[i]+latch[i]+.5*(rebound[i]+coinc[i]+seq[i]+surprise[i]) for i in range(k)]
        denom = sum(raw[i] for i in self.eligible)
        pay = [18*raw[i]/denom if i in allowed else 0.0 for i in range(k)]
        self.state = dict(h=h, hprev=old['h'][:], q=q, latch=latch, clear=clear,
                          rebound=rebound, coincidence=C, event=event_trace)
        return dict(pay=pay, diagnostics=dict(adaptation=adapt, prediction=prediction,
                    surprise=surprise, latch=latch, release=release, rebound=rebound,
                    coincidence=coinc, sequence=seq, events=events, raw=raw))
