==============================
How to do RPC Docs with a fork
==============================

Before you begin, ask Lana or Karin to grant you access to the rpcdocs
organization on GitHub.

Working with a fork provides an extra layer of "insulation" between your
work in progress and the main repo. You can create branches in the main
repo if you really want to, but note that many extra branches in the
main repo can create clutter, in the form of branches that go stale and
need to be pruned.

Forking the repository
~~~~~~~~~~~~~~~~~~~~~~

The procedure here uses https as an example. You can use ssh as well.

#. In your browser, navigate to the `rpcdocs repository
   <https://github.com/rpcdocs/rpcdocs>`_.
#. Click on **Fork**. When prompted, select your user ID.
#. When the forking is complete, open a Terminal window. Create an
   ``rpcdocs`` folder and switch to that folder.

   .. code::

      $ mkdir rpcdocs
      $ cd rpcdocs

3. Clone your fork.

   .. code::

      $ git clone https://github.com/USERNAME/rpcdocs.git

#. Switch to the new cloned folder.

   .. code::

      $ cd rpcdocs

#. Set your upstream to ``rpcdocs/rpcdocs``.

   .. code::

      $ git remote add upstream https://github.com/rpcdocs/rpcdocs.git

#. Re-point your origin back to your fork.

   .. code::

      $ git remote set-url origin https://github.com/USERNAME/rpcdocs.git

Repeat these steps whenever you need access to one of the ``rpcdocs``
repositories.

.. note::

   You can also set remotes to point to other users' forks. This
   is useful for more easily reviewing pull requests or collaborating on a
   change. For instance, if you want to create a remote for user ``janedoe``:

   .. code::

      $ git remote add janedoe https://github.com/janedoe/rpcdocs.git

Making sure you have the latest upstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Navigate to the repo you want to update.

   .. code::

      $ cd REPONAME

#. Fetch and merge the upstream code.

   .. code::

      $ git checkout master
      $ git fetch upstream
      $ git merge upstream/master

#. Push the updated upstream code to your GitHub fork.

   .. code::

      $ git push origin master

   .. note::

      If you're feeling clever, you can cut and paste all those
      commands into a single line:

   .. code::

      $ git checkout master; git fetch upstream; git merge upstream/master; git push origin master

Do **not** forget the ``git push origin master`` step. Otherwise your
fork on GitHub will fall behind the upstream repo, even though your
local repo is up to date.

Editing, branching, and pull requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you begin, make sure you've grabbed the latest upstream code.

#. Create a branch off ``master`` in which to do your work. A good
   naming convention for a branch is your initials, something indicating
   what you're fixing, and the date. For example: ``kl-configure-0930``

   .. code::

      $ git checkout -b BRANCHNAME

#. After you've finished your work locally, commit it. If it resolves an
   issue, be sure to include the issue number in the correct format.

   .. code::

      $ git commit

   .. code::

      Meaningful commit message on first line

      Further explanation if needed

      Fixes rpcdocs/issues#NNN

#. Push the change to your fork on GitHub.

   .. code::

      $ git push origin BRANCHNAME

#. In your browser, go to your forked repository.

   .. code::

      $ open https://github.com/USERNAME/rpcdocs

#. At the top of the screen you'll see a status bar showing the change
   you've just committed and a green button to compare and create a pull
   request. Verify that the base branch is correct, then follow the
   prompts to create the pull request.

#. Ask someone else to review, test build, and merge your commit.

Creating a pull request against a version branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you may need to make a change on a particular version branch
that affects only that version. This is the procedure.

#. Check your git remote setup.

   .. code::

      $ git remote -v

   You should have something like this:

   .. code::

      origin https://github.com/USERAME/rpcdocs.git (push)
      origin https://github.com/USERNAME/rpcdocs.git (fetch)
      upstream   https://github.com/rpcdocs/rpcdocs.git (fetch)
      upstream   https://github.com/rpcdocs/rpcdocs.git (push)

#. Run the following command to grab the latest version staging branch
   (substitute the appropriate number for vN) and update it on your
   rpcdocs fork:

   .. code::

      $ git checkout vN-stage; git fetch upstream; git merge upstream/vN-stage; git push origin vN-stage

#. Create a working branch off the version staging branch:

   .. code::

      $ git checkout –b BRANCHNAME

#. Make your changes and commit them.

#. Push the changes to your fork:

   .. code::

      $ git push origin BRANCHNAME

#. Go to the rpcdocs repo page on GitHub and create a pull request. On
   the **Compare changes** page, make sure you have the following
   options selected:

   .. code::

       * base fork: rpcdocs/rpcdocs
       * base: vN-stage
       * head fork: USERNAME/rpcdocs
       * compare: BRANCHNAME

#. Complete the pull request as normal.
