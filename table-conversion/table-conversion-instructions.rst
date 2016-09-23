============================================
Convert table grids to list-table directives
============================================

You can use the ``table.py`` script in the
``https://github.com/rackerlabs/docs-rackspace/tree/master/tools`` repo to
convert table grids to list-table directives in an rst file.

#. Download ``table.py`` from the GitHub repo to a directory on your local
   machine.


#. In terminal,  type ``python table.py filename.rst`` (the name of file that
   you want to convert).

   Doing this gives you the conversion in the terminal window. You can cut and
   paste from the terminal window into your .rst file.

   You can also use ``python table.py inputfilename.rst > outputfilename.rst``,
   which will put the converted file into the ``outputfilename.rst``. You can
   cut and paste from that file, or simple replace the ``inputfilename.rst``
   file with the ``outputfilename.rst`` file in your documents. Make sure you
   rename it or adjust any indexes as necessary.
