================================
Markdown to RST table conversion
================================

The **prebuild.py** and **postbuild.py** scripts enable markdown table
rendering when using Sphinx and the recommonmark extension.

#. Prebuild.py makes temporary copies of markdown files and converts markdown
   tables fenced by ``<!--table--> <!--endtable-->`` comment lines to RST
   tables fenced by ``eval_rst`` code blocks.

#. Sphinx builds HTML using the markdown files with the converted
   rst tables.

#. Postbuild.py returns the markdown files to their original state and removes
   the temporary files created by prebuild.py.


Formatting markdown tables
~~~~~~~~~~~~~~~~~~~~~~~~~~

To label a markdown table for conversion, add ``<!--table-->`` on the line
prior to the table and ``<!--endtable-->`` on the line after the table.
For example:

.. code:: ini

   <!--table-->
   | Tables        | Are           | Cool  |
   | ------------- |-------------- | ----- |
   | col 3 is      | nifty         | $1600 |
   | col 2 is      | awesome       |   $12 |
   | zebra stripes | are neat      |    $1 |
   <!--endtable-->

Limitations
-----------

The underlying markdown to RST conversion is handled by Pandoc, but there are
some limitations to what it can parse.

**HTML tags**

Pandoc converts HTML tags in markdown tables to raw HTML directives in RST.
This breaks the table syntax.

The **prebuild.py** and **postbuild.py** scripts can handle ``<br>`` and
``<li>`` HTML tags. Do not use any other HTML tags within markdown tables.

An alternative to ``<li>`` tags is ``&bull;``, which inserts a bullet point
character.

If you require other HTML tags, please open an issue in
`rackerlabs/docs-rackspace <https://github.com/rackerlabs/docs-rackspace>`_
to have support added.

**Empty cells**

The conversion process cannot handle empty cells in tables. If you require
a blank cell, use ``&nbsp;`` in the cell. Example:

.. code:: ini

   <!--table-->
   Correct name | Notes
   --- | ---
   Apache | This is a good name.
   Bash shell | &nbsp;
   CentOS | &nbsp;
   Git	 | We all love Git.
   <!--endtable-->

See `HTML named special symbols
<http://turner.faculty.swau.edu/webstuff/htmlsymbols.html>`_.


Configuration
~~~~~~~~~~~~~

The **prebuild.py** and **postbuild.py** scripts read configuration settings
from the ``tox.ini`` file in the ``[mdsphinx]`` section. The following settings
are available:

docdir
   The documentation directory, relative to ``tools/``. This is usually
   ``../doc/``.

mdsuffix
   The suffix being used for markdown files. This is usually ``.md``.

tempsuffix
   The temporary suffix used during the conversion process. This is usually
   ``.temp``.

ignore
   A comma-separated list of files to ignore. Use file names only without
   paths. Does not accept directories or wildcards (\*).

debug
   ``True`` - show debugging output.

   ``False`` - hide debugging output.

**Sample configuration**

.. code:: ini

   [mdsphinx]
   docdir = ../doc/
   mdsuffix = .md
   tempsuffix = .temp
   ignore = README.md, draft.md
   debug = False


Makefile html target
~~~~~~~~~~~~~~~~~~~~

The **prebuild.py** and **postbuild.py** scripts are integrated into the
**Makefile** html target. They run automatically when the ``tox -e checkbuild``
or ``make html`` commands are run.

.. code:: ini

   html:
   @echo "\nConverting MD tables to RST"
   python3 ../tools/prebuild.py
   @echo
   $(SPHINXBUILD) -E -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
   @echo "\nCleaning up from MD table conversion"
   python3 ../tools/postbuild.py
   @echo
   @echo "Build finished. The HTML pages are in $(BUILDDIR)/html."


Prebuild.py
~~~~~~~~~~~

.. automodule:: prebuild
   :members:


Postbuild.py
~~~~~~~~~~~~

.. automodule:: postbuild
   :members:


Example input and output
~~~~~~~~~~~~~~~~~~~~~~~~

Prebuild.py converts a markdown file with the following content:

.. code:: ini

   # Heading 1
   This is some text

   ## Heading 2
   This is some more text. This is an *emphasized* word.

   <!--table-->
   | Tables        | Are           | Cool  |
   | ------------- |-------------- | ----- |
   | col 3 is      | nifty         | $1600 |
   | col 2 is      | awesome       |   $12 |
   | zebra stripes | are neat      |    $1 |
   <!--endtable-->

   More paragraphs, tables, and other markdown text.

to a markdown file with the following content:

.. code:: ini

   # Heading 1
   This is some text

   ## Heading 2
   This is some more text. This is an *emphasized* word.

   ```eval_rst
   .. list-table::
      :widths: 33 33 33
      :header-rows: 1

      * - Tables
        - Are
        - Cool
      * - col 3 is
        - nifty
        - $1600
      * - col 2 is
        - awesome
        - $12
      * - zebra stripes
        - are neat
        - $1

   ```

   More paragraphs, tables, and other markdown text.
