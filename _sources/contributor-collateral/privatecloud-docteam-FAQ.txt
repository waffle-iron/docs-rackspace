==================================================
Documentation team FAQ for Rackspace Private Cloud
==================================================

This FAQ is intended to help Rackspace Private Cloud (RPC) developers and
support team members contribute to the documentation.

As developers and support team members, you routinely communicate your expert
product knowledge in the course of your work. When you write down that
knowledge, you enable the Information Development (doc) team to work with you
to turn your words into expert, professional customer documentation that we can
deliver to the Rackspace documentation and support sites.

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
quite sure what to do, you can ask for help by opening `an issue in the
project's GitHub repo <https://github.com/rackerlabs/docs-rpc/issues>`_.
Alternatively, you can make and submit large changes via a PR. The doc team
will review and edit the changes as necessary.

For additional information, see the following sections:


* `Who is the doc team and what do we do?`_
* `Rackspace Private Cloud documentation`_
* `OpenStack-Ansible (OSA) documentation`_
* `OpenStack documentation`_
* `Private Cloud How-To and Control Panel articles`_

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

Rackspace Private Cloud documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section answers questions about the Rackspace Private Cloud Powered By
OpenStack (RPCO) documentation.

Where do the RPCO docs live?
----------------------------

The RPCO docs repo is a private repo, and it is located at
https://github.com/rackerlabs/docs-rpc. Send a message to one of the docs team
managers for access.

The two most important folders in the repo are ``/doc`` and ``/internal``.

The ``/doc`` folder contains the following external guides that are published
to the `Rackspace Developer Docs site
<https://developer.rackspace.com/docs/#docs-private-cloud>`_:

* Administrator Guide (rpc-admin)
* Technical FAQ (external)
* Operations Guide
* Release Notes
* Standalone Object Storage Guide (swift)
* Upgrade Guide

The ``/internal`` folder contains the internal guides that contain information
specific to Rackspace support that is not intended for public use. For example,
the internal operations guide contains the following information, which is not
published in the external operations guide:

* Backups
* Dashboard solutions tab

The following internal guides are published to the `Rackspace Developer Portal
<https://pages.github.rackspace.com/rpc-internal/docs-rpc/>`_ using the GitHub
pages feature:

* Installation Guide
* Technical FAQ (internal)
* Operations Guide (internal)

.. note::

   Although you need to be on the Rackspace network to view the published
   internal guides, you do not have to be to view the RST source in the GitHub
   repo.

What do the RPCO docs contain?
------------------------------

The **Installation Guide** provides Rackspace support staff with the following
installation information:

* Technology used by RPCO
* Environment and network architecture
* Requirements to install RPCO
* Installation process workflow, including the necessary commands to execute
  each step.

The RPCO Installation Guide is *completely different* from the
OpenStack-Ansible (OSA) installation guide, which is maintained separately.

The **internal Technical FAQ** contains Rackspace internal support questions.
Do not distribute this guide outside of Rackspace to any customer.

The **external Technical FAQ** is a quick reference for Rackspace customers who
have questions about RPCO.

The **Operations Guides** contain information and instructions for configuring
and managing a Rackspace Private Cloud environment. The external guide is for
customer operators, and the internal guide is for Rackspace Support. These
guides describe the following tasks for cloud operators:

* Manage a deployed cloud environment
* Manage containers
* Monitor the cloud environment
* Conduct log inquiries
* Manage Galera clusters
* Diagnose and fix issues with the cloud environment

The **Administrator Guide** describes how to create and manage projects, users,
quotas, and security in a Rackspace Private Cloud environment. This guide is
intended for customer system administrators who perform the following tasks:

* Create and configure projects
* Create and manage users
* Manage project quotas
* Add and manage project security group rules
* Diagnose and fix Identity service issues

The **Standalone Object Storage Guide** is intended for Rackspace Support and
any other Rackers who are adding stand-alone OpenStack Object Storage (swift)
for a customer in a Rackspace data center or a customer data center.

The **Upgrade Guide** contains information and instructions for upgrading a
Rackspace Private Cloud environment. Note that this guide is different from the
OSA upgrade documentation, which is maintained separately.

The **Release Notes** describes new features and known and resolved issues in
the current release of RPCO.

How do we contribute to RPCO docs?
----------------------------------

RPCO uses GitHub for code, bug and issue management, and code reviews.

To learn how to contribute to RPCO documentation, see the following
instructions:

* `GitHub workflow
  <https://github.com/rackerlabs/docs-rpc/blob/master/GITHUBING.rst>`_
* `Contributor guidelines
  <https://github.com/rackerlabs/docs-rpc/blob/master/CONTRIBUTING.rst>`_


OpenStack-Ansible (OSA) documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section answers questions about the OpenStack-Ansible (OSA) documentation.

Where do the OSA docs live?
---------------------------

The OSA docs repo is at https://github.com/openstack/openstack-ansible.

The most important folder is ``/doc``. This folder contains the following
external guides, which are published to the `OpenStack-Ansible Documentation
site <http://docs.openstack.org/developer/openstack-ansible/>`_:

* OpenStack-Ansible Installation Guide
* Upgrade Documentation
* Developer Documentation

What do the OSA docs contain?
-----------------------------

The **OpenStack-Ansible Installation Guide** is intended to help deployers
install OpenStack-Ansible for the first time. As such, the guide is somewhat
opinionated, focusing on ensuring that the deployer has to make very few
decisions and implement the least amount of configuration possible to deploy a
running OpenStack environment.

.. note::

   As of June 2016, the OpenStack-Ansible Installation Guide is under review
   and will be newly formatted for the next release.

The **Upgrade Guide** contains information and instructions for upgrading your
OSA environment per release. It specifically details manual upgrade steps,
scripts that are used in the upgrade process, and playbooks that are used in
the upgrade process.

The **Developer Documentation** provides documentation relevant to developing
OpenStack-Ansible:

* Quick start (all instructions relevant to your AIO build)
* Included scripts (several helper scripts to manage gate jobs, install base
  requirements, and update repository information)
* Playbooks
* Extending OpenStack-Ansible
* Contributor Guidelines
* Core Reviewers
* Adding new roles and services
* OpenStack-Ansible inventory

How do we contribute to OSA docs?
---------------------------------

OSA is an upstream project. The source code lives in GitHub, and it is
developed and maintained by using OpenStack tools and processes, which include
Launchpad for bug and issue logging and management, and Gerrit for code
reviews.

Use the following resources to learn how to contribute to the OSA
documentation:

* `OpenStack Developer's Guide: Getting Started
  <http://docs.openstack.org/infra/manual/developers.html>`_
* `OpenStack Contributor Guidelines
  <http://docs.openstack.org/developer/openstack-ansible/developer-docs/contribute.html>`_


OpenStack documentation
~~~~~~~~~~~~~~~~~~~~~~~

This section answers questions about the OpenStack manuals documentation.

Where do the OpenStack manuals docs live?
-----------------------------------------

The OpenStack manuals docs repo is at
https://github.com/openstack/openstack-manuals.

The most important folder is ``/doc``. This folder contains the following
external guides, which are published at http://docs.openstack.org/.

Release Notes:

* OpenStack Projects Release Notes
* OpenStack Documentation Release Notes

Install Guides:

* Installation Guide for openSUSE Leap 42.1 and SUSE Linux Enterprise Server 12
  SP1
* Installation Guide for Red Hat Enterprise Linux 7 and CentOS 7
* Installation Guide for Ubuntu 14.04 (LTS)

Operations And Administration Guides:

* Administrator Guide
* High Availability Guide
* Operations Guide
* Security Guide
* Virtual Machine Image Guide
* Architecture Design Guide
* Networking Guide

Configuration Guides:

* Configuration Reference

API Guides:

* API Complete References
* API Guide

User Guides:

* End User Guide (includes Python SDK)
* Command-Line Interface Reference
* Open source software for application development

Contributor Guides:

* OpenStack Documentation Contributor Guide
* OpenStack Technical Committee Governance Documents
* Python Developer Documentation
* Language Bindings and Python Clients
* OpenStack Project specifications
* OpenStack Project Team Guide
* OpenStack Developer and Community Infrastructure Documentation
* OpenStack I18n Guide

What do the OpenStack manuals docs contain?
-------------------------------------------

The **Release Notes** contain information about new features, upgrades,
deprecations, known issues, and bug fixes.

The **Install Guides** contain information about getting started with the most
commonly used OpenStack services on openSUSE, SUSE Linux, Red Hat Enterprise
Linux, CentOS, and Ubuntu.

The **Operations and Administration Guides** contain the following information:

* Administrator Guide
    Manage and troubleshoot an OpenStack cloud
* High Availability Guide
    Install and configure OpenStack for high availability
* Operations Guide
    Design, create, and administer a production OpenStack cloud
* Security Guide
    Guidelines and scenarios for creating more secure OpenStack clouds
* Virtual Machine Image Guide
    Obtain, create, and modify OpenStack compatible virtual machine images
* Architecture Design Guide
    Guidelines for designing an OpenStack cloud
* Networking Guide
    Deploy and manage OpenStack Networking (neutron)

The **Configuration Reference** contains installation and configuration options
for OpenStack.

The **API Guides** contain the following information:

* API Complete References
    Comprehensive OpenStack API reference
* API Guide
    Introduction to using the OpenStack API

The **User Guides** contain the following information:

* End User Guide (includes Python SDK)
    Create and manage resources using the OpenStack dashboard, command-line
    client, and Python SDK
* Command-Line Interface Reference
    Comprehensive OpenStack command-line reference
* Open source software for application development
    Resources for application development on OpenStack clouds

The **Contributor Guides** contain the following information:

* OpenStack Documentation Contributor Guide
    Documentation workflow and conventions
* OpenStack Technical Committee Governance Documents
    OpenStack Technical Committee reference documents and official resolutions
* Python Developer Documentation
    Documentation for OpenStack developers
* Language Bindings and Python Clients
    Documentation for the OpenStack Python bindings
* OpenStack Project specifications
    Specifications for future project features
* OpenStack Project Team Guide
    Guide to the OpenStack project and community
* OpenStack Developer and Community Infrastructure Documentation
    Development and infrastructure documentation
* OpenStack I18n Guide
    Internationalization workflow and conventions

How do we contribute to OpenStack manuals?
------------------------------------------

OpenStack manuals is an upstream project. The source code lives in GitHub, and
it is developed and maintained by using OpenStack tools and processes, which
include Launchpad for bug and issue logging and management, and Gerrit for code
reviews.

Use the following resources to learn how to contribute to the OpenStack manuals
documentation:

* `First timers
  <http://docs.openstack.org/contributor-guide/quickstart/first-timers.html>`_
* `OpenStack Documentation Contributor Guide
  <http://docs.openstack.org/contributor-guide/index.html>`_

Private Cloud How-To and Control Panel articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section answers questions about the How-To articles.

Where do the How-To articles live?
----------------------------------

The How-To article repo is at
`<https://github.com/rackerlabs/rackspace-how-to>`_.

The most important folder is ``/content``. This folder contains the
subdirectories, with article source files, for each of the Private
and Public Cloud products and services.

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
