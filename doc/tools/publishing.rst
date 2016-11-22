===============================================================
Configure development and production builds for Sphinx projects
===============================================================

This document describes how to configure development branches
to enable PR previews, and how to create and configure Strider
production builds.
<https://developer.rackspace.com/docs/>`_ for a new branch.

.. note::

   Existing branches are continuously integrated by
   `Strider <https://build.developer.rackspace.com/>`_. Merging a pull request
   to a branch that is currently being published updates
   `developer.rackspace.com <https://developer.rackspace.com/docs/>`_
   automatically.


Configure PR previews for development content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To preview development-only builds on a branch, update the ``staging.horse``
site configuration in the nexus-control content and template mapping files.

#. Add the contentIDbase for the branch content to the
   `config/content.d/staging.horse.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/content.d/staging.horse.json>`_
   configuration file. For example:

   .. code::

      "/docs/private-cloud/rpc/master/": "https://github.com/rackerlabs/docs-rpc/master/",

#. Add the template mapping to `config/routes.d/staging.horse.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/routes.d/staging.horse.json>`_
   configuration file. For example:

   .. code::

      "^/docs/private-cloud/": "developer.rackspace.com/user-guide.html",

#. After you have updated the configuration files, submit a PR to the branch in
   your project repository and wait for PR to update with the preview link to
   review your content.


Create Strider production build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can automatically generate the Strider production build job by adding the
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


Update nexus-control configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To build and deploy the content on the branch you added, update the
nexus-control configuration files for ``developer.rackspace.com`` to
define the URL for content deployment and to specify the template to apply
during the build process.

#. Add the branch to the ``developer.rackspace.com``
   `content.d/developer.rackspace.com.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/content.d/developer.rackspace.com.json>`_
   configuration file. For example:

   .. code::

      "/docs/private-cloud/rpc/v12/": "https://github.com/rackerlabs/docs-rpc/v12/",

#. Check the ``developer.rackspace.com`` `routes.d/developer.rackspace.com.json
   <https://github.com/rackerlabs/nexus-control/blob/master/config/routes.d/developer.rackspace.com.json>`_
   configuration file to confirm that a template has been listed for the
   URL pattern you specified for the branch. For example:

   .. code::

      "^/docs/private-cloud/": "user-guide.html",

#. After you have updated the configuration files, submit a PR to the branch in
   your project repository and wait for PR to update with the preview link to
   review your content.


Update docs-quickstart
~~~~~~~~~~~~~~~~~~~~~~
Add the new documents to the landing page.

#. Update `docs-quickstart
   <https://github.com/rackerlabs/docs-quickstart/blob/master/index.rst>`_ to
   add the new documents to the appropriate card on the
   `developer.rackspace.com <https://developer.rackspace.com/docs/>`_
   landing page. For example:

   .. code::

      <h5>Rackspace Private Cloud v12</h5>
      <ul>
          <li><a href="/docs/private-cloud/rpc/v12/rpc-admin/">Administrator Guide</a></li>
          <li><a href="/docs/private-cloud/rpc/v12/rpc-faq-external/">Technical FAQ</a></li>
          <li><a href="/docs/private-cloud/rpc/v12/rpc-ops/">Operations Guide</a></li>
          <li><a href="/docs/private-cloud/rpc/v12/rpc-releasenotes">Release Notes</a></li>
          <li><a href="/docs/private-cloud/rpc/v12/rpc-swift">Standalone Object Storage Guide</a></li>
          <li><a href="/docs/private-cloud/rpc/v12/rpc-upgrade">Upgrade Guide</a></li>
      </ul>


Reference
~~~~~~~~~
For more information about adding a new content repository, see the
`deconst documentation
<https://deconst.horse/writing-docs/author/#adding-a-new-content-repository>`_.
