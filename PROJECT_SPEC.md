**THIS DOCUMENT IS A WIP.  Feel free to give feedback and suggest changes, but 
DO NOT use this spec (yet) to store binary data.**

# Cohort Metadata Project V0.1 (beta)
This document describes v0.1 of the Cohort Metadata Project (CMP) format.  The
CMP format is an data storage specification used to hold information extracted
from binary analysis tools.  This project format is designed to be highly
accessible, extendable, and open to being placed under version control (git,
mercurial, etc) for easy collaboration between binary analysts.

## Core design principles
The Cohort Metadata Project
 1. **Never store binary data**  

    A CMP should be able to be created and understood entirely by a human using
    a plain text editor.  When making decisions on what data to store in a CMP,
    use this as a rule of thump.

    This probably seems a little odd, but there's some solid logic behind this
    decision.  Firstly, version control technologies at the time of this
    document's publication primarily operate on text-based formats (aka code).
    In order to leverage the full breadth of this technology for collaboration,
    we need to stick with plaintext as much as possible.  Secondly, we want a
    CMP project to be readable without requiring specialized tools.  There are
    many binary analysis tools and methodologies, and until there is a unified
    and popular standard, there will almost always be at least one person who
    will not have access to all the information that can be extracted from a
    binary.  Until that information can be imported into their tool or
    workflow, they should be able to read and write to a CMP with a text
    editor.
    
 2. **Avoid storing bytes from analyzed binary**

    Unless absolutely necessary, never store bytes copied from a binary under
    analysis in a CMF file.  This is useful both for efficient storage (we
    don't want to store the entire binary under analysis) and for avoiding
    potential copyright law violations when sharing a CMF file.

    If you find yourself needing to store bytes from the binary that a CMF file
    would describe, opt instead to store the byte range (start and ending
    offset in the file) that your 

  3. **One CMP describes one binary file and it's resources**

## Format
CMPs are represented as normal directories and files.  CMPs can be shared in a
compressed format, but are operated on as a system of files and directories.
Compressed CMPs should be stored as <project>.cmp.<compression format> (e.g.
kernel.dll.cmp.gz)

project.xml
stores info about the project (name, description, binary name, binary hash,
etc)

.cohort
stores metadata and internal information about the project.  This is meant to
be used internally by the main cohort app for things like local storage,
caching, and anything else we wouldn't want to be committed to version control.
It also is used by the cohort tool to determine if it's operating inside a
directory that represents a CMP.

symbol ID
Data items in a binary are identified by their offset in the binary and a
nonce.  The nonce is used to differentiate references to a particular location
that have different purposes.

/
contains any core information about the project.

/{module}/
different types of information that can be extracted from a binary should be
catagorized and stored in a module folder.  modules provide a spec for storing
extracted information so that the information may be universally imported and
exported.  Modules should follow certain assumptions I'll write up in a base
spec (identifying symbols, working properly with XREFS, etc) so that they can
interoperate.

ex.
/data/xrefs
/data/functions
/data/structs
/data/classes

modules can have submodules
ex.
/data/functions/disassembly
/data/functions/decompilation
