# cohort
Reverse engineering is often a solitary activity out of necessity rather than preference.  There are many working methodologies and many tools that exist, but no good way to share the information gleaned from them.  Cohort aims to solve that problem by extracting information from various popular tools used by reverse engineers (IDA, Radare2, etc), committing that information to version control, and then allowing that information to be imported into other tools.  Using this tool, multiple people could tackle the task of reverse engineering a massive binary and share the knowledge they uncover independent of their preferred tools.

Ideas:
  * Use git for version control?  We can likely store this information in a plaintext format that will enable diffs to be intelligble.
  * Store information in a graph, with the root node being an application, children of that root being a binary children of the binary being a cfg, method table, etc)
  * Use folders to organize information heirarchies?  One folder for the application, subfolders for binaries, files for cfg, methods, etc.
  * Store a hash of each binary so we can ensure that the symbols we attempt to load apply to that binary.
  * Store names for known memory locations (variables, strings, etc)
  * For methods, store comments we write, pseudocode we generate or write, local variable names, etc.  Store only information that pertains directly to the specific bytes that make up that method, leave things like xrefs to the binary node to store.
  * Include a hash of the bytes that make up a method so we can recognize it independent of a binary.
  * Allow certain "snippets" common in the binary to be automatically commented, colored, etc (e.g. `xor eax, eax  ; sets eax to 0`).  Maybe also allow these snippets to be shortened to some alternate representation.  For example, if we encounter a huge block of operations that just obfuscate the result of setting eax to 0, we could make it so that these obfuscation snippets are recognized and have a shorthand that can replace the actual displayed text in a disassembly window (code can be expanded by clicking an expander or something).
  * Store information like the cfg extracted during analysis?
  * Store binary information, method information, resource information, etc in such a way that each can be extracted and used in other projects through some sort of "find known symbols" feature (one that looks for known methods, snippets, resources, etc and automatically comments them).
