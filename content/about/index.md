---
title: "About"
date: 2022-07-14T11:34:58+01:00
---

<!-- ![headshot](mugshot.jpg) -->

I'm John Charlton, a Postdoctoral Research Fellow at the [University of Sheffield](https://www.sheffield.ac.uk), in [Neopath](https://www.neopath.org.uk/), part of the [School of Clinical Dentitry](https://www.sheffield.ac.uk/dentalschool)

My work is in the field of Computational Pathology, which seeks to utilise modern hardware advancements, developments in algorithms, and connect between different disciplines, to forward healthcare. I am specifically examining detections of head and neck cancers, with the aim of improving the detection and prognosis.

## PhD

I completed my PhD, as well as carried out 3 years of Research Associate work in the [Department of Computer Science](https://www.sheffield.ac.uk/dcs), in the [Visual Computing Group](https://www.sheffield.ac.uk/dcs/research/groups/visual-computing/home). Where my focus was of GPU computing, and simulating pedestrian crowds.

My PhD supervisors were [Paul Richmond](http://paulrichmond.shef.ac.uk/) and [Steve Maddock](http://staffwww.dcs.shef.ac.uk/people/S.Maddock/index.shtml), and I worked closely with [David Fletcher](https://www.sheffield.ac.uk/mecheng/people/academic/david-fletcher) in [Mechanical Engineering](https://www.sheffield.ac.uk/mecheng)

My focus is on fast and realistic simulations of dense pedestrian crowds. My research examines models and algorithms suitable for increasing accuracy and realism of crowds, while running in real-time. This is applied to practical areas such as train stations and platforms to help understand crowd dynamics and effects.

Graphical proccessing units (GPUs) are exelent hardware for use with pedestrian simulations. The effective compute throughput is theortically far higher in GPUs than CPUs. Since pedestrians follow similar rules and behaviours, there is a high degree of parallelism within models. The GPU is also used for visualisations, providing both computation and visualisation with only a fraction of additional overhead. 

![Me presenting at a conference](presenting.jpg)

Being subject to real-time simulations, there must be a trade off between model complexity and number of simulated people. By increasing one, the other must decrease for simulation steps to remain constant. Use of GPUs allows for an increase in both model complexity and number of simulated people due to its high compute throughput.

I have examined the use of the ORCA model on GPUs, originally created by [van den Berg et. al](http://gamma.cs.unc.edu/ORCA/). It allows for millions of people to be simulated and visualised in real-time. It is an exellent baseline steering model in which to build more complex designs.

<!-- My current work is examining ways to increase realism and accuracy of dense crowds. As well as working on my PhD thesis, I have been applying the models developed with the department of Mechanical Engineering to ask and answer questions around the platform-train interface, through RateSetter. -->

## RateSetter

As a research associate I am examining the Platform-Train Interface (PTI) within train stations. This has been particularly interesting during COVID times as social distancing  greatly changes the boarding and alighting behaviour of people. 

My work has involved creating a computer model of the PTI boarding-alighting process, validating it against CCTV from train stations, and then using the model to make predictions on how different parameters (e.g. platform layout, stock type) will affect this PTI process.

It has been really interesting to bring together two departments, computer science and mechanical engineering, to work on a joint topic. The exertise in the two areas come together to create complex, accurate models which can validate and predict future behaviour.