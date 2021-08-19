# Personal Site

## Install and Run

Depends on `Python` and `pipenv`. Should be as simple as running `pipenv shell` in the root folder to get started.

## Test site

Run `pelican --listen` to start a local testing server

Run `pelican content` to update any changes made to the source

## Theme

A Pelican Theme is both a way to style the website as well as rules for handling automated content to put on webpages. The styling is handled by `static` folder theme information. Information on pages is handled in `templates` folder of the theme. Templates are useful to create customised views of articles. Pages that use a template have the metadata `template: ...` at the start of the markdown page.

## Publishing

Run `make github`, which uses the base `pelicanconf.py` and adjusts production-ready values (such as generating feeds). This pushes the output folder to the `site` branch of the personal page.

To see the published site files, visit the e.g. `site` git branch.
