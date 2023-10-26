# Testing the website locally

Obviously it is desirable to be able to verify changes to the 
scripts or the specs/schemas locally to verify them before
they are posted live on the LXI website.

This file documents how to do that.

## Pre-requisites

Running the website nominally requires:

* Python (3 or newer)
* jekyll
* bundle

## Basic steps

Basic steps are:

1. clone the website sources (LxiStandard.github.io).  This will pick up the
  most recently posted specifications and schemas (actions in those repositories
  push any changes to them to the website repo).

2. If you want to run with different *Specifications* or *lxi-api* put the new image 
  into *specificationsIN*/*schemasIN* directory.  Presumably you would only be doing 
  this if you want to verify the behavior of a new schema or specification 
  on the website rendering.

3. From the *site* subdirectory, run *bundle install*.  This should only be necessary 
   the first time you follow this process (or if you add components).

5. At the time of this writing, you will need to change 1 line in the file  
  *site/_config.yml*.  That is the line that declares the template. 

    Specifically, the *remote_theme* must be changed to just a *theme*

    ```
    theme: just-the-docs
    #remote_theme: just-the-docs/just-the-docs
    ```
  
    This is basically required because Ruby/Jekyll in unable to find the 
    theme from the *theme* keyword (the just-the-docs theme is not one
    of the themes automatically provided by github).  Future versions of 
    github pages (or Jekyll?) may change this.
    This is basically required because Ruby/Jekyll in unable to find the 
    theme from the *theme* keyword (the just-the-docs theme is not one
    of the themes automatically provided by github).  Future versions of 
    github pages (or Jekyll?) may change this.
   
1. From Linux, run the script *scripts/buildLXI.sh*, this is the script run
  by the github action.  If you are not on Linux, you can directly invoke the
  python scripts *scripts/buildSchemaPages.py* and/or
  *scripts/buildSpecificationPages.py*.

1. Run the server from the *site* subdirectory, using *bundle exec jekyll server*

Above verified on Ubuntu 22, 2023-10-17 (JM).

## Using the scripts/serve.ps1 script

This automates firing up the website inside a Docker container.

However, it is a little more fragile and does require Docker.  Worked on Windows 
the last time I tried it (JM).