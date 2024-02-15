---
title: "Ph.D Thesis"
date: 2023-11-08T12:44:04Z #Date paper was published, or rought date of relevance
draft: false
summary: My PhD thesis
submission: "Published" #or "Published"
journal: #Submitted journal name
doi: https://etheses.whiterose.ac.uk/33512/
manuscript: "../manuscripts/_John_Charlton____Thesis.pdf" #add the pdf to the content/publications/manuscript folder and insert filename here
---

The culmination of many years of hard work, struggle, procrastination, anxiety and effort.

### The Ph. D Viva
Many thanks to [Peter Lawrence](https://www.gre.ac.uk/people/rep/faculty-of-engineering-and-science/peter-lawrence) at the University of Greenwich for reading through this, and providing many questions to me during my viva.
And thanks to [Dawn Walker](https://www.sheffield.ac.uk/dcs/people/academic/dawn-walker) at Sheffield University for also grilling me in the viva. It was a memory and lasting experience, and I'm glad it's over!

### Abstract:
Central to simulating pedestrian crowds is their motion and behaviour. It is required to understand how pedestrians move to simulate and predict scenarios with crowds of people. Pedestrian behaviours enhance the range of motions people can demonstrate, resulting in greater variety, believability, and accuracy. Models with complex computations and motion have difficulty in being extended with additional behaviours. This is because the structure of these models are not designed in a way that is generally compatible with collision avoidance behaviours. To address this issue, this thesis will research a possible pedestrian model that can simulate collision response with a wide range of additional behaviours. The model will do so by using constraints, a limit on the velocity of a person's movement. The proposed model will use constraints as the core computation. By describing behaviours in terms of constraints, these behaviours can be combined with the proposed model. Pedestrian simulations strike a balance between model complexity and runtime speed. Some models focus entirely on the complexity and accuracy of people, while other models focus on creating believable yet lightweight and performant simulations. Believable crowds look realistic to human observation, but do not match up to numerical analysis under scrutiny. The larger the population, and the more complex the motion of people, the slower the simulation will run. One route for improving performance of software is by using Graphical Processing Units (GPUs). GPUs are devices with theoretical performance that far outperforms equivalent multi-core CPUs. Research literature tends to focus on either the accuracy, or the performance optimisations of pedestrian crowd simulations. This suggests that there is opportunity to create more accurate models that run relatively quickly. Real time is a useful measure of model runtime. A simulation that runs in real time can be interactive and respond live to user input. By increasing the performance of the model, larger and more complex models can be simulated. This in turn increases the range of applications the model can represent. This thesis will develop a performant pedestrian simulation that runs in real time. It will explore how suitable the model is for GPU acceleration, and what performance gains can be obtained by implementing the model on the GPU.
