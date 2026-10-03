from math import sqrt
from statistics import NormalDist, variance
import scipy
from scipy.stats import nct, t
zsum2 = (NormalDist().inv_cdf(.9875) + NormalDist().inv_cdf(.8)) ** 2
print('sample_variances=%.6f,%.6f' % (variance([48,55,65]), variance([13,32,41])))
print('z_sum_squared=%.6f' % zsum2)
for difference_variance in [2*variance([13,32,41]), 4*variance([13,32,41])]:
    for n in range(2, 1000):
        critical = t.ppf(.9875, n-1)
        shift = 10*sqrt(n/difference_variance)
        power = nct.sf(critical,n-1,shift)+nct.cdf(-critical,n-1,shift)
        if power >= .8:
            print('n=%d; difference=10; difference_variance=%.6f; model_power=%.6f; total_runs=%d; cpu_hours_100k=%d; phased_wall_hours_100k=%d' %
                  (n,difference_variance,power,8*n,16*n,2*((2*n+2)//3+(6*n+2)//3)))
            break
print('Python SciPy version:',scipy.__version__)
