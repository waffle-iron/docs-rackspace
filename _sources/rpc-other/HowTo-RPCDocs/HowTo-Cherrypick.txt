==========================================
Picking commits from staging to publishing
==========================================

Changes committed to a staging branch will not appear in publishing
until they have been cherry-picked to the publishing branch.

.. note::

   The only commits you should cherry-pick are commits in which
   the actual code change was made. Never cherry-pick a "Merge pull
   request..." commit, because that will create headaches.

#. Ensure that your local copies of the staging and publishing branches
   are up to date.

   For current versions:

   .. code::

      $ git checkout master; git fetch upstream; git merge upstream/master; git push origin master
      $ git checkout v11; git fetch upstream; git merge upstream/v11; git push origin v11

   For previous versions:

   .. code::

      $ git checkout vN-stage; git fetch upstream; git merge upstream/vN-stage; git push origin vN-stage
         $ git checkout vN; git fetch upstream; git merge upstream/vN; git push origin vN``

#. Identify the SHA of the commit that you want to pick. For this
   example, we'll use ``54008e7``, the first seven characters of the
   full SHA.

#. Check out the publishing branch:

   .. code::

      $ git checkout vN

#. Create and checkout a branch for the cherry-pick. A good standard is
   to include the SHA in the branch name, as in the following example.

   .. code::

      $ git checkout -b cherrypick-54008e7

#. Run the ``cherry-pick`` command:

   .. code::

      $ git cherry-pick 54008e7

   You may encounter merge errors. Fix the errors as needed and commit the
   fix with ``git commit -a``.

#. Push the branch containing the cherry-picked commit to the
   repository.

   .. code::

      git push origin cherrypick-54008e7

#. Go to the rpcdocs repo page on GitHub and create a pull request. On
   the **Compare changes** page, make sure you are comparing the vN
   publishing branch to your cherry-pick branch:

   .. code::

      * base fork: rpcdocs/rpcdocs
      * base: vN
      * head fork: USERNAME/rpcdocs
      * compare: cherrypick-54008e7

#. Complete the pull request as normal.
