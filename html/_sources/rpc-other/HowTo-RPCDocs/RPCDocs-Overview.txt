===========================================
RPC writing and publishing process overview
===========================================

The docs publishing process currently has a number of interlocking
stages, and the repository configuration also requires a bit of
explanation.

This document addresses only the RPC-O OpenStack process and repo
config. Other projects, such as VMWare and RPC-R, have their own
repositories and follow a similar process.

Docs are published to (scroll down to the bottom):

-  External site: http://docs.rackspace.com/
-  Pre-publication site (VPN): http://docs-internal.ipa.rackspace.com/
-  WIP staging site (VPN):
   http://docs-staging-internal.ipa.rackspace.com/

As a rule, non-urgent updates (typos, grammar fixes, fixes for
non-breaking errors) should go out with periodic V.n.n patch releases.
Urgent updates (blatant errors that make the product unusable, incorrect
file names, major bugs) should be published as soon as the correct
documentation has been confirmed.

If you run into issues, contact Steve Ortiz and Jayson DeLancey.

Repository configuration
------------------------

The documentation for the RPC OpenStack product lives in the ``rpcdocs``
repo. Documentation work for the in-development version of RPC takes
place in the ``master`` branch. When changes are ready to be published,
they are cherry-picked to the publishing branch. Earlier versions have
their own staging and publishing branches.

Pre-publication checklist
-------------------------

When changes are picked from staging to publishing, they will appear
automatically on docs.rackspace. Make sure that you have completed all
of the following tasks:

-  For new books: remove ``status="draft"`` from the ``<book>`` tag in
   the ``bk-*.xml`` file
-  For major changes (e.g. version updates): Update the ``<revhistory>``
   section in the ``bk-*.xml`` file with a description of the changes
   made
-  Release notes: ensure that the full V.n.n is in the ``<releaseinfo>``
   tag.
-  Ensure that the book builds correctly
-  Verify with the RPC Docs team that publishing the update is okay
-  Notify Steve Ortiz and Jayson DeLancey that the document will need to
   be (re-)published on docs-internal.

Making changes for the current RPC version
------------------------------------------

This is the process for making a change that will be committed to the
latest version of RPC. At the time of writing, the current version is
**v11**.

1. If you haven't already done so, create a fork of the ``rpcdocs``
   repository and clone that fork to your computer.
2. In your local working repo, create a working branch in which to make
   your changes.
3. Make the changes and push the branch to your fork.
4. Create a pull request against ``rpcdocs/master``.
5. Have someone else review the pull request and ensure that the
   document builds, then merge the pull request.
6. Cherry-pick the commit(s) in that pull request to a pull request
   against the ``v11`` branch.
7. Have someone else review the pull request with the cherry pick(s) and
   ensure that the ``v11`` document builds, then merge the pull request.

Detailed instructions for these steps are found in the following pages:

-  ``How to RPC Docs with a fork <HowTo-RPCDocs-With-A-Fork.md>``\ \_\_
-  ``Picking commits from staging to publishing <HowTo-Cherrypick.md>``\ \_\_

Making changes for a previous RPC version
-----------------------------------------

This is the process for making a change that will be committed to a
previous version of RPC.

1. Fetch the latest versions of the ``vN-stage`` and ``vN`` branches.
2. In your local working repo, check out ``vN-stage`` and then create a
   working branch in which to make your changes.
3. Make the changes and push the branch to your fork.
4. Create a pull request against ``rpcdocs/vN-stage``.
5. Have someone else review the pull request and ensure that the
   document builds, then merge the pull request.
6. Cherry-pick the commit(s) in that pull request to the ``vN`` branch.
7. Have someone else review the pull request with the cherry pick(s) and
   ensure that the ``vN`` document builds, then merge the pull request.

Detailed instructions for these steps are found in the following pages:

-  ``How to RPC Docs with a fork <HowTo-RPCDocs-With-A-Fork.md>``\ \_\_
-  ``Picking commits from staging to publishing <HowTo-Cherrypick.md>``\ \_\_
