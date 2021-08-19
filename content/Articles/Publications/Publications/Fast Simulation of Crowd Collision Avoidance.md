Title: Fast Simulation of Crowd Collision Avoidance
Slug: Simulating ORCA People Crowds
Date: 2019-06-01
Published: 2019-06 
Summary: Visually simulating numerous people with steering
Submission: Published
Journal: CGI 2019: Advances in Computer Graphics
DOI: https://doi.org/10.1007/978-3-030-22514-8_22
Manuscript: /static/manuscripts/ORCA_GPU_Paper.pdf

Performing calculations on the GPU means that the results can be easily and speedily visualised, since there is no need for CPU->GPU data transfer for visualising, it is already present on the device. By using fast and efficient linear program solving on the GPU it is possible to simulate many thousands of people using more complex methods than would be possible for CPU-based methods. 

This paper demonstrates the performance of using the ORCA steering algorithm with many thousands of people in real-time.

The image below shows 10,000 people, separated into 8 colored groups steering within an open space. The insert image in the bollow right shows a head-level view, including the ability to visualise people of different sizes, textures, and movement speed.

<img src='/static/images/regular8way.png' style='width: 600px;' alt='10,000 people in the Unreal Engine'>
