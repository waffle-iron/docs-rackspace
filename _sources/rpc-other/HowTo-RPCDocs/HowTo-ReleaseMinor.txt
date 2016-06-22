====================================
RPCDocs: Minor and revision releases
====================================

Val Wanjura has developed
``a release process for RPC <https://one.rackspace.com/display/PrivateCloud/Release+Process>``\ \_\_.
This document refers to the stages laid out in her process and describes
the RPCDocs tasks and deliverables at each stage of the process.

-  **Minor releases (V.n)** only require changes to existing books and
   release notes.
-  **Revision releases (V.n.n)** only require changes to the release
   notes.

For major releases (V.0), refer ``here <HowTo-ReleaseMajor.md>``\ \_\_.

Revision releases
-----------------

Revision releases will be happening on an ongoing basis. These consist
chiefly of minor updates to the release notes. Documentation bug fixes
that have been reported in
``docs-issues <https://github.com/rpcdocs/docs-issues/issues>``\ \_\_
will also be released at this time.

In a standard 2-week sprint, Engineering will complete triaged bug
updates at the end of the first sprint week. During the second week,
docs changes based on those bugs will be made, including:

-  **Add** a link to the release notes, pointing to the latest update of
   the engineering changelog.
-  **Remove** any resolved issues from the Known Issues section of the
   release notes.
-  **Update** the release notes with any major changes (e.g. "A security
   fix has been applied; we recommend upgrading ASAP.")
-  **Solicit reviews** from engineering and from reporters of bugs.
   These reviews should be highly focused (e.g. "The following commit
   addresses bug #NN; please review the commit and let us know if the
   bug has been satisfactorily addressed.").
-  **Update** the documentation changelog.
-  **Publish** the updated release notes and any other documentation
   updates since the last revision release.

In the event of a CVE, release notes updates will be posted ASAP
according to when engineering tags the release.

Minor Release stage 1: PLAN
---------------------------

-  **Develop information plan** \| This document uses inputs from
   Product, Engineering, and Marketing to define the deliverables that
   will be created for the current release. Deliverables include but are
   not limited to: installation documentation, release notes, white
   papers.

-  **Create a
   ``JIRA issue <https://jira.rax.io/secure/Dashboard.jspa>``\ \_\_ for
   the Knowledge Center** \| This is only necessary if the
   ``FAQ <http://www.rackspace.com/knowledge_center/article/rackspace-private-cloud-faq>``\ \_\_
   is changing. The issue must include: the release date and the pages
   that will be updated.

Minor Release stage 2: DEVELOP
------------------------------

-  **Write the docs** \| Docs development occurs on an agile sprint
   basis, to match engineering feature development. In order for
   developers to be able to sign off on a work task (Trello card), the
   docs team need to have the associated documentation completed, or it
   needs to be identified specifically as non-customer facing. At the
   end of each sprint period, a draft document is made available on an
   internal server, for review by those developers who had work to be
   documented.

**Note**: Depending on feature scale and how rapidly the product is
iterating, we may end up documenting things that are incomplete or
expected to change drastically before delivery. This is OK! We always
expect that a large portion of our early work will eventually be thrown
away or completely rewritten, but they are the building blocks that
allow us to create the final deliverables. - \| **Update the release
notes** \| Create a new chapter file for the release notes and add it to
the ``-bk.xml`` file. The file name should be in the format
``section-vN-vN_n`` (for example, a v10.2 release would require
``section-v10-v10_2.xml``). Document all new features, changed features,
and resolved issues for the release here.

-  **Have informal doc reviews as needed** \| As features are
   documented, keep in communication with engineering to ensure that the
   features have been documented correctly. Documentation will be
   released to engineering, QE, and other key stakeholders for review at
   the end of every sprint cycle, but informal reviews can occur at any
   time if there is a reason to do so.

-  **Verify builds and ensure docs appear in docs-staging** \| Work with
   DocTools to ensure the docs are building correctly and that the draft
   documentation is visible in
   ``docs-staging <http://docs-staging.rackspace.com/>``\ \_\_ and
   ``docs-internal-staging <http://docs-internal-staging.rackspace.com/>``\ \_\_.

Minor Release stage 3: FULL QE
------------------------------

By this point, the draft docs should be visible in
``docs-staging <http://docs-staging.rackspace.com/>``\ \_\_ and
``docs-internal-staging <http://docs-internal-staging.rackspace.com/>``\ \_\_.
When you send documentation out for review, send links to the
documentation in the staging area.

-  **Begin DevOps, Support, and Training review** \| In the first week
   of the Full QE stage, distribute documentation to DevOps, Support,
   and Training for their review.

-  **Begin full formal review** \| In the third week of the Full QE
   stage, distribute documentation to all of OPC for review.

Minor Release stage 4: GA PREP
------------------------------

At this stage, **no major changes to the documentation will be
accepted** unless they are critical fixes (i.e. "fix this or nothing
will work"). Any non-critical fixes will be logged as issues to be dealt
with in the next revision release.

-  \*\*Verify all docs in
   ``docs-staging <http://docs-staging.rackspace.com/>``\ \_\_ and
   ``docs-internal-staging <http://docs-internal-staging.rackspace.com/>``\ \_\_\*\*
   \| Review everything and make sure everything looks right.

-  **Publish INTERNAL documentation** \| As soon as all docs have been
   verified (preferably within the first week of this stage),
   ``publish the INTERNAL documentation <HowTo-Publish-Docs.md>``\ \_\_
   to ``docs-internal <http://docs-internal.rackspace.com/>``\ \_\_.
   Notify OPC that the internal documentation has been published.

Minor release: GA
-----------------

-  **Confirm go-live date/time with RPC Product and Marketing**

-  **Publish EXTERNAL documentation** \| When go-live is confirmed,
   prepare to
   ``publish the EXTERNAL documentation <HowTo-Publish-Docs.md>``\ \_\_
   to ``docs <http://docs.rackspace.com/>``\ \_\_. You should hit the
   **Deploy to Production** button about an hour before the go-live
   date/time to ensure that the docs are updated when all the marketing
   emails go out.

-  **Verify all changes** \| Verify that all changes appear correctly on
   the Knowledge Center when notified by the KC team that they're live,
   and on ``docs <http://docs.rackspace.com/>``\ \_\_ and
   ``docs-internal <http://docs-internal.rackspace.com/>``\ \_\_ when
   the deployment to production is complete.
