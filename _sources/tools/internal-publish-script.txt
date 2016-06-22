========================================
Publishing to pages.github.rackspace.com
========================================

The :ref:`publish.sh` script publishes documentation to a Rackspace GitHub
pages URL accessible only to internal users (pages.github.rackspace.com). To
use the script, you have to do some initial setup to fetch the content for
publishing.

.. warning::

   After running the script, always check the published books. The script does
   not catch errors and has no test suite. Use it with cautious optimism.


Initial setup
~~~~~~~~~~~~~

The **publish.sh** script enables you to publish internal content from an
external github.com repository to an internal github.rackspace.com
gh-pages URL. It assumes two repositories:

- an internal repository on github.rackspace.com which you clone to your local
  machine
- a public or private repository on github.com, which is set as the upstream
  source for your local clone of the internal repository

.. warning::

   Do not edit the internal repository directly, as it acts as a
   mirror of the external repository. Make all changes upstream in the
   github.com repository then push those changes to the internal
   github.rackspace.com repository.

These instructions use **docs-rpc** as an example repository. Update the
script and substitute your repositories as required.

Run the following commands while connected to the Rackspace network directly
or through VPN.

#. Clone the internal repository:

   .. code::

      $ git clone git@github.rackspace.com:rpc-internal/docs-rpc.git

#. Change into the cloned **docs-rpc** directory and set the upstream to the
   rackerlabs/docs-rpc repository:

   .. code::

      $ cd docs-rpc
      $ git remote add upstream git@github.com:rackerlabs/docs-rpc.git

   .. note::

      In order to avoid confusion with the rackerlabs repository of the same
      name, you may want to change the directory name of **docs-rpc**.

#. Confirm your setup by pulling from upstream and pushing to origin:

   .. code::

      $ git fetch upstream
      $ git merge upstream/master
      $ git push origin master

#. Create local versions of the stable upstream branches:

   .. code::

      $ git checkout v10
      $ git checkout v11

#. Checkout master. You are now ready to publish internally.

   .. code::

      $ git checkout master


Publishing
~~~~~~~~~~

Run the following command while connected to the Rackspace network directly
or through VPN.

#. To build and publish the content using GitHub pages, run the **publish.sh**
   script from the master branch of the cloned enterprise repository:

   .. code::

      $ . publish.sh

#. Check the published output at the URL provided by the script. For the
   **docs-rpc** books, this is
   https://pages.github.rackspace.com/rpc-internal/docs-rpc/. You must be on
   the Rackspace network to view this page.

For more information on the commands run, see the code comments in the
:ref:`publish.sh` script.

For more information on publishing to gh-pages manually, see
`Creating project pages manually
<https://help.github.com/articles/creating-project-pages-manually/>`_.


.. _publish.sh:

publish.sh
~~~~~~~~~~

The following version of the **publish.sh** script publishes the internal-only
v10 and v11 RPC books. It also publishes the internal books from the master
branch (v12), which are labelled as DRAFT.

Adapt the script as required for your repositories.

.. code::

    #!/bin/bash

    # Helper script for publishing RPC documentation to pages.github.rackspace.com.
    # Run from the master branch of the internal RPC repository.

    # set repo root directory
    GITDIR=`git rev-parse --show-toplevel`

    # set source directories
    SOURCE='internal common figures'
    V11SOURCE='internal/rpc-v11-faq-internal internal/rpc-v11-install internal/rpc-v11-ops-internal internal/rpc-v11-releasenotes-internal-supp'
    V10SOURCE='internal/rpc-v10-faq-internal internal/rpc-v10-installation internal/rpc-v10-releasenotes-internal-supp'

    # set branches to build
    BRANCHES=(v10 v11 master)

    # ensure branches are up-to-date
    for branch in ${BRANCHES[@]}; do
        cd $GITDIR
        git checkout $branch
        git fetch upstream
        git merge upstream/$branch
        git push origin $branch
    done

    # checkout gh-pages branch and delete contents except . files
    git checkout gh-pages
    find * -not -name ".*" -delete

    # checkout source directories and reset HEAD
    git checkout master $SOURCE
    git checkout v11 $V11SOURCE
    git checkout v10 $V10SOURCE
    git reset HEAD

    # build html from rst in internal directory
    cd internal
    make html

    # move html files to root directory
    mv -fv _build/html/* ../

    # remove source files
    cd $GITDIR
    rm -rf $SOURCE

    # add, commit, and push new html files
    git add .
    git commit -m "gh-pages: `git log master -1 --pretty=short --abbrev-commit`"
    git push origin gh-pages

    # checkout master and signal completion
    git checkout master
    echo
    tput setaf 2
    echo "Published at: https://pages.github.rackspace.com/rpc-internal/docs-rpc/"
    tput sgr0
