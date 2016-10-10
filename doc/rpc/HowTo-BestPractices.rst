======================
RPCDocs Best practices
======================

Please try and follow these practices when working in the docs.

General process
---------------

-  Before you leave for the day, make sure all your work has been
   committed and you have submitted pull requests.

-  First thing in the morning, update your local repo clone to ensure
   that you have the latest upstream code.

-  Do not open issues in a version/project repo. ALWAYS open issues in
   the Issues repo.

Pull requests, merges, and making changes
-----------------------------------------

-  If you have more than two or three commits in a PR, please squash the
   commits down to one or two. This makes it easier to pick the commits
   from the staging branch to publishing.

-  It's okay to self-merge a PR when kicking off a project. Once the
   project is in flight and has other writers involved, you should
   create PRs for your co-lead to review.

-  Try to be aware of when a change will affect more than one version.
   When this is the case, isolate the change to a single commit and note
   the effect in the commit message so that the change can be
   ``cherry-picked <HowTo-Cherrypick.md>`` from one version to the
   next.

   For example, if you fix a typo in ``common-front.xml`` in the ``v9``
   repo and need that change to be added to ``v10``, fix the typo, commit
   that change by itself, and include ``Affects v10`` in the commit
   message::

      Typo fixed in common-front.xml, affects v10

After the commit is merged, someone else can cherry-pick that commit into
the ``v10`` repo.

-  Rolling up multiple small commits in a single PR is fine; just be
   sure that your PR comment explains it. Multiple commits to multiple
   files run a greater risk of conflicting with other changes; try and
   confine multiple-commit PRs to one file.

-  When you make a commit that resolves an issue, include the issue
   number in the format ``rpcdocs/issues#ISSUE-NUMBER``.

   Sample commit message::

      git commit -a -m "Spelling fix for rpcdocs/issues#12"

Publishing
----------

-  Always review the docs in docs-staging or docs-internal-staging
   before publishing.

-  In fact, you should review the change in the staging area after a
   commit has been merged, to make sure that it shows up properly there.

-  Before publishing, make sure that the ``<revhistory>`` section of the
   book file is up to date with all the changes that have been made
   since the last publication of the book.
