============================
How-To: RPC Docs with a fork
============================

Before you begin, ask Lana or Karin to grant you access to the **rackerlabs**
organization on GitHub.

Working with a fork provides an extra layer of "insulation" between your
work in progress and the main repo. You can create branches in the main
repo if you really want to, but note that extra branches in the
main repo can create clutter and require regular pruning.

Forking the repository
~~~~~~~~~~~~~~~~~~~~~~

The procedure here uses https as an example. You can use ssh as well.

#. In your browser, navigate to the `docs-rpc
   <https://github.com/rackerlabs/docs-rpc>`_ repository.
#. Click on **Fork**. When prompted, select your user ID.
#. When the forking is complete, open a Terminal window and clone your fork:

   .. code::

      $ git clone https://github.com/USERNAME/docs-rpc.git

#. Switch to the new cloned folder.

   .. code::

      $ cd docs-rpc

#. Set your upstream to ``rackerlabs/docs-rpc``.

   .. code::

      $ git remote add upstream https://github.com/rackerlabs/docs-rpc.git

#. Check your git remote setup.

   .. code::

      $ git remote -v

   You should have something like this:

   .. code::

      origin https://github.com/USERAME/docs-rpc.git (push)
      origin https://github.com/USERNAME/docs-rpc.git (fetch)
      upstream   https://github.com/rackerlabs/docs-rpc.git (fetch)
      upstream   https://github.com/rackerlabs/docs-rpc.git (push)

.. note::

   You can also set remotes to point to other users' forks. This
   is useful for reviewing pull requests and collaborating on a
   change. For instance, if you want to create a remote for user ``janedoe``:

   .. code::

      $ git remote add janedoe https://github.com/janedoe/docs-rpc.git

Updating your fork
~~~~~~~~~~~~~~~~~~

#. Change into the **docs-rpc** directory.

#. If required, commit or stash changes on your working branch and checkout
   **master**:

   .. code::

      $ git stash
      $ git checkout master

#. Fetch and merge the upstream code.

   .. code::

      $ git fetch upstream
      $ git merge upstream/master

#. Push the updated upstream code to your GitHub fork.

   .. code::

      $ git push origin master

   .. note::

      If you're feeling clever, you can cut and paste those
      commands into a single line or create a bash script that runs them all:

   .. code::

      $ git fetch upstream; git merge upstream/master; git push origin master

   .. code-block:: bash

      #!/bin/bash

      git fetch upstream
      git merge upstream/master
      git push origin master

Do **not** forget the ``git push origin master`` step. Otherwise your
fork on GitHub will fall behind the upstream repo, even though your
local repo is up to date.

Editing, branching, and pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you begin, make sure you have updated your fork.

#. Create a branch off ``master`` in which to do your work. A good
   naming convention for a branch is an issue number or the topic of your
   work. For example: ``issue-14`` or ``update-links``.

   .. code::

      $ git checkout -b BRANCHNAME

#. After you've finished your work locally, commit it. If it resolves an
   issue, be sure to include the issue number in the correct format.

   .. code::

      $ git add .
      $ git commit -a

   .. code::

      Meaningful commit message on first line

      Further explanation if needed

      Fixes #14

#. Push the change to your fork on GitHub.

   .. code::

      $ git push origin BRANCHNAME

#. In your browser, go to your forked repository.

   .. code::

      $ open https://github.com/USERNAME/docs-rpc

#. At the top of the screen you'll see a status bar showing the change
   you've just committed and a green button to compare and create a pull
   request. Verify that the base branch is correct, then follow the
   prompts to create the pull request.

#. Ask someone else to review, test build, and merge your commit.

Creating a pull request against a version branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you may need to make a change on a particular version branch
that affects only that version. This is the procedure.

#. Run the following commands to checkout the required stable branch. This
   example uses **v12**.

   .. code::

      $ git checkout v12
      $ git fetch upstream
      $ git merge upstream/v12
      $ git push origin v12

#. Create a working branch off the version staging branch:

   .. code::

      $ git checkout –b BRANCHNAME

#. Make your changes and commit them.

#. Push the changes to your fork:

   .. code::

      $ git push origin BRANCHNAME

#. Go to the docs-rpc repo page on GitHub and create a pull request. On
   the **Compare changes** page, make sure you have the following
   options selected:

   .. code::

       * base fork: rackerlabs/docs-rpc
       * base: v12
       * head fork: USERNAME/docs-rpc
       * compare: BRANCHNAME

#. Complete the pull request as normal.
