===============================================================
Configure development and production builds for Sphinx projects
===============================================================

This document describes how to configure new documentation projects
for development and production.

Configure a project for development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Development projects are built and deployed to the
staging.deconst.horse domain instead of developer.rackspace.com.

These projects do not show up on the docs landing
page, and you have to update the project configuration file to ensure that
the content is excluded from search indexing.

If you want to move a development project to production, update the
nexus-control configuration by following the steps to configure a production
build.

Complete the following steps to build and deploy a documentation project to the
development environment.

#. :ref:`Add a new content repository to deconst <add-content-repo>`.
#. :ref:`Enable Strider build automation
   <enable-strider-build>`.
#. :ref:`Configure a project for development builds
   <configure-development-build>`.
#. :ref:`Review Strider build information <review-strider-build>`.


Configure a project for production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete the following steps to build and deploy a documentation project
to the production environment.

#. :ref:`Add a new content repository to deconst <add-content-repo>`.
#. :ref:`Enable Strider build automation <enable-strider-build>`.
#. :ref:`Configure a project for production builds
   <configure-production-build>`.
#. :ref:`Review Strider build information <review-strider-build>`.
#. :ref:`Add documentation to landing page <add-documentation-to-menu>`.

.. note::

   Existing branches are continuously integrated by
   `Strider <https://build.developer.rackspace.com/>`_. Merging a pull request
   to a branch that is currently being published updates
   `developer.rackspace.com <https://developer.rackspace.com/docs/>`_
   automatically.

.. _add-content-repo:

Add a new content repository to Deconst
---------------------------------------

You can add a new content repository branch to Deconst if your content
is written in reStructuredText (RST) or Markdown, and hosted in a git
repository on github.com.

#. Update the GitHub repository settings to enable deconst to create a Strider
   build job for your project.

   #. In the GitHub UI, click :guilabel:`Settings > Collaborators & teams`.

   #. Add the GitHub user ID `rackernexus` to the account with administrator
      privileges.

   #. In the `Deconst Slack channel
      <https://rackdx.slack.com/archives/deconst>`_,
      notify the deconst administrator (@bmoss or @meker12) to accept the
      GitHub invitation to add the `rackernexus` user to the repository.

#. Create a deconst configuration file for the project you want to build.

   #. In the content repository branch, navigate to the root folder for your
      documentation project.

   #. Add the :file:`_deconst.json`.

   #. Add the following parameters to the new file.

      - contentIDBase: A content ID to identify the content produced from
        this directory. It must be a unique ID to all content repositories
        published to Deconst.

      - githubUrl: The GitHub URL for the content repository.

      - githubBranch: Specifies the target branch for "edit on GitHub" link
        if your project is on a branch other than ``master``.

      - preferGitHubIssues: Specifies whether the documentation interface
        provides a `Submit issue` link to open a GitHub issue or an
        'Edit on Github`link to edit documentation source.

      For example:

      .. code:: ini

         {
             "contentIDBase": "https://github.com/rackerlabs/docs-rpc/v13/",
             "githubUrl": "https://github.com/rackerlabs/docs-rackspace/",
             "githubBranch": "v13",
             "meta": {
                 "preferGithubIssues": true
             }
         }

#. If the project is a development project, update the project configuration
   file to exclude the content from search indexing.

   For Sphinx projects, update the ``conf.py`` file with the following
   configuration settings:

   .. code::

      # Exclude content from elastic search index
      deconst_default_unsearchable = True

For more information on adding a new content repository, see the
`deconst documentation
<https://deconst.horse/writing-docs/author/#adding-a-new-content-repository>`_.


.. _enable-strider-build:

Enable Strider build automation
-------------------------------

You can generate the Strider production build job automatically by adding the
source repository URL to the Nexus control configuration. For each repository,
you can configure builds for one or more branches. By default, Strider builds
from the master branch. If you want to build from other branches, you must
specify the branch name.

**Prerequisite**
The source repository must have the ``rackernexus`` GitHub ID configured as
an outside collaborator with Admin access.

#. Add the repository to the `content-repositories.json
   <https://github.com/rackerlabs/nexus-control/blob/master/content-repositories.json>`_
   file. For example:

   .. code::

      { "kind": "github", "project": "rackerlabs/docs-rpc" },

#. To add builds for a specific branch, add the branch name.

   For example, the following specification shows the configuration to build
   from master, v10, v11, and v12 branches:

   .. code::

      { "kind": "github", "project": "rackerlabs/docs-rpc", "branches": [master, "v10", "v11", "v12"] },

#. Commit your changes, submit a PR and merge it.

The next time you submit a PR to the repository branch for your project,
the Strider build is created. You should see a preview link in the PR
indicating that the build ran successfully.

.. _configure-development-build:

Configure a project for development builds
------------------------------------------

To configure a development build on a branch, update the ``staging.horse``
site configuration in the nexus-control content and template mapping files.
These files are in the nexus control repository that manages the
build and deployment process for the Rackspace documentation websites.


#. Add the contentIDBase for the branch content to the
   `config/content.d/staging.horse.json <https://github.com/rackerlabs/
   nexus-control/blob/master/config/content.d/staging.horse.json>`_
   configuration file. For example:

   .. code::

      "/docs/private-cloud/rpc/master/": "https://github.com/rackerlabs/docs-rpc/<branchname>/",

#. Add the template mapping to `config/routes.d/staging.horse.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/routes.d/staging.horse.json>`_
   configuration file. For example:

   .. code::

      "^/docs/private-cloud/": "developer.rackspace.com/user-guide.html",


After you have updated the configuration files, submit a PR to the branch in
the project repository that you added. Wait for the PR to update with the
preview link to review your content. See
:ref:`Review Strider build information <review-strider-build>`.

If the preview link fails, or if the
formatting does not look right, verify that the nexus-control configuration
includes the branch in the content and template mapping files, and that
the repository has been added to the ``content.repositories`` file.

.. note::

   You can move a project from development to production by
   following the process to add a production build.

.. _configure-production-build:

Configure a project for production builds
-----------------------------------------

If you want to build and deploy a project to production, update
the nexus-control configuration files for ``developer.rackspace.com`` to
define the URL for content deployment and to specify the template to apply
during the build process.

#. Add the contentIDBase for the branch content to the
   ``developer.rackspace.com`` `content.d/developer.rackspace.com.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/content.d/developer.rackspace.com.json>`_
   configuration file. For example:

   .. code::

      "/docs/private-cloud/rpc/v13/":"https://github.com/rackerlabs/docs-rpc/v13/",

   .. note::

      The contentIDBase is defined in the `_deconst.json` file located
      in the content repository branch.

#. Check the ``developer.rackspace.com`` `routes.d/developer.rackspace.com.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/routes.d/developer.rackspace.com.json>`_
   configuration file to confirm that a template has been listed for the
   URL pattern you specified for the branch. For example:

   .. code::

      "^/docs/private-cloud/": "user-guide.html",


#. After you have updated the configuration files, submit a PR to the branch in
   your project repository and wait for PR to update with the preview link to
   review your content.

.. _review-strider-build:

Review Strider build information
--------------------------------

.. note::
    To create a Strider build for a documentation project,
    complete the nexus-control configuration updates to
    :ref`Enable Strider build automation <Enable Strider build automation>`.

Use the following information to view Strider build information:

- Review a list of Strider build jobs for documentation projects at
  https://build.developer.rackspace.com.

  If you get a 404 error, log in with your
  GitHub ID. If you still can't view the builds, open an
  `issue <https://github.com/rackerlabs/docs-rackspace/issues/new>`_ to
  request access.

- To view builds for a repository, look for the build badge at the top of the
  ``readme`` file. It indicates whether the most recent build passed or failed.
  Click the badge to open the build log.

- You can view the build log for a PR from the GitHub interface. When you
  submit the PR, a GitHub webhook triggers the Strider build process. Build
  results are added to the PR.

  - If the build fails, click the :guilabel:`Details`.

  - If the build passes, click :guilabel:`Show all checks`. Then, click
    :guilabel:`Details`.

Reference
^^^^^^^^^

For more information about deconst, see the`deconst documentation
<https://deconst.horse/>`_.


.. _add-documentation-to-menu:

Add documentation to the landing page
-------------------------------------

After you add a documentation project to production, update
the `landing page <https:\\developer.rackspace.com\docs\>`
to add the documentation title to the documentation menu.

#. Update the ``conf.py`` file in the new branch to restore search
   indexing in production. Comment out the search index setting:

   .. code::

      # Exclude content from elastic search index
      # deconst_default_unsearchable = True

#. Update `docs-quickstart
   <https://github.com/rackerlabs/docs-quickstart/blob/master/index.rst>`_ to
   add the new documents to the appropriate card on the
   `developer.rackspace.com <https://developer.rackspace.com/docs/>`_
   landing page. For example:

   .. code::

      <h5>Rackspace Private Cloud v12</h5>
      <ul>
          <li><a href="/docs/private-cloud/rpc/v13/rpc-admin/">Administrator Guide</a></li>
          <li><a href="/docs/private-cloud/rpc/v13/rpc-faq-external/">Technical FAQ</a></li>
          <li><a href="/docs/private-cloud/rpc/v13/rpc-ops/">Operations Guide</a></li>
          <li><a href="/docs/private-cloud/rpc/v13/rpc-releasenotes">Release Notes</a></li>
          <li><a href="/docs/private-cloud/rpc/v13/rpc-swift">Standalone Object Storage Guide</a></li>
          <li><a href="/docs/private-cloud/rpc/v13/rpc-upgrade">Upgrade Guide</a></li>
      </ul>

#. Commit the menu page updates and submit a PR.

#. In the GitHub view for the PR, click the preview link to
   to make sure the updates render correctly.

   If the content does not build correctly,
   :ref:`review the build log <review-strider-build>`.

#. After verifying the content, merge the PR to deploy to production.

#. Check the `landing page`_ to make sure the content is deployed correctly.

.. note::

   If the content is not deployed on the landing page, verify that the
   `rackerlabs/docs-quickstart` project is building successfully in
   https://build.developer.rackspace.com. If the build is stuck, click
   on the :guilabel:`Retest & Deploy` icon.


.. _landing page: https://developer.rackspace.com/docs
