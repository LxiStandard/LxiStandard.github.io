# The *public.lxistandard.org* web subdomain (*LxiStandard.github.io*)

This repository is used to generate the website at the *public.lxistandard.org* 
subdomain.  The purpose of this subdomain is to make certain key LXI documents
broadly available on the web.  That includes:

  * LXI Specifications that taken as a setup make up a 
  generation.  Where a generation is a set of self-consistent
  specifications that are required for conformance with LXI. 
  That is, a device that conforms to multiple specifications 
  (such as, the LXI Device specification and the LXI IP v6 
  specification) are required to comply with specified
  self-consistent versions of those specifications.

  * LXI Schemas used by the LXI API are available.  This includes the XML XSD schemas, documentation, and examples.

 * This website includes a standard github blog, useful for
  annotating updates to other parts of this website.

## Repository Summary

This repository is a conventional github pages website.  With the following special
features:

1. When a push is made to the *LxiStandard/Specifications* repository, actions in that
   repository perform a push to this repository.  All specifications are pushed to 
   the *specificationsIN* directory at the root of this repository.

   The workflow in this repository generates the html pages that make up the 
   Specifications section of this repository.

2. Similarly, when a push is made to the *LxiStandard/lxi-api* repository, actions
   in that repository perform a push to this repository of the schemas, examples, and documentation.

   The workflow in this repository generates the html pages that make up the 
   Specifications section of this repository.

## Repository workflow

The key work of creating the specifications and schemas area
of the website is performed by the shell script 
*scripts/buildLXI.sh*. It defers most of the work to python
scripts to create the schema pages (*scripts/buildSchemaPages.py*)
and the specification pages (*scripts/buildSpecificationPages.py*).

After these steps, the repository workflow follows conventional
github pages steps.

# Specifications

This section has documentation on the structure and usage of the
*LxiStandard/Specifications* repository.  This 
documentation would fit well in the README in that repository, 
however, to keep the documentation together, and because
the Python scripts that consume the files in that repository
are in this repository, the documentation is here.



## Organization of the Specifications repository

The Specifications repository loosely follows the organization
that is exposed to customers on the website as illustrated here:


````
├── specifications
│   ├── LXI_1.5
│   │   ├── */*.docx
│   │   ├── */*.pdf
│   │   ├── VersionInfo.md
│   ├── LXI_1.6
│   │   ├── */*.docx
│   │   ├── */*.pdf
│   │   ├── VersionInfo.md
...
````
Additional directories may be added for additional
LXI **Generations**.

The *VersionInfo.md* file contains the description of this 
particular LXI Generation, and any caveats (for instance
if the version is under construction).  When the user navigates
to this generation page they will see this markdown page 
with a table appended to it by the Python script providing
links to the docx and pdf files.

The table of docx and pdf files attempts to parse the files
using the Python-style regular expression:

  ```r"([\w\d-]+)_([\d\.]+)_(\d\d\d\d-\d\d-\d\d).(.*)"```

It should be immediately clear to the casual reader that 
this parses a file name of the form:

  ```My_cool_LXI_Spec_1.2.3_1958-05-02.pdf```

If the docx or pdf file names conform to this convention, then
the table columns are populated with the specification name
('My_cool_LXI_Spec'), the version ('1.2.3'), the date
('1958-05-02'); and links are placed in the table for
docx and pdf files.

If the filename does not conform with this convention, it 
is placed in the table on a line by itself with no attempt
to combine docx/pdf onto a single line or parse the contents.

Clearly, this regular expression could be easily adapted for
some other filename convention, or to make it more flexible 
(for instance accepting hyphens as separators).

**Any push to the *LxiStandard/Specifications* repository 
will result in all of the Specifications being pushed into 
the *LxiStandard/lxistandard.github.io* where these actions
are run.**

## The *buildSpecificationPages.py* program

As noted above, this program is called by the buildLXI.sh
script as part of the workflow for the 
*LxiStandard/lxistandard.github.io* repository.

This script is conventional Python and should not require
substantial external documentation. The basic function 
is to read the SpecificationIN directory and create a 
specifications directory in the site subdirectory.  In 
addition, the script scans all the file names in each 
subdirectory and creates the table visible on the website.

# Schemas


This section has documentation on the structure and usage of the
*LxiStandard/lxi-api* repository.  This 
documentation would fit well in the README in that repository, 
however, to keep the documentation together, and because
the Python scripts that consume the files in that repository
are in this repository, the documentation is here.

The README documetation in the lxi-api repository has 
detailed documentation regarding the use of the Python
scripts that generate the documentation from the 
XSD files.  None of the information is repeated here, although
the output of that generation step is included with
the XSD files.


## Organization of the lxi-api repository

The lxi-api repository loosely follows the organization
that is exposed to customers on the website as illustrated here:


````
├── scripts
├── lxi-api
│   ├── InstrumentIdentification
│   │   ├── 1.0.xsd
│   │   ├── 2.0.xsd
│   │   ├── <additional versions>.xsd
│   │   ├── <example1>.xml
│   │   ├── <example2>.xml
│   │   ├── SchemaInfo.md
│   ├── <replicated for each schema>
...
````

You can see from the functioning website how this information 
is published to the website.

  * For each schema a page is created starting with the 
  *SchemaInfo.md*.  This should be a substantive file 
  describing the use of the schema and anything important
  about changes between versions.
  * After this information, a table is inserted with links
  for the schema files and the documetation files (these
  documentation files are generated by the Python script
  in the *LxiStandard/lxi-api* repository.)