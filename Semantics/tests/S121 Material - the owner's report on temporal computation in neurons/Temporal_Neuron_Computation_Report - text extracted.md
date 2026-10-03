Temporal computation in biological and artificial neurons

A report on neuronal processing, timing dependent capabilities, efficient models and tested implementations

Prepared for Aza • 2 October 2026

# Scope and main findings

This report brings together the full substance of the supplied discussion: whether a neuron resembles a logic gate or a network, what temporal dependencies contribute, how those dependencies can be modelled efficiently, and which timing sensitive behaviours have been simulated or built. It retains the illustrative examples, equations, experimental qualifications and research links. It is a synthesis of the conversation rather than a new systematic literature review; the cited studies and implementation claims have not been independently rechecked for this report.

A biological neuron can contain interacting local processors whose evolving states make its response depend on previous inputs. Timing therefore supports memory, sequence recognition, coincidence and interval detection, rhythm sensitivity and adaptation. These capabilities can also be implemented with digital logic, provided that the circuit includes the relevant memory and state updates. Their potential advantage lies in representation and implementation efficiency, which must be measured for a particular task.

There is no fixed count of timing sensitive neuron types. Anatomical cell types, electrical response behaviours, mathematical model families and learning rules are different classifications. The classic Izhikevich comparison demonstrates 20 response behaviours using a compact model with different parameter settings; it does not identify 20 biological cell types or exhaust all temporal computations. [1]

# A neuron as a collection of processors

The simplest artificial neuron adds weighted inputs and applies a threshold or activation function. That resembles the simplified biological picture of incoming signals being summed until firing occurs. For many biological neurons, particularly highly branched pyramidal cells, this leaves out consequential internal structure.

Dendrites receive signals and process them locally. Nearby inputs on a branch can interact nonlinearly, so their combined effect need not equal the sum of their separate effects. Different branches can act as partly independent processing subunits before their contributions converge into the cell’s output. A classic modelling study approximated pyramidal neuron firing rates with a two layer neural network in which dendritic subunits supplied the first layer. This is a computational analogy, not a claim that a cell contains other neurons. [2]

A toy Boolean illustration is:

(A AND B) OR (C AND D)

One branch could detect A together with B, while another detects C together with D; the cell could combine the local results. This illustrates several operations inside one neuron. Actual dendritic signals are graded, dependent on timing and affected by electrical coupling rather than clean Boolean values. The branches are interacting parts of one cell, so multiple internal computations need not yield multiple separately accessible answers. [2, 3]

A 2021 study trained artificial networks to reproduce the millisecond input–output behaviour of a detailed simulated cortical neuron. Within the approach tested, this required networks with five to eight layers. This establishes the complexity that a single artificial unit can omit, but it does not establish a universal conversion between a biological neuron and a fixed number of AI layers. The result depends on the neuron model, network architecture and desired accuracy. [4]

# What timing contributes to computation

A memoryless system computes an output from its present input:

y = f(x)

A stateful system also updates an internal representation of its history:

sₜ₊₁ = F(sₜ, xₜ, Δt)       yₜ = G(sₜ, xₜ)

Here s is the internal state, x the input and Δt the elapsed time. Consider B arriving after A, compared with B arriving without a preceding A. At B’s arrival, the present external input can be identical. A memoryless function must respond identically; a stateful system can respond differently because A changed its state. Sequential digital circuits provide the corresponding distinction from combinational circuits. [5]

Some temporal state exists within a single biological cell. Membrane voltage, adaptation and dendritic dynamics can carry effects of earlier inputs, so recurrence among multiple neurons is not required for every form of temporal memory. Experiments on cortical pyramidal neurons have demonstrated sensitivity to the order and speed of synaptic activation along a dendrite. [6, 7]

## Order and sequence recognition

A system can respond to A followed by B while rejecting B followed by A. Changing the order of otherwise similar dendritic inputs can change the neuronal response. This can support direction sensitivity for a moving pattern, because the ordered activation of positions matters rather than merely the presence of those inputs. [6, 7]

## Intervals and coincidence

Short lived internal responses create narrow windows within which inputs can reinforce one another. Longer lived responses permit accumulation over broader windows. A detector can consequently distinguish closely spaced inputs from the same inputs spread over time. Adding delays to input pathways can convert a preferred interval into a coincidence at the receiving unit.

## Recent activity and context

The same stimulus can produce a different response after recent activity. Adaptation, for example, can progressively reduce firing during sustained stimulation. The response depends on the current signal and the neuron’s recent activity. These capabilities need not be independent processors; several can emerge from interacting state variables in one dynamical system. [8]

# Comparison with standard logic gates

Timing does not confer a class of computation fundamentally inaccessible to ordinary digital logic. The fair comparison is with a circuit containing memory and feedback, rather than a memoryless arrangement of AND and OR gates. Gates can be combined to construct the memory required for temporal computation. [5]

A digital sequence detector might record that A occurred, store a timestamp and compare it when B arrives. A neuron inspired detector might leave a decaying trace of A that changes B’s effect. Both implement the temporal rule, while representing the relevant history differently. A feedforward circuit could also process an entire recorded sequence supplied as its input.

For a neuron model restricted to finite precision, internal state can be encoded in bits and its update rules implemented digitally in principle. The practical limitation is whether the necessary history survives in the input or stored state. Two histories collapsed to the same internal state cannot subsequently be distinguished by a deterministic model receiving the same future inputs.

Potential advantages include compact state, a natural fit to streaming events and implementation dependent energy or latency savings. None follows merely from a neuron being richer than one gate. A biological neuron is not equivalent to a single transistor or elementary gate, and comparisons must include the complete hardware or software implementation.

# An efficient temporal order detector

A small illustrative model can recognise A followed shortly by B without simulating biological detail. Maintain a trace r_A, initially zero. On A, set the trace to one. Between events, let it decay exponentially:

r_A(t + Δt) = r_A(t) exp(−Δt / τ)

When B arrives, output a response if r_A exceeds a threshold θ. A followed shortly by B succeeds. B before A fails, assuming no earlier A remains in memory. A followed much later by B also fails because the trace has faded.

With τ = 50 milliseconds, the trace is approximately 0.82 after 10 milliseconds and 0.14 after 100 milliseconds. A threshold of 0.5 separates those cases. A single state variable supplies short term memory and a graded representation of recency.

Because A resets the trace to one, the threshold is equivalent to a timer condition measured from the most recent A:

r_A > θ  ⇔  elapsed time < −τ ln(θ),       0 < θ < 1

For τ = 50 milliseconds and θ = 0.5, this window is approximately 34.7 milliseconds. This equivalence makes clear that the mechanism is a dynamical representation of a timing rule, rather than an operation unavailable to digital logic.

Brian 2 supports exact event driven updates for suitable independent, one dimensional linear differential equations. Exponential traces can therefore be updated when an event needs them rather than at every small simulation timestep. This does not make arbitrary nonlinear or coupled models exactly event driven. [9]

# Efficient models for richer behaviour

A small state space model can use several traces with different timescales and nonlinear interactions. Input identity must remain represented: collapsing every signal into a single undifferentiated sum can destroy the distinctions needed for sequence recognition. Partial sequence states can implement a progression in which A enables B, and B enables C.

For K independent traces, updating every trace requires O(K) arithmetic work and O(K) stored state per event, excluding input processing and output calculation. Dense interactions can increase the work. Lazy updates can reduce unnecessary operations where only a subset of traces is accessed and the intervening dynamics are analytically tractable. Constant sized state compresses history; it is not an unlimited record.

For biological firing behaviour, adaptive exponential integrate and fire, or AdEx, uses membrane voltage and adaptation as two dynamical variables together with a spike and reset rule. It can reproduce several firing patterns without representing every ion channel. A basic point neuron does not capture separate dendritic branches; branch specific computation requires additional compartments or suitable surrogate states. [8]

Izhikevich models provide another compact family for exploring many response behaviours. Parameter changes can produce qualitatively different firing regimes, so a library need not use a separate implementation for every named behaviour. [1]

For general sequence processing, recurrent networks and state space models also update a compact state as inputs arrive. Mamba uses input dependent state space updates to control information persistence. This is a computational connection, not evidence that Mamba reproduces dendritic physiology. [10]

Event driven simulation can save work when activity is sparse and the dynamics between events are simple. Scheduling overhead, dense activity and complicated dynamics can remove that advantage. The numerical update method also matters: an appropriate differential equation can still produce an unstable or inaccurate implementation. [11, 12]

# Timing sensitive behaviours and their functions

## Leaky integration

A leaky integrator asks whether enough input has accumulated recently. It sums signals while older contributions fade, so closely spaced inputs can trigger firing when isolated inputs cannot. The simplest leaky integrate and fire model, LIF, has one membrane voltage variable and a spike/reset rule. Synaptic dynamics can add state. LIF is implemented in software and neuromorphic hardware and is widely used as a baseline. [12]

## Coincidence detection

A coincidence detector favours inputs arriving within a narrow window. Different pathway delays let it recognise a particular arrival difference instead. The detector and its delays jointly implement the computation. A SpiNNaker sound localisation implementation distinguished synthetic spike patterns representing inter ear timing differences of −30, 0 and +30 microseconds. This was a hardware model tested with generated inputs, not a complete biological auditory system. [13]

## Resonance

A resonator favours certain input intervals or rhythms. Its internal state oscillates, so closer spacing does not invariably produce a stronger response. Resonate and fire models capture this timing or frequency preference. The discussion cited a May 2026 photonic electronic device whose responses depended on the interval between optical pulses, with bandpass filtering and temporal pattern recognition demonstrations. This is evidence of a functioning timing sensitive prototype, not of a general AI advantage. [14]

## Adaptation

An adaptive neuron changes its sensitivity following recent activity, for example through an increased threshold or adaptation current. This can emphasise stimulus onset and provide longer lasting state. Model families include adaptive LIF, AdEx and double exponential adaptive threshold models, DEXAT. DEXAT was tested on sequential digit and speech recognition. A spoken up versus down demonstration combined physical adaptive threshold circuits with other neuron operations in software; it was hybrid rather than a fully physical network. [15]

## Post inhibitory rebound

A rebound neuron fires after inhibition is removed. Suppression changes its internal state, and release becomes an effective trigger. This can serve as an offset or release detector. An engineered sequence processor could use the end of suppression to trigger its next stage; that is a possible computational use rather than a universal biological function. AdEx simulations reproduce rebound behaviour, including sensitivity to abrupt versus gradual release. [8]

## Bursting

A bursting neuron emits a cluster of spikes, sometimes at onset and sometimes repeatedly. Receivers can distinguish an isolated spike, an initial burst and ongoing bursts. BrainScaleS 2 implements AdEx dynamics in silicon and provides configurations for initial and regular bursting using the same underlying neuron circuit with different parameters. [16]

## Latency encoding

A latency sensitive neuron represents information through the delay to its first spike. Stronger input may produce an earlier spike, allowing a response without waiting for a long spike count. Experimental resonant tunnelling diode circuits showed input dependent latency and firing rate encoding. The separate multilevel signal reconstruction example in that work was numerical and should not be described as a measured hardware application. [17]

## Bistability

A bistable neuron supports persistent regimes, such as quiet versus repetitive firing. An input can change the regime and the state can remain after that input ends, resembling a latch rather than a decaying trace. A 2024 Physical Review Letters study demonstrated a spiking flip flop in a resonant tunnelling diode neuron; appropriately timed set and reset pulses switched it between spiking and quiet regimes. [18]

## Dendritic sequence detection

A dendritic sequence detector retains where inputs arrive as well as when. Local electrical interactions can make the same input set yield different outputs in different orders. Sequence sensitivity has been observed experimentally in cortical pyramidal dendrites. A separate detailed Purkinje cell simulation demonstrated direction sensitive sequence discrimination and, under restricted conditions, learning that changed the preferred direction. That learning result was simulated, not established in a living animal. [7, 19]

These models typically need more structure than a point neuron because input location participates in the computation. The Purkinje model explicitly represented dendritic compartments and channel dynamics. [19]

# Learning temporal computations

## The tempotron

The tempotron learns to fire for some spatiotemporal input patterns and remain silent for others. It can classify information carried by spike timing rather than only average firing rates. The original work implemented and tested learning computationally. Its principal output is a binary decision within a window, rather than an arbitrarily prescribed sequence of precisely timed output spikes. It is a learning model, not an anatomical neuron type. [20]

## The chronotron

The chronotron learns to produce a target output spike pattern when a given input pattern arrives. Original computer experiments reported sub millisecond timing precision and classification through shared output patterns for inputs in the same class. These results demonstrate a temporal input to output transformation in simulation, not that the brain uses the exact training rule. [21]

The distinction is useful: a tempotron primarily recognises a timed pattern, while a chronotron can respond with a new pattern whose timing is controlled. Both are learning approaches rather than additional biological cell categories.

# Delays as a computational component

Some apparent neuronal temporal capabilities depend on connections as well as the neuron. Delayed copies of inputs can transform a sequence problem into a coincidence problem. Delays, weights, membrane dynamics and readout together determine the overall computation.

DenRAM built circuits combining delays and synaptic weights and evaluated temporal tasks with hardware informed simulations. Its speech benchmark used longer simulated delays than the demonstrated circuit supplied. Consequently, construction of the components must be distinguished from execution of the full benchmark on physical hardware. [22]

# Choosing a model and testing its contribution

Start by specifying which histories must produce different outputs. For an exact known sequence rule, a small state machine with timers may be simplest. For graded intervals and interacting short term memories, a compact dynamical state space model is a suitable starting point. For a broad range of firing behaviours, AdEx or Izhikevich models avoid duplicating implementations. Add dendritic compartments when input location and branch interactions are necessary.

A practical first experiment is an adaptive neuron with configurable timescales and optional input delays. Compare it with simpler alternatives on a task requiring timing. Hold input identities and counts fixed while changing their order, spacing or rhythm. This prevents a temporal model from succeeding through input counts alone.

The contribution of each component can then be examined by removing adaptation, removing delays or replacing detailed branch dynamics with a simpler state representation. Compare task performance at a stated timing accuracy alongside memory, runtime, energy where measurable and implementation complexity. Working prototypes establish feasibility; a claimed efficiency advantage requires a matched comparison.

The central computational principle is that an input changes how the system responds to subsequent inputs. Biological neurons embody this in evolving physical state. Digital circuits and compact software models can reproduce the principle by explicitly implementing the relevant states and update rules.

# Research sources from the discussion

The links below preserve the research trail supplied in the conversation. They are not a fresh verification record. The earlier discussion attached a dendritic sequence paper to one AdEx description; this report instead associates that description with the AdEx source already provided elsewhere in the discussion.

[1] Izhikevich comparison of neuron response behaviourshttps://www.izhikevich.org/publications/whichmod.pdf

[2] Pyramidal neuron as a two layer neural networkhttps://pubmed.ncbi.nlm.nih.gov/12670427/

[3] Dendritic computation reviewhttps://pubmed.ncbi.nlm.nih.gov/15156147/

[4] Deep artificial networks modelling a simulated cortical neuronhttps://pubmed.ncbi.nlm.nih.gov/34380016/

[5] Computation Structures on sequential logichttps://computationstructures.org/notes/sequential_logic/notes.html

[6] Dendritic sensitivity to temporal input sequenceshttps://pubmed.ncbi.nlm.nih.gov/16014787/

[7] Experimental dendritic sequence processinghttps://pmc.ncbi.nlm.nih.gov/articles/PMC6354899/

[8] Adaptive exponential integrate and fire dynamicshttps://pmc.ncbi.nlm.nih.gov/articles/PMC2798047/

[9] Brian 2 synapses and event driven equationshttps://brian2.readthedocs.io/en/2.10.0/user/synapses.html

[10] Mamba selective state space modelshttps://arxiv.org/abs/2312.00752

[11] Brian 2 simulation methods and event driven restrictionshttps://brian2.readthedocs.io/en/stable/advanced/how_brian_works.html

[12] Adaptive neuron modelling and numerical updateshttps://www.nature.com/articles/s41467-025-60878-z

[13] SpiNNaker coincidence detection and sound localisationhttps://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2015.00206/full

[14] Photonic electronic timing sensitive neuronhttps://www.nature.com/articles/s42005-026-02694-5

[15] DEXAT adaptive threshold neuronshttps://www.nature.com/articles/s41467-021-24427-8

[16] BrainScaleS 2 AdEx dynamics demonstrationshttps://electronicvisions.github.io/documentation-brainscales2/latest/brainscales2-demos/fp_adex_complex_dynamics.html

[17] Resonant tunnelling diode latency and rate encodinghttps://arxiv.org/html/2503.21342

[18] Physical spiking flip flophttps://link.aps.org/doi/10.1103/PhysRevLett.133.267301

[19] Purkinje cell sequence discrimination modellinghttps://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2023.1075005/full

[20] The tempotronhttps://www.nature.com/articles/nn1643

[21] The chronotronhttps://pmc.ncbi.nlm.nih.gov/articles/PMC3412872/

[22] DenRAM circuits and temporal benchmarkshttps://www.nature.com/articles/s41467-024-47764-w