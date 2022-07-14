---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }} #Date paper was published, or rought date of relevance
draft: true
summary:
submission: "Draft" #or "Published"
journal: #Submitted journal name
doi: https://doi.org/ #...
manuscript: "../manuscripts/" #add the pdf to the content/publications/manuscript folder and insert filename here
---
