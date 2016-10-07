============================================
Convert grid tables to list-table directives
============================================

You can use the ``table.py`` script in the `docs-rackspace/tools
<https://github.com/rackerlabs/docs-rackspace/tree/master/tools>`_ repo to
convert table grids to list-table directives in an rst file.

Usage
-----

#. Download ``table.py`` from the GitHub repo to a directory on your local
   machine.

#. Convert grid tables in a file to list-tables. The result is output
   to stdout::

      $ python tables.py input.rst

#. Convert several files::

      $ python tables.py input1.rst input2.rst

      $ python tables.py *.rst

Options
-------

-c, --create    create new files ``*.rst.new`` with the converted tables.
                Original files are unchanged.
-r, --replace   modify input files, replacing grid tables with list-tables

.. warning::

   The script does not perform any tests on the conversion nor does it
   rollback if it encounters an error. Using the ``--replace`` option
   replaces the source text completely. To prevent data loss, use the
   ``--create`` option and confirm the conversion is correct before removing
   the original source file.

.. important::

   Always build your document and compare the rendered list-table to the
   original rendered grid table. It is very possible that some errors may
   occur that require manual fixes, especially when converting complex tables.

   The script does not handle cells that span multiple rows or columns. If
   you convert a table with these types of cells you may receive a parsing
   error when running sphinx-build::

       ERROR: Error parsing content block for the "list-table" directive:
              uniform two-level bullet list expected, but row 2 does not
              contain the same number of items as row 1 (4 vs 3)

   This indicates that the list-table needs manual clean-up. Look for lines
   like this in the source::

      * - Alarms
        - Acknowledge an alarm    * - hello
        -
        - Yes

   Compare with the original table to determine the correct structure of the
   broken row.

Notes
-----

- The script does not create titles for tables. After conversion, you may
  want to manually add titles.

- The script sets all columns to the same width: ``100 / col_num``. After
  conversion, you may want to manually edit ``:width:``.

- The script automatically uses the first row of the table as a header.
  After conversion, you may want to manually edit ``:header-rows:``.
