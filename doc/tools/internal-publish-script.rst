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


Prerequisites
~~~~~~~~~~~~~

Sphinx is required for building HTML from the RST source:

.. code::

   $ sudo pip install sphinx

(Optional) Install tox for testing. It can also run the publish.sh script.

.. code::

   $ sudo pip install tox


Initial repository setup
~~~~~~~~~~~~~~~~~~~~~~~~

The **publish.sh** script enables you to publish internal content from an
external github.com repository to an internal *github.rackspace.com*
gh-pages URL. It assumes two repositories:

- an internal repository on *github.rackspace.com* which you clone to your
  local machine
- a public or private repository on *github.com*, which is set as the upstream
  source for your local clone of the internal repository

.. warning::

   **Do not edit the internal repository directly**, as it acts as a
   mirror of the external repository. Make all changes upstream in the
   *github.com* repository then push those changes to the internal
   *github.rackspace.com* repository.

These instructions use **docs-rpc** as an example repository. Update the
script and substitute your repositories as required.

Run the following commands while connected to the Rackspace network directly
or through VPN.

#. Clone the internal repository:

   .. code::

      $ git clone git@github.rackspace.com:rpc-internal/docs-rpc.git internal-docs-rpc

   .. note::

      In order to avoid confusion with the rackerlabs repository of the same
      name, the internal repository is cloned into **internal-docs-rpc**.

#. Change into the cloned **internal-docs-rpc** directory and set the upstream
   to the **rackerlabs/docs-rpc** repository:

   .. code::

      $ cd internal-docs-rpc
      $ git remote add upstream git@github.com:rackerlabs/docs-rpc.git

#. Confirm the origin and upstream remotes are correctly set:

   .. code::

      $ git remote -v

      origin	git@github.rackspace.com:rpc-internal/docs-rpc.git (fetch)
      origin	git@github.rackspace.com:rpc-internal/docs-rpc.git (push)
      upstream	git@github.com:rackerlabs/docs-rpc.git (fetch)
      upstream	git@github.com:rackerlabs/docs-rpc.git (push)

#. Set the remote for master to upstream:

   .. code::

      $ git branch --set-upstream-to upstream/master

#. Confirm you can pull from upstream and push to origin:

   .. code::

      $ git fetch upstream
      $ git merge upstream/master
      $ git push origin master

   .. note::

      If the ``git merge upstream/master`` command results in merge conflicts,
      origin and upstream are not in sync. To reset your local branch and
      origin to upstream, run the following commands:

      .. code::

         $ git remote update
         $ git reset --hard upstream/master --
         $ git push origin +master

#. Create local versions of the stable upstream branches:

   .. code::

      $ git checkout -b v10 upstream/v10
      $ git checkout -b v11 upstream/v11
      $ git checkout -b v12 upstream/v12

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

      $ bash tools/publish.sh

   Alternatively, you can run the **publish.sh** script using tox:

   .. code::

      $ tox -e publish

   .. note::

      You can also run publish.sh by sourcing it: ``. publish.sh``. If you
      do this and the script encounters an error, it exits the shell
      session entirely. Using ``bash`` or ``tox`` is preferred, as they
      return you to the current session with an error message.

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

See https://github.com/rackerlabs/docs-rpc/blob/master/tools/publish.sh for the
latest version of the publish.sh script.
