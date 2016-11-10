======================================================================
Documentation team FAQ for Rackspace Public Cloud and Managed services
======================================================================

This FAQ is intended to help Rackspace Public and Managed Cloud developers
and support team members contribute to the documentation.

As developers and support team members, you routinely communicate your expert
product knowledge in the course of your work. When you write down that
knowledge, you enable the Information Design and Development (doc) team to
work with you to turn your words into expert, professional customer
documentation that we can deliver to the Rackspace documentation and support
sites.

In this process, the people with the expertise and product knowledge perform as
much of the content production cycle as they reasonably can and, in turn, the
doc team provides:

* Guidance in using our documentation platform and tools
* Templates and writing guidance
* Expertise in information development and architecture
* Reviews, editorial feedback, and publication approval

This collaborative process most often expedites the addition of smaller changes
to content. The doc team still drives the overall documentation strategy and
large changes to the content sets. If you want to make large changes but aren't
quite sure what to do, you can ask for help by opening an issue in the
project's GitHub repo. Alternatively, you can make and submit large changes via
a PR. The doc team will review and edit the changes as necessary.

For additional information, see the following sections:


* `Who is the doc team and what do we do?`_
* `API documentation`_
* `How-To and Control Panel articles`_

Who is the doc team and what do we do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation is produced by the Rackspace Information Development team. This
section lists the team members with their primary areas of expertise, but team
members often do different work depending on business needs and priorities.
Team members also contribute to OpenStack manuals.

The team consists of Information Developers (technical writers), Information
Architects, and Editors.

* Information Developers are professional writers who produce technical
  documentation that helps people understand and use a product or service.
* Information Architects ensure that the structural design of shared
  information environments (our documentation) supports usability and
  findability.
* Editors work closely with the Information Developers and Information
  Architects to ensure that all documentation uses a consistent tone and
  follows standards as described in the Rackspace style guide.

Following are the members of the team:

* **Senior Manager: Laura Clymer (IRC: onthecly)**
* Lana Brindley (IRC: loquacities) - Manager of AU team and PTL for OpenStack
  manuals

  * Darren Chan (IRC: darrenc) - Information Architect, OSIC
  * Brian Moss (IRC: bmoss) - Information Architect, OSIC
  * Joseph Robinson (IRC: JRobinson\_) - Information Developer, OSIC

* Karin Levenstein (IRC: klevenstein) - Manager of Austin, US team

  * Margaret Eker - Senior Information Developer, RPC, Public Cloud
  * Kelly Holcomb - Editor
  * Catherine Richardson (IRC: cathrichardson) - Senior Information Developer,
    RPC and Public Cloud
  * Robb Romans (IRC: rromans) - Senior Information Developer, RPC and OSA
  * Alexandra Settle (IRC: asettle) - Information Developer, OSIC, RPC and
    OSA
  * Erik Wilson (IRC: erikmwilson) - Senior Information Developer, RPC

* Renee Rendon - Manager of San Antonio, US team

  * Nate Archer - Information Developer, How-To
  * Stephanie Fillmon - Information Developer, How-To
  * Kyle Laffoon - Information Developer, How-To
  * Cat Lookabaugh (IRC: catlook) - Senior Information Developer, How-To,
    Public Cloud


API documentation
~~~~~~~~~~~~~~~~~

This section answers questions about the Rackspace API
documentation.

Where do the API docs live?
---------------------------

The API docs are located in the following https://github.com/rackerlabs repos:

-  `Cloud Backup <https://github.com/rackerlabs/docs-cloud-backup>`_
-  `Cloud Big Data <https://github.com/rackerlabs/docs-cloud-big-data>`_
-  `Cloud Block Storage
   <https://github.com/rackerlabs/docs-cloud-block-storage>`_
-  `Cloud Databases <https://github.com/rackerlabs/docs-cloud-databases>`_
-  `Cloud DNS <https://github.com/rackerlabs/docs-cloud-dns>`_
-  `Cloud Files <https://github.com/rackerlabs/docs-cloud-files>`_
-  `Cloud Identity <https://github.com/rackerlabs/docs-cloud-identity>`_
-  `Cloud Images <https://github.com/rackerlabs/docs-cloud-images>`_
-  `Cloud Keep <https://github.com/rackerlabs/docs-barbican>`_
-  `Cloud Load Balancers
   <https://github.com/rackerlabs/docs-cloud-load-balancers>`_
-  `Cloud Orchestration
   <https://github.com/rackerlabs/docs-cloud-orchestration>`_
-  `Cloud Networks <https://github.com/rackerlabs/docs-cloud-networks>`_
-  `Cloud Queues <https://github.com/rackerlabs/docs-cloud-queues>`_
-  `Cloud Servers <https://github.com/rackerlabs/docs-cloud-servers>`_
-  `Rackspace Autoscale
   <https://github.com/rackerlabs/otter/tree/master/api-docs/rst/dev-guide>`_
-  `Rackspace CDN <https://github.com/rackerlabs/docs-cloud-cdn>`_
-  `Rackspace Metrics <https://github.com/rackerlabs/docs-cloud-metrics>`_
-  `Rackspace Monitoring
   <https://github.com/rackerlabs/docs-cloud-monitoring>`_

The most important folder in these repos is ``/api-docs``. If the product has
more than one supported version, separate documentation is maintained in
version-specific directories under ``/api-docs``.

The ``/api-docs`` folder (or the version-specific subfolder) contains the
following external guides that are published to the `Rackspace Developer Docs
site <https://developer.rackspace.com/docs/>`_:

* Getting Started Guide
* Developer Guide
* API Reference
* Release Notes

What do the API docs contain?
-----------------------------

The **Getting Started Guide** provides the following information:

* Prerequisites for using the product API
* Installation instructions for cURL and clients
* Information about sending API requests
* Instructions for API authentication
* Use cases for basic product operations, including the necessary commands to
  execute each step

The **Developer Guide** contains information to assist software developers who
want to develop applications by using the REST API for the product, including
the following information:

* Explanation of product concepts
* General API information, including:

  - Service access endpoints
  - Request and response types
  - Limits and quotas
  - Role based access control

The **API Reference** provides a list of all supported API operations,
including:

* The operation URI
* Additional information regarding the operation and its use
* Lists of URI, query, request body, and response body parameters
* Examples of request and response bodies, if any

The **Release Notes** describes new features and known and resolved issues in
the current release of the product or service.

How do we contribute to API docs?
---------------------------------

Rackspace Cloud services documentation uses GitHub for code, bug and issue
management, and code reviews.

To learn how to contribute to API documentation, see the following
instructions:

* GitHub workflow found in ``GITHUBING.rst`` in the root directory of the
  product repo
* Contributor guidelines found in ``CONTRIBUTING.rst`` in the root director of
  the product repo

For example, see the following documents in the Cloud Servers repo:

* `GitHub workflow
  <https://github.com/rackerlabs/docs-cloud-servers/blob/master/GITHUBING.md>`_
* `Contributor guidelines
  <https://github.com/rackerlabs/docs-cloud-servers/blob/master/CONTRIBUTING.md>`_

How-To and Control Panel articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section answers questions about the How-To articles.

Where do the How-To articles live?
----------------------------------

The How-To article repo is at
`<https://github.com/rackerlabs/rackspace-how-to>`_.

The most important folder is ``/content``. This folder contains the
subdirectories, with article source files, for each of the Public Cloud
products and services.

What do the How-To articles contain?
------------------------------------

How-To articles provide users and system administrators with tactical,
troubleshooting, and FAQ information for Rackspace products and services.
How-To articles also provide instructions to set up and maintain Rackspace
products from the Rackspace Cloud Control Panel.

How do we contribute to How-To articles?
----------------------------------------

The How-To uses GitHub for code, bug and issue management, and code reviews.

To learn how to contribute to How-To articles, see `Contributing to the
Rackspace How-To content repository
<https://github.com/rackerlabs/rackspace-how-to/blob/master/CONTRIBUTING.md>`_.
