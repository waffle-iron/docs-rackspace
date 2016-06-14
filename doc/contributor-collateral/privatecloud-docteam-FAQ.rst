==================================================
Documentation team FAQ for Rackspace Private Cloud
==================================================

This FAQ is intended to help RPC developers and support team members
contribute to the documentation.

As a general rule: if you have the knowledge - write it down. As the
developers of our software, you routinely communicate your deep and
expert product knowledge in the course of your work. If you write that down,
you immediately allow our team to engage with you to turn your words into
expert, professional customer documentation that we can deliver to the
Rackspace developer documentation and support sites.

With this process, people with the expertise and product knowledge contribute
to and perform as much of the content production cycle as they reasonably can,
and the Information Development team provides key guidance, process, and
assistance using our documentation platform and tools and applying our
expertise in development and information architecture.

The docs team provides the templates, tools, process and guidance to write
content. We also review, edit, and approve the content before publishing it.

.. note::

   The docs team still drives the big changes, and you should always feel free
   to   solicit docs team for help. Opening an issue in project GitHub repo is
   the quickest way to do so. The collaborative process is mainly to expedite
   the addition of smaller changes whenever possible. If you want to make large
   changes, feel free to do so and to submit the change via PR. The changes
   will be reviewed and edited as necessary.

For additional information, see the following links:


* `Who is the doc team and what do we do?`_
* `Rackspace Private Cloud documentation`_
* `OpenStack-Ansible (OSA) documentation`_
* `OpenStack manuals documentation`_


Who is the doc team and what do we do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation is produced by the Rackspace Information Development team. For
the purposes of this FAQ, we've listed the team members with their primary
areas of expertise, but team members often do different work depending on
business needs and priorities. Team members also contribute to OpenStack
Manuals.

The docs team consists of Information Developers (technical writers),
Information Architects, and Editors.

* Information Developers are professional writers who produce technical
  documentation that helps people understand and use a product or service.
* Information Architects ensure the structural design of shared information
  environments (our documentation) support usability and findability.
* Editors work closely with the Information Developers and Information
  Architects to ensure all documentation establishes a consistent tone and
  voice as described in Rackspace Style Guide.
* Senior Manager: Laura Clymer (IRC: onthecly)
* Lana Brindley (IRC: loquacities) - AU team and PTL for OpenStack manuals

  * Darren Chan (IRC: darrenc) - Information Architect, OSIC
  * Brian Moss (IRC: bmoss) - Information Architect, OSIC
  * Joseph Robinson (IRC: JRobinson\_) - OSIC

* Karin Levenstein (IRC: klevenstein) - US team, Austin

  * Margaret Eker - Public Cloud
  * Kelly Holcomb - Sr. Technical Editor
  * Catherine Richardson (IRC: cathrichardson) - Public Cloud
  * Robb Romans (IRC: rromans) - RPC, OSA
  * Alexandra Settle (IRC: asettle) - OSIC, RPC, OSA
  * Erik Wilson (IRC: erikmwilson) - RPC

* Renee Rendon - US team, San Antonio

  * Nate Archer - How-To
  * Stephanie Fillmon - How-To
  * Kyle Laffoon - How-To
  * Cat Lookabaugh - How-To, Public Cloud


Rackspace Private Cloud documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where do the RPC-O docs live?
-----------------------------

The docs repo is a private repo (message one of the docs team managers for
access), and it is located here: https://github.com/rackerlabs/docs-rpc

The two most important folders here are ``/doc`` and ``/internal``.

``/doc`` contains the following external guides that are published to the
`Rackspace developer documentation developer site
<https://developer.rackspace.com/docs/#docs-private-cloud>`_:

* Administrator Guide (rpc-admin)
* Technical FAQ (External)
* Operations Guide
* Release Notes
* Standalone Object Storage Guide
* Upgrade Guide

``/internal`` contains the internal guides that contain information
specific to Rackspace support that is not intended for public use.
For example, the internal operations guide contains the following information,
which is not published in the external operations guide:

* Backups
* Dashboard solutions tab

The following internal guides are published to the `Rackspace enterprise github
<https://pages.github.rackspace.com/rpc-internal/docs-rpc/>`_ using the Github
pages feature:

* Installation Guide
* Technical FAQ (Internal version)
* Operations Guide (Internal version)

Note that while you need to be on the Rackspace network to view the published
internal guides, you can view the RST source in the github repo:
https://github.com/rackerlabs/docs-rpc/blob/master/internal/

What do the RPC-O docs contain?
-------------------------------

The **Installation Guide** provides Rackspace support
staff with the following installation information:

* The technology used by RPCO
* The environment and network architecture
* Requirements to install RPCO
* The installation process workflow, including the necessary commands to
  execute each step.

The RPC Installation Guide is *completely different* from the OpenStack Ansible
(OSA) installation guide, which is maintained separately.

The **internal Technical FAQ** contains Rackspace internal support questions.
Do not distribute this guide outside of Rackspace to any customer.

The **external Technical FAQ** is a quick reference for Rackspace
customers who have questions about Rackspace Private Cloud Powered by
OpenStack.

The **Operations Guides** contain information and instructions for configuring
and managing a Rackspace Private Cloud environment. The external ops guide is
for customer operators, and the internal ops guide is for Rackspace Support.
These guides provide the following information for cloud operators:

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
any other Rackers who are adding standalone OpenStack Object Storage (swift)
for a customer in a Rackspace data center or a customer data center.

The **Upgrade Guide** contains information and instructions for upgrading a
Rackspace Private Cloud environment. Note that this guide is different from
the OSA upgrade documentation, which is maintained separately.

The **Release Notes** describes new features and known and resolved issues in
the current release of Rackspace Private Cloud Powered By OpenStack (RPCO).

How do we do RPC-O docs?
------------------------

RPC-O uses github for code, as well as bug/issue management and code reviews.

To learn how to contribute to RPC-O documentation, all instructions are
outlined here: https://github.com/rackerlabs/docs-rpc/blob/master/GITHUBING.rst

AND here: https://github.com/rackerlabs/docs-rpc/blob/master/CONTRIBUTING.rst


OpenStack-Ansible (OSA) documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where do the OSA docs live?
---------------------------

The docs repo for OSA is here: https://github.com/openstack/openstack-ansible

The most important folder here for documentation is ``/doc``.

``/doc`` contains the external guides that are published at
http://docs.openstack.org/developer/openstack-ansible/

These guides are:

* OpenStack-Ansible Installation Guide
* Upgrade Documentation
* Developer Documentation

What do the OSA docs contain?
-----------------------------

The **OpenStack-Ansible Installation Guide** is intended to help deployers
install OpenStack-Ansible for the first time. As such, the install guide
is somewhat opinionated, focusing on ensuring that the deployer has to make
very few decisions and implement the least amount of configuration possible
to deploy a running OpenStack environment.
Please note the OpenStack-Ansible Installation Guide is currently under
review and work will begin on a newly formatted guide before the next release.

The **Upgrade Guide** contains information and instructions for upgrading
your OSA environment per release. It specifically details manual upgrade steps,
scripts that are used in the upgrade process, and playbooks that are used in
the upgrade process.

The **Developer Documentation** provides documentation relevant to developing
OpenStack-Ansible. This includes the following:

* Quick start (all instructions relevant to your AIO)
* Included scripts (several helper scripts to manage gate jobs, install base
  requirements, and update repository information)
* Playbooks
* Extending OpenStack-Ansible
* Contributor Guidelines
* Core Reviewers
* Adding new roles and services
* OpenStack-Ansible inventory

How do we do OSA docs?
----------------------

OSA is an upstream project. The source code lives in github and is developed
and maintained using OpenStack tools and processes which include launchpad for
bug/issue logging and management and gerrit for code reviews.

Use the following resources to learn how to contribute to the OSA
documentation:

* `OpenStack Developer's Guide: Getting Started
  <http://docs.openstack.org/infra/manual/developers.html>`_
* `OpenStack Contributor Guidelines
  <http://docs.openstack.org/developer/openstack-ansible/developer-docs/contribute.html>`_


OpenStack manuals documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where do the openstack-manuals docs live?
-----------------------------------------

The docs repo for openstack-manuals is here:
https://github.com/openstack/openstack-manuals

The most important folder here for documentation is ``/doc``.

``/doc`` contains the external guides that are published at
http://docs.openstack.org/

The Release Notes:

* OpenStack Projects Release Notes
* OpenStack Documentation Release Notes

The Install Guides:

* Installation Guide for openSUSE Leap 42.1 and SUSE Linux Enterprise
  Server 12 SP1
* Installation Guide for Red Hat Enterprise Linux 7 and CentOS 7
* Installation Guide for Ubuntu 14.04 (LTS)

The Operations And Administrator Guides:

* Administrator Guide
* High Availability Guide
* Operations Guide
* Security Guide
* Virtual Machine Image Guide
* Architecture Design Guide
* Networking Guide

The Configuration Guides:

* Configuration Reference

The API Guides:

* API Complete References
* API Guide

The User Guides:

* End User Guide (includes Python SDK)
* Command-Line Interface Reference
* Open source software for application development

The Contributor Guides:

* OpenStack Documentation Contributor Guide
* OpenStack Technical Committee Governance Documents
* OpenStack Technical Committee reference documents and official resolutions
* Python Developer Documentation
* Language Bindings and Python Clients
* OpenStack Project specifications
* OpenStack Project Team Guide
* OpenStack Developer and Community Infrastructure Documentation
* OpenStack I18n Guide

What do the openstack-manuals docs contain?
-------------------------------------------

The Release Notes contain information for new features,
upgrades and deprecation notes, known issues, and bug fixes.

The Install Guides contain getting started information with the most commonly
used OpenStack services (openSUSE, SUSE Linux, RHEL 7, CentOS 7, and
Ubuntu 14.04).

The operations and administrator guides each contain different information.

* Administrator Guide
     Manage and troubleshoot an OpenStack cloud
* High Availability Guide
     Install and configure OpenStack for high availability
* Operations Guide
     Design, create, and administer a production OpenStack cloud
* Security Guide
     Guidelines and scenarios for creating more secure OpenStack clouds
* Virtual Machine Image Guide
     Obtain, create, and modify OpenStack-compatible virtual machine images
* Architecture Design Guide
     Guidelines for designing an OpenStack cloud
* Networking Guide
     Deploy and manage OpenStack Networking (neutron)

The Configuration Reference guid contains installation and configuration
options for OpenStack.

The API Guides each contain different information:

* API Complete References
     Comprehensive OpenStack API reference
* API Guide
     Introduction to using the OpenStack API

The User Guides each contain different information:

* End User Guide (includes Python SDK)
     Create and manage resources using the OpenStack dashboard, command-line
     client, and Python SDK
* Command-Line Interface Reference
     Comprehensive OpenStack command-line reference
* Open source software for application development
     Resources for application development on OpenStack clouds

The Contributor Guides each contain different information:

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

How do we do openstack-manuals docs?
------------------------------------

OpenStack manuals is an upstream project. The source code lives in github and
is developed and maintained using OpenStack tools and processes which include
launchpad for bug/issue logging and management and gerrit for code reviews.

Use the following resources to learn how to contribute to the OpenStack manuals
documentation:

* `First timers
  <http://docs.openstack.org/contributor-guide/quickstart/first-timers.html>`_
* `OpenStack Documentation Contributor Guide
  <http://docs.openstack.org/contributor-guide/index.html>`_
