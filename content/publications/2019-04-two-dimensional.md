---
title: "Two-Dimensional Batch Linear Programming on the GPU"
date: 2019-04-01T11:37:43+01:00
summary: An efficient algorithm for solving multiple linear programs on the GPU.
submission: Published
journal: Journal of Parallel and Distributed Computing
doi: https://doi.org/10.1016/j.jpdc.2019.01.001
manuscript: ../manuscripts/Two_Dimensional_Batch_Linear_Programming_Post-accept.pdf
---

---
![Naive implementation](../images/OldWork.png)
![Paper implementation](../images/NewWork.png)

Implementation of "Work Units" - smallest common work load that the linear program can be composed of. Above: a naive implementation that fails to utilise some of the threads within a GPU warp. Below: distributing work units evenly across GPU threads to more fully utilise the device