======================
Documentation team FAQ
======================

This FAQ is intended for developers and support team members, to help them
contribute to the documentation.

As a general rule: if you have the knowledge - write it down. As the developers of
our software, that is a part of your role, and it will help us if, in doing so,
you are more directly involved with the documentation. This way, people with the
expertise and knowledge perform as much of the content cycle
as they reasonably can, and we provide key guidance, process, and assistance where needed.

The docs team provides the templates, tools, process and guidance to write content.
We also review, edit, and approve the content before publishing it.

This document addresses the following FAQs:

1. Who is the doc team and what do we do?
2. Rackspace Private Cloud documentation
	a. Where do the RPC-O docs live?
	b. What do the RPC-O docs contain?
	c. How do we do RPC-O docs?
3. OpenStack-Ansible documentation
	a. Where do the OSA docs live?
	b. What do the OSA docs contain?
	c. How do we do OSA docs?

Who is the doc team and what do we do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation is produced by the Rackspace Information Development team. For the
purposes of this FAQ, we've listed the team members with their primary
areas of expertise, but team members may do different work depending on the
overall needs of the business. Team members also contribute to OpenStack Manuals.

Senior Manager:

* Laura Clymer (IRC: onthecly)

Managers and reports:

* Lana Brindley (IRC: loquacities) - AU team and PTL for OpenStack manuals
	* Darren Chan (IRC: darrenc) - OSIC
	* Brian Moss (IRC: bmoss) - OSIC
	* Joseph Robinson (IRC: JRobinson_) - OSIC
* Karin Levenstein (IRC: klevenstein) - US team, Austin
	* Margaret Eker - Public Cloud
	* Kelly Holcomb - Sr. Technical Editor
	* Catherine Richardson - Public Cloud
	* Robb Romans (IRC: rromans) - RPC, OSA
	* Alexandra Settle (IRC: asettle) - OSIC, RPC, OSA
	* Erik Wilson (erikmwilson) - RPC
* Renee Rendon - US team, San Antonio
	* Nate Archer - How-To
	* Stephanie Fillmon - How-To
	* Kyle Laffoon - How-To
	* Cat Lookabaugh - How-To, Public Cloud

The docs team consists of Information Developers (technical writers), and
Information Architects.

* Information Developers are professional writers who produce technical documentation
  that helps people understand and use a product or service.
* Information Architects ensure the structural design of shared information
  environments (our documentation) to support usability and findability.
  The Information Architects are:
  * Darren Chan
  * Brian Moss

Rackspace Private Cloud documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where do the RPC-O docs live?
-----------------------------

The docs repo is here: https://github.com/rackerlabs/docs-rpc

The two most important folders here are `/doc` and `/internal`.

`/doc` contains the external guides that are published at https://developer.rackspace.com/docs/
(You have to scroll to the RPCO-O section about 3/4
down the page). These guides are:

* Administrator Guide (rpc-admin)
* Technical FAQ (External)
* Operations Guide
* Release Notes
* Standalone Object Storage Guide
* Upgrade Guide

`/internal` contains the internal guides that are published at
https://github.rackspace.com/rpc-internal/docs-rpc. These guides contain
information specific to Rackspace support, and are not intended to be widely
shared with the public:

* Installation Guide
* Technical FAQ (Internal version)
* Operations Guide (Internal version)

For example, the internal operations guide contains the following information,
whichis not published in the external operations guide:

* Backups
* Dashboard solutions tab

Note that while you need to be on the Rackspace network to view the published
internal guides, you can view the RST source in the github repo:
https://github.com/rackerlabs/docs-rpc/blob/master/internal/

What do the RPC-O docs contain?
-------------------------------

The **Installation Guide** is intended for Rackspace Support, and provides
the following installation information:

* The technology used by RPCO
* The environment and network architecture
* Requirements to install RPCO
* The installation process workflow, including the necessary commands to execute each step.

Note that this guide is *completely different* from the OpenStack Ansible
(OSA) installation guide, which is maintained separately.

The **internal Technical FAQ** contains Rackspace internal support questions, and should not
be distributed outside of Rackspace to any customer.

The **external Technical FAQ** is intended as a quick reference for Rackspace
customers who have questions about Rackspace Private Cloud Powered by OpenStack.

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

The **Standalone Object Storage Guide** is intended for Rackspace Support and any
other Rackers who are adding standalone OpenStack Object Storage (swift) for a
customer in a Rackspace data center or a customer data center.

The **Upgrade Guide** contains information and instructions for upgrading a
Rackspace Private Cloud environment. Note that this guide is different from
the OSA upgrade documentation, which is maintained separately.

The **Release Notes** describes new features and known and resolved issues in the
current release of Rackspace Private Cloud Powered By OpenStack (RPCO).

How do we do RPC-O docs?
------------------------

RPC-O uses github for code, as well as bug/issue management and code reviews.

To learn how to contribute to RPC-O documentation, all instructions are outlined
here: https://github.com/rackerlabs/docs-rpc/blob/master/GITHUBING.rst

AND here: https://github.com/rackerlabs/docs-rpc/blob/master/CONTRIBUTING.rst


OpenStack-Ansible (OSA) documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where do the OSA docs live?
---------------------------

The docs repo for OSA is here: https://github.com/openstack/openstack-ansible

The most important folder here for documentation is `/doc`.

`/doc` contains the external guides that are published at http://docs.openstack.org/developer/openstack-ansible/

These guides are:

* OpenStack-Ansible Installation Guide
* Upgrade Documentation
* Developer Documentation

What do the OSA docs contain?
-----------------------------

The **OpenStack-Ansible Installation Guide(()) is intended to help deployers
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
* Included scripts (several helper scripts to manage gate jobs, install base requirements,
  and update repository information)
* Playbooks
* Extending OpenStack-Ansible
* Contributor Guidelines
* Core Reviewers
* Adding new roles and services
* OpenStack-Ansible inventory

How do we do OSA docs?
----------------------

OSA is an upstream project and this means that the code lives in github,
but it uses launchpad for bug/issue logging and management, and gerrit for code reviews.

To learn how to contribute to OSA documentation, all instructions are outlined
here: http://docs.openstack.org/infra/manual/developers.html

AND here: http://docs.openstack.org/developer/openstack-ansible/developer-docs/contribute.html#documentation-and-release-note-guidelines
