# The *public.lxistandard.org* web subdomain (*LxiStandard.github.io*)

This repository is used to generate the website at the *public.lxistandard.org* 
subdomain.  The README files for the *LxiStandard/lxi-api* repository and the
*LxiStandard/Specifications* repos point to this documentation for details
on the required file names and organization.

**For step-by-step instructions to just update the specifications
that are posted, see the README file in the *Specifications*
repository:**
[Posting New Specifications](https://github.com/LxiStandard/Specifications/blob/main/README.md)

The purpose of this subdomain is to make certain key LXI documents
publicly available on the web.  This includes:

  * LXI Specifications that taken as a set make up a 
    generation.  Where a generation is a set of self-consistent
    specifications that are required for conformance with LXI. 
    That is, a device that conforms to multiple specifications 
    (such as, the LXI Device specification and the LXI IP v6 
    specification) are required to comply with specified
    self-consistent versions of those specifications.

  * LXI Schemas used by the LXI API are available.  This includes
    the XML XSD schemas, documentation, and examples.

 * This website includes a standard github blog, useful for
   annotating updates to other parts of this website.  Blog
   entries can be made to site/_posts, preceding the filename
   with the date and following the pattern of other blog
   posts already there.

## Repository Summary

This repository is a conventional github pages website.  With the following special
features:

1. When a push is made to the *LxiStandard/Specifications* repository, actions in that
   repository perform a push to this repository.  All specifications are pushed to 
   the *specificationsIN* directory at the root of this repository.

   The workflow in this repository generates the html pages that make up the 
   Specifications section of this repository.

2. Similarly, when a push is made to the *LxiStandard/lxi-api* repository, actions
   in that repository perform a push to this repository of the schemas, examples,
   and documentation.

   The workflow in this repository generates the html pages that make up the 
   Specifications section of this repository.

## Repository Workflow

The repository workflow is triggered for any push.  It creates 
the content that is created programmatically, then has standard
github pages actions.

The key work of creating the specifications and schemas area
of the website is performed by the shell script 
*scripts/buildLXI.sh*. It defers most of the work to python
scripts to create the schema pages (*scripts/buildSchemaPages.py*)
and the specification pages (*scripts/buildSpecificationPages.py*).

After these steps, the repository workflow follows conventional
github pages steps.

# Specifications Pages

This section has documentation on the structure and usage of the
*LxiStandard/Specifications* repository.  This 
documentation would fit well in the README in that repository, 
however, to keep the documentation together, and because
the Python scripts that consume the files in that repository
are in this repository, the documentation is here.

**For step-by-step instructions to update the specifications
that are posted, see the README file in the *Specifications*
repository:**
[Posting New Specifications](https://github.com/LxiStandard/Specifications/blob/main/README.md)

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

The *VersionInfo.md* file contains markdown with any
appropriate customer-facing documention for this 
particular LXI Generation. The *VersionInfo.md* should 
also contain any caveats (for instance
if the version is under construction) regarding this 
generation or the files in it.  

When the user navigates
to the generation page for a set of specifications they 
will see this markdown page with a table appended to it 
by the Python script providing links to the docx and pdf files.

The table of docx and pdf files attempts to parse the files
using the Python-style regular expression:

  ```r"([\w\d-]+)_([\d\.]+)_(\d\d\d\d-\d\d-\d\d).(.*)"```

It should be immediately clear to the casual reader that 
this parses a file name of the form:

  ```My_cool_LXI_Spec_1.2.3_1958-05-02.pdf```

If the docx or pdf file names conform to this convention, then
the table columns are populated with the specification name
('My_cool_LXI_Spec'), version ('1.2.3') and date
('1958-05-02').  Link are placed on each row for 
docx and pdf files.

If the filename does not conform with this convention, it 
is placed in the table on a line by itself with no attempt
to combine docx/pdf onto a single line or parse the filename.

Clearly, this regular expression could be easily adapted for
some other filename convention, or to make it more flexible 
(for instance accepting hyphens as separators).  This is
intentionally a little finicky to encourage consistent 
filenaming.

**Any push to the *LxiStandard/Specifications* repository 
will result in all of the Specifications being pushed into 
the *LxiStandard/lxistandard.github.io* where these actions
are run.**

## The *buildSpecificationPages.py* Program

As noted above, this program is called by the buildLXI.sh
script as part of the workflow for the 
*LxiStandard/lxistandard.github.io* repository.

This script is conventional Python and should not require
substantial external documentation. The basic function 
is to read the *SpecificationIN* directory and create a 
specifications directory in the site subdirectory.  In 
addition, the script scans all the file names in each 
subdirectory and creates the table visible on the website.

# Schema Pages

This section has documentation on the structure and usage of the
*LxiStandard/lxi-api* repository.  This 
documentation would fit well in the README in that repository, 
however, to keep the documentation together, and because
the Python scripts that consume the files in that repository
are in this repository, the documentation is here.

The README documentation in the lxi-api repository has 
detailed documentation regarding the use of the Python
scripts that generate the documentation from the 
XSD files.  None of that information is repeated here, although
the output of that generation step is included with
the XSD files. 
See: [LXI API README](https://github.com/LxiStandard/lxi-api/blob/main/README.md).


## Organization of the *LxiStandard/lxi-api* Repository

The lxi-api repository loosely follows the organization
that is exposed to customers on the website as illustrated here:


````
├── scripts
├── lxi-api
│   ├── InstrumentIdentification
│   │   ├── 1.0.xsd
│   │   ├── 2.0.xsd
│   │   ├── 1.0.html
│   │   ├── 2.0.html
│   │   ├── <additional versions>.xsd
│   │   ├── <example1>.xml
│   │   ├── <example2>.xml
│   │   ├── SchemaInfo.md
│   ├── <replicated for each schema>
...
````

You can see from the functioning website how this information 
is published to the website.

  * The html files are generated by the actions in 
    the lxi-api repository.  The documentation is scraped
    from the schema files to create the html.
  * For each schema, a page is created starting with the 
    *SchemaInfo.md*.  This should be a substantive file 
    describing the use of the schema and anything important
    about changes between versions.
  * A table is appended to the end of *SchemaInfo.md* with links
    for the schema files and the documetation files arranged
    by version (these are the
    documentation files generated by the Python script
    in the *LxiStandard/lxi-api* repository).
  * If present, links for the examples are inserted. Any
    documentation regarding the examples should be put in
    a table in the *SchemaInfo.md* file.

## The *buildSchemaPages.py* Program

The *buildSchemaPages* program is somewhat simpler than the 
*buildSpecificationPages.py* program because it does not need
to coalesce multiple formats of a spec into a single table entry
or parse off dates and versions from the filename.

*buildSchemaPages.py* walks the directory structure indicated above
and builds a table of the schemas and the corresponding
documentation, then appends the list of XML examples.

The program starts with the *SchemaInfo.md* file and 
appends a table of the schema files.  The table of 
schema files includes a link to the schema and documentation
for each version of the schema in the repository.

The file names are NOT parsed by the Python.  They are 
presumed to be in the format shown in the file list above.  
That is, *<major number>.<minor number>*.

Finally, the XML files are all presumed to be examples
and links to them are appended at the end.  Any documentation 
appropriate for the XML files (for instance, a table describing 
each one) should be included in the *SchemaInfo.md* file.

**Any push to the *LxiStandard/lxi-api* repository 
will result in the schemas being pushed into 
the *LxiStandard/lxistandard.github.io* where these actions
are run.**
