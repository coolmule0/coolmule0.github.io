Title: About
Date: 2021-08-18 10:20

I'm John Charlton, a PhD student/Research Asssociate at the [University of Sheffield](https://www.sheffield.ac.uk), in the [Department of Computer Science](https://www.sheffield.ac.uk/dcs), in the [Visual Computing Group](https://www.sheffield.ac.uk/dcs/research/groups/visual-computing/home).

Supervisors are [Paul Richmond](http://paulrichmond.shef.ac.uk/) and [Steve Maddock](http://staffwww.dcs.shef.ac.uk/people/S.Maddock/index.shtml)

<p>My focus is on fast and realistic simulations of dense pedestrian crowds. My research examines models and algorithms suitable for increasing accuracy and realism of crowds, while being ran in real-time. The advantage of real-time simulations is immediate visualisation and interactivity. User-input can affect the model and add imersion to enhance realism. </p>

<p>Graphical proccessing units (GPUs) are exelent hardware for use with pedestrian simulations. The effective compute throughput is theortically far higher in GPUs than CPUs. Since pedestrians follow similar rules and behaviours, there is a high degree of parallelism within models. This lends itself well to GPUs. The GPU is also used for visualisations. By having data computed on the GPU, results can be visualised with only minimal extra overhead.  </p>

<a href="imgs/presenting_large.jpg"><img src="imgs/presenting.jpg" class="textImage"></a>

<p>Being subject to real-time simulations, there must be a trade off between model complexity and number of simulated people. By increasing one, the other must decrease for simulation steps to remain constant. Use of GPUs allows for an increase in both model complexity and number of simulated people due to its high compute throughput.</p>

<p>I have examined the use of the ORCA model on GPUs, originally created by <a href="http://gamma.cs.unc.edu/ORCA/">van den Berg et. al</a>. It allows for millions of people to be simulated and visualised in real-time. </p>

<p>Current work is examining ways to increase realism and accuracy of dense crowds.</p>
