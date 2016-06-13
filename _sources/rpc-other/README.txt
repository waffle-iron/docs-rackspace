======================
RPC team documentation
======================

Non-product material for the RPC documentation team.

- How to documentation, including how to install OpenStack on the Rackspace
  public cloud
- other information to be listed

Files
~~~~~

The following files are critical for various reasons. Please use caution when
making changes:

.git
   Git version control files. DO NOT TOUCH.

.gitignore
   List of files and directories that are excluded from version control.

.nojekyll
   Marker file to prevent GitHub Pages from treating content as a Jekyll build.
   Required for displaying Shinx documentation builds correctly on
   github.rackspace.com.

tox.ini
   Configuration file for tox.

Tox
~~~

This project uses Tox to run tests. Tox also builds the documentation during
its ``checkbuild`` test, and this can be used as an alternative to building
with the ``make html`` command.

If you are unfamiliar with tox, note that you can run the whole test suite,
including building the docs, from anywhere within the docs-rpc repo like this:

$ tox

If you don't want to run all the other checks and just want to build the docs:

$ tox -e checkbuild

Take a look in doc-rpc/tox.ini for other target environments if you want to run
different tests in isolation, for example:

$ tox -e checkniceness
