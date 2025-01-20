# Personal Site

Code for my personal site. Built using [Hugo](https://gohugo.io)

## Getting this repo
This repo contains a submodule. When cloning, ensure submodules are also incorporated, either with `git clone --recurse-submodules #this-repo.git`, or for already clones repos, 
```
git submodule init 
git submodule update
```

## To Create a published paper

`hugo new publications/$name.md` will produce a skeleton document. Fill out the front matter.

## Developing the site

Run `hugo server` for a live site to test changes on.

`git push` changes to github. The workflow actions will run to update the actual site itself with the changes.