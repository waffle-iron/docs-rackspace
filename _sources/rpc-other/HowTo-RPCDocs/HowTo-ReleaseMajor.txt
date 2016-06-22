=======================
RPCDocs: Major releases
=======================

Val Wanjura has developed
``a release process for RPC <https://one.rackspace.com/display/PrivateCloud/Release+Process>``\ \_\_.
This document refers to the stages laid out in her process and describes
the RPCDocs tasks and deliverables at each stage of the process.

For minor (V.n) and revision (V.n.n) releases, refer
``here <HowTo-ReleaseMinor.md>``\ \_\_.

Major Release stage 1: PLAN
---------------------------

-  **Develop information plan** \| This document uses inputs from
   Product, Engineering, and Marketing to define the deliverables that
   will be created for the current release. Deliverables include but are
   not limited to: installation documentation, release notes, white
   papers.

-  **Inform DocTools that a new major release is in development** \|
   Rackspace DocTools manages docs.rackspace.com. Key players: Marty
   Sixkiller (manager), Thu Doan, Steve Ortiz.

-  \*\*Create a
   ``JIRA issue <https://jira.rax.io/secure/Dashboard.jspa>``\ ** for
   the Knowledge Center\*\* The issue must include: the release date and
   the pages that will be updated. Generally this will be the
   ``Getting Started    page <http://www.rackspace.com/knowledge_center/getting-started/rackspace-private-cloud>``**
   and the
   ``FAQ <http://www.rackspace.com/knowledge_center/article/rackspace-private-cloud-faq>``\ \_\_

-  **Inform RPC Marketing of the new Install Guide URL** \| RPC
   Marketing will need this information in updating their collateral and
   in communicating changes to the Rackspace web team. \| NOTE: We may
   be able to avert this if we can agree on a universal Install Guide
   URL that never changes, regardless of release. Possibly the Knowledge
   Center Getting Started page?

Major Release stage 2: DEVELOP
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
allow us to create the final deliverables.

-  **Provide doc ID and URL information to DocTools** \| This is the
   ``canonicalUrlBase`` and ``<id>`` information included in the
   ``-bk.xml`` and ``pom.xml`` files that is required to publish the
   documentation. You must provide this information for each book.

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

Major Release stage 3: FULL QE
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

Major Release stage 4: GA PREP
------------------------------

At this stage, **no major changes to the documentation will be
accepted** unless they are critical fixes (i.e. "fix this or nothing
will work"). Any non-critical fixes will be logged as issues to be dealt
with in the next minor release or revision release.

-  **Update the Knowledge Center pages** \| On the
   ``Getting Started page <http://www.rackspace.com/knowledge_center/getting-started/rackspace-private-cloud>``\ \_\_,
   create a new draft. In the new draft, create a new section for the
   new version (use the same format as what you'll see there). Update
   the JIRA issue that you created during the PLAN phase to state that
   you've updated the page.

-  \*\*Verify all docs in
   ``docs-staging <http://docs-staging.rackspace.com/>``\ \_\_ and
   ``docs-internal-staging <http://docs-internal-staging.rackspace.com/>``\ \_\_\*\*
   \| Review everything and make sure everything looks right.

-  **Publish INTERNAL documentation** \| As soon as all docs have been
   verified (preferably within the first week of this stage),
   ``publish the INTERNAL documentation <HowTo-Publish-Docs.md>``\ \_\_
   to ``docs-internal <http://docs-internal.rackspace.com/>``\ \_\_.
   Notify OPC that the internal documentation has been published.

Major release: GA
-----------------

-  **Confirm go-live date/time with RPC Product and Marketing**

-  **Ensure that KC team is aware of go-live date/time** \| Update the
   JIRA issue, follow up with email to KC team assignee.

-  **Publish EXTERNAL documentation** \| When go-live is confirmed,
   prepare to
   ``publish the EXTERNAL documentation <HowTo-Publish-Docs.md>``\ \_\_
   to ``docs <http://docs.rackspace.com/>``\ \_\_. You should hit the
   **Deploy to Production** button at least 1 hour before the go-live
   date/time to ensure that the docs are updated when all the marketing
   emails go out.

-  **Verify all changes** \| Verify that all changes appear correctly on
   the Knowledge Center when notified by the KC team that they're live,
   and on ``docs <http://docs.rackspace.com/>``\ \_\_ and
   ``docs-internal <http://docs-internal.rackspace.com/>``\ \_\_ when
   the deployment to production is complete.
