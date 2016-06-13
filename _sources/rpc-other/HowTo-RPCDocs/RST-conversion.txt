===========================
RST conversion instructions
===========================

With docs.rackspace.com being decommissioned, we are implementing a new
toolchain and publishing to a new external site developer.rackspace.com
and internal site (TBD).

RPC and VMware documentation will be RST source built with Sphinx, and
migrated from github.com/rpcdocs/rpcdocs and
https://github.com/rpcdocs/dedicated-vcloud, to
https://github.com/rackerlabs/docs-rpc and
https://github.com/rackerlabs/docs-dedicated-vcloud respectively.

Instructions to convert DocBook to RST is described below.

Prerequisites :sub:`:sub:`:sub:`:sub:`:sub:`~`````\ ~~

Install the following tools:

-  Pandoc: http://pandoc.org/installing.html
-  Tox:

``pip install tox``

RST conversion :sub:`:sub:`:sub:`:sub:`:sub:`:sub:`~``````\ ~

1. Add your name to the migration tracking sheet
   https://docs.google.com/spreadsheets/d/1mYootV7otazacamT32Tn8MlqAjADQA75661JHTojwRQ/edit#gid=0

-  Fork the new docs repository *https://github.com/rackerlabs/docs-rpc*
   (and *https://github.com/rackerlabs/docs-dedicated-vcloud* for VMware
   documentation). Clone and work in your personal fork.
-  Update your local rpcdocs directory.
-  Download the xml2rst.sh script at
   https://github.com/rackerlabs/docs-migration/tree/master/tools.
-  Run the script in the rpcdocs/ \ *GUIDE*/src/docbx/ directory to
   convert XML files to RST files.
-  Create a local branch in the docs-rpc directory.
-  Create a local folder for the guide in the docs-rpc/doc directory.
-  Copy across the converted RST files from
   rpcdocs/ \ *GUIDE*/src/docbx/ to docs-rpc/doc/ \ *GUIDE*/source, and
   images to docs-rpc/doc/ \ *GUIDE*/figures.
-  Rename and clean up RST files. See
   https://github.com/rackerlabs/docs-rpc/tree/master/doc/admin as an
   example.
-  Pandoc has its quirks, so check all the content has been migrated
   from the source files.
-  Follow RST conventions documented in
   http://docs.openstack.org/contributor-guide/rst-conv.html.
-  Clean up tables where the pandoc conversion just outputs paragraphs.
-  Remove numbering from Example titles and Table titles.
-  Remove "programlisting" "screen" and "literallayout" from .. code::
   lines.
-  Build the document and check for errors:

``tox`` - Commit your changes per
https://github.com/rpcdocs/rpcdocs/blob/master/README.rst#working-with-rpc-releases-and-branches.
