**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Documentation for Rackspace products and
  services](#documentation-for-applications-and-services)
    - [Contributing to documentation](#contributing-to-documentation)
        - [High-level contribution process](#high-level-contribution-process)
        - [New product, new content](#new-product-new-content)
        - [Existing product, new feature, new
          content](#existing-product-new-feature-new-content)
        - [Existing product, fix or update](#existing-product-fix-or-update)
        - [Existing content, fixes and
          updates](#existing-content-fixes-and-updates)
    - [Continuous integration and delivery with
      Deconst](#continuous-integration-and-delivery-with-deconst)
       - [Managing GitHub source repositories for
         documentation](#managing-github-source-repositories-for-documentation)
       - [Delivering documentation to a Deconst
         site](#delivering-documentation-to-a-deconst-site)
           - [Writing content](#writing-content)
           - [Coordinating a Deconst site](#coordinating-a-deconst-site)

# Documentation for Rackspace products and services

As a developer, you create and update applications and services to provide new
and additional functionality for customers. Often that functionality needs to
be documented so that customers can use it effectively. In these cases, you
collaborate with the Information Development (Info Dev) team to create and
deliver customer-facing documentation like user and administrator guides,
expert How-To articles, and API reference documentation. The Info Dev team can
help you with tasks like the following ones:

- Determining what kind of documentation customers need
- Coordinating publishing with product release schedules
- Developing and delivering high quality documentation to the right channel at
  the right time

Like other teams in Engineering, the Info Dev team provides a framework of
common standards and practices and a shared documentation development
environment that supports a continuous integration and delivery (CI/CD)
workflow. We also provide ongoing maintenance and improvements to the tools,
processes, and systems that support this environment. Using this framework
allows you to focus on documenting your product or service for customers
without having to worry about the tools and systems for developing and
delivering the finished product.

In this collaborative process, people like you that have domain expertise and
product knowledge perform as much of the content production cycle as they
reasonably can and, in turn, the Info Dev team provides:

- Guidance in using the documentation tools and CI/CD workflow
- Templates and writing guidance
- Expertise in information development and architecture
- Reviews, editorial feedback, and publication approval

## Contributing to documentation

When you contribute to the documentation, you use the Deconst documentation
platform created by the Developer Experience team to support continuous
integration and delivery (CI/CD) of documentation. If you're a regular
contributor or if you are coordinating the documentation work for your team,
you'll find it helpful to [learn more about
Deconst](#continuous-integration-and-delivery).

How you contribute to documentation depends on what you are developing:

- **New product or service**: All the content is new.
- **New feature for an existing product and service**: New content is added to
  an existing documentation project.
- **Fixes or updates for an existing product or service**: Small changes and
  updates are made to an existing documentation project.

You can also contribute to documentation by fixing mistakes that you discover.
This section provides a high-level overview of the contribution process and
then describes how to approach each type of contribution.

**Note:** For information about how to find documentation source repositories,
see [Managing GitHub source repositories for
documentation](managing-github-source-repositories-for-documentation).

### High-level contribution process

The Info Dev team welcomes contributions to Rackspace documentation. Most
documentation source repositories (repos) include README and CONTRIBUTING files
that provide the following information:

- List of documentation deliverables and links to published content
- Explanation of the source format and tools for authoring and building the
  content
- Outline of the project organization so that contributors can determine what
  files to update and where to add new sections
- GitHub workflow instructions for submitting pull requests
- Review guidelines

When you write customer-facing documentation, follow the writing and style
guidelines specified in the
[Rackspace Documentation Guides](http://rackerlabs.github.io/docs-rackspace/style-guide/index.html).

The following process provides an overview of the general contribution workflow
for updating customer-facing documentation for Rackspace products and services.
For more detailed contribution information with Info Dev contact information
and source locations, see the following FAQs:

- [Documentation FAQ for Rackspace Public Cloud](http://rackerlabs.github.io/docs-rackspace/contributor-collateral/publiccloud-docteam-FAQ.html)
- [Documentation FAQ for Rackspace Private Cloud](http://rackerlabs.github.io/docs-rackspace/contributor-collateral/privatecloud-docteam-FAQ.html)

**General contribution workflow**

1. **Create an issue for your work.**
    - You can skip this step for trivial changes.
    - If available, reuse an existing issue on the topic.
    - If you are planning to do the work, assign yourself to the task.
    - If you need help, clearly state the work you want done and the
      context in which the work needs to be completed.

2. **Create a fork of the repo.**

    When you are ready to create or revise content, follow the contribution
    guidelines in repo to create a fork, clone it locally, and create a branch
    on the cloned repo where you can do your work.

3. **Make and commit your changes.**
   - Add your changes to the appropriate location in the project. For example,
     if you are adding a topic to an existing section, ensure that it is in the
     same folder as the other topics in that section. If you are updating an
     existing topic, be sure to add your content in the appropriate place in
     the file, adding or adjusting heading levels as necessary. If you add a
     topic, make sure that it is included in the site index or navigation.
   - Name your file meaningfully, using lowercase letters and dashes.
   - If you are contributing to a Sphinx project, use reStructuredText. If
     you are contributing to a Jekyll project, use GitHub-flavored Markdown.
   - Include diagrams where appropriate. Diagrams are required to be in the PNG
     or JPG format, but we encourage the inclusion of SVG format to make
     editing easier.
   - For new sections or topics, use other sections and topics as models to
     follow.
   - Before committing your changes, check the file syntax to
     prevent build errors. You can use a locally installed linter or follow
     the instructions to build content locally.
   - Push your changes to your fork on GitHub.

4. **Create a pull request (PR)** against the upstream repo's **master**
   branch and wait for review feedback.

### New product, new content
Whether you are working on a new cloud service or a new type of offering, such
as Carina, you first work with the Info Dev team to determine what kind of
customer-facing content is needed.

Depending on the offering, a minimum set of content is defined. For example, a
new cloud service requires introductory content, an FAQ, and basic control
panel tasks documented and delivered to the Rackspace Support site, as well as
API reference information documented and delivered to the Rackspace Developer
site.

The Info Dev team works closely with the development team to determine the
content set and the information architecture. The Info Dev team then provides
templates and guidelines to help you draft the content that is needed.

When you want to create documentation for a new product or service, open an
[issue](https://github.com/rackerlabs/docs-rackspace/issues/new) or send an
[email](mailto:group-laura-clymer@rackspace.com) with the general requirements,
context, and timeline for the project.

### Existing product, new feature, new content
When you update an existing product to add a feature or functionality that
requires customer-facing documentation, you update the existing documentation
project to add content.

For this type of change, you can scope the work yourself or work with the Info
Dev team. In either case, follow the [general contribution
workflow](#general-contribution-workflow) to submit an issue about the required
updates.

### Existing product, fix or update
Fixing or updating the code for an existing product might or might not require
updates to the customer-facing documentation. If the change affects the ways
that users interact with the product, review the existing content to determine
whether it needs to be updated. If so, follow the [general contribution
workflow](#general-contribution-workflow) to submit changes.

### Existing content, fixes and updates
As you create and work with documentation, you will find mistakes and outdated
information. You can easily fix the content yourself by following the [general
contribution workflow](#general-contribution-workflow).


## Continuous integration and delivery with Deconst

Rackspace uses the Deconst documentation platform created by the Developer
Experience team to support continuous integration and delivery (CI/CD) of
documentation. This platform enables you to treat docs like code, which means
you can use GitHub issue and pull request workflows and CI/CD processes like
the ones you use to develop, update, review, build, and deploy code.

[Deconst](https://github.com/deconst) is a continuous-delivery pipeline that
assembles documentation source projects from individual GitHub repositories to
a single site hosted on a Deconst instance. Deconst can also host multiple
domains within the site and manage content independently for each domain. The
Deconst instance currently deployed hosts a site that serves documentation to
the following domains:

Domain | Types of content | Format |
------ | ---------------- | ------ |
[developer.rackspace.com](https://developer.rackspace.com/docs/) | Private Cloud end-user documentation <br> Public Cloud API guides <br> Public Cloud SDK quickstart guides| Sphinx documentation project (reStructuredText)
[support.rackspace.com](https://support.rackspace.com/how-to/) | Articles for using and troubleshooting Rackspace services | Jekyll (Markdown) |
[getcarina.com](https://getcarina.com/docs/) | Articles for using Carina | Jekyll
[pages.github.rackspace.com](https://pages.github.rackspace.com/IX/internal-docs-landing-page/) | Private Cloud support documentation <br> Public Cloud service admin guides <br> Product services guides | Sphinx |
| staging.developer.rackspace.com |

Deconst provides several services for building and managing the content
deployed to these domains and serving it to customers. A few are described
here. For detailed information about all the features and how the Deconst CI/CD
pipeline works, see the [Architecture
section](https://deconst.horse/developing/architecture/) of the Deconst
documentation.

- A *control repository* for centralized management of site-wide concerns, such
  as setting up build jobs for documentation projects sourced from distributed
  content repositories, configuring and managing the paths where content is
  deployed on each domain, assigning templates to content.

  The control repository for the Rackspace Developer and Support How-To
  documentation is in the
  [nexus-control](https://github.com/rackerlabs/nexus-control) repository
  hosted on GitHub.

- [Preparers](https://deconst.horse/developing/architecture/#term-preparer)
  that convert content repositories in different formats to a common JSON
  format that allows content generated by different documentation engines to be
  built, integrated, and deployed using the same CI/CD process.

  Deconst provides a preparer for Sphinx documentation projects authored in
  reStructuredText (``.rst``) and another preparer for Jekyll projects authored
  in GitHub Flavored Markdown (``.md``). The preparer is run by the deconst
  CI/CD system on each commit to the repository.

  You can extend the Deconst platform to support other formats by [creating
  other preparers](https://deconst.horse/developing/preparer/).

- A *content service* that provides content storage and retrieval for content
  deployed to a Deconst instance. You can use the content service
  [API](https://github.com/deconst/content-service#api) to create, read, or
  update content manually and to run queries to get information about currently
  deployed content.

- Common, Rackspace-branded
  *[templates](https://deconst.horse/writing-docs/coordinator/templates/)* that
  determine the branding, navigation,and HTML boilerplate elements for each
  page. Templates are applied at runtime when the content is served by the
  content service API.

- Automated build and integrated testing services powered by
  [Strider](https://www.npmjs.com/package/strider), a continuous integration
  server integrated with Deconst to prepare the content and submit it to the
  content service for storage and retrieval.

- Development and Staging environments that enable collaborative review and
  early Beta releases of documentation. Staging environments are automatically
  created and linked on each pull request.

### Managing GitHub source repositories for documentation
You can find the GitHub source repository for published documentation by
clicking on the **Edit on GitHub** or **Submit an issue** link available on the
website. Because some repositories are private, you might need help getting
access or finding the repository. In that case, open an
[issue](https://github.com/rackerlabs/docs-rackspace/issues/new) to get help
from the Info Dev team.

A content repository can contain multiple documentation projects.

- Each project must be in its own folder or on its own branch.
- Source files within a folder must be written in one of the supported formats,
  for example Sphinx or Jekyll.
- Each project must have a Deconst configuration file (``deconst.json``) that
  specifies a unique content ID and other project metadata.

**Note:** The easiest path to creating a new deliverable is to copy an existing
template and update the deconst configuration file to add a unique content ID.

The content repository must also be added to the control configuration
repository for the Deconst instance to enable the Strider build job, and to
specify where the content will be deployed and what templates will be applied
when the content is rendered. Typically, a Deconst *site coordinator* manages
control configuration updates and changes.

After a content repository has been added to the control configuration, the
documentation projects in the repository will build and deploy a staging
version of the content each time someone submits a GitHub pull-request to the
repository. When the pull request is merged, the content is deployed to the
production site. If your content is in beta or early access, you can also
configure the content so that it deploys only to a development server.

### Delivering documentation to a Deconst site
The work required to deliver documentation by using Deconst depends on whether
you are authoring content or managing the site configuration settings that
enable the CI/CD workflow automation.

#### Writing content
Authors create content by writing and committing documentation source files
written in the appropriate format to a content repository. They perform tasks
like the following ones:

- Use existing Info Dev documentation project and content type templates to
  create [Markdown content for
  Jekyll](https://deconst.horse/writing-docs/author/jekyll/) or
  [resStructuredText content for
  Sphinx](https://deconst.horse/writing-docs/author/sphinx/) in new or existing
  content repositories.

- Create and maintain the Deconst configuration file in the root of the content
  directory. This file tells Deconst important details about the content within
  this directory. Place the configuration in the root project directory, with
  the ``conf.py`` or ``_config.yml`` files.

- Add new content repositories to the [automatic build
  list](https://github.com/rackerlabs/nexus-control/blob/master/content-repositories.json)
  in the Deconst control repository to configure the Strider build.

For details, see [Authoring content for
deconst](https://deconst.horse/writing-docs/author/).

#### Coordinating a Deconst site
Site coordinators assemble content from many sources into a single site by
maintaining the following configuration files in the control repository for the
Deconst instance:
- *[Content
  mapping](https://deconst.horse/writing-docs/coordinator/mapping/)files that
  specify the path where Deconst will display the content
- *[Template
  mapping](https://deconst.horse/writing-docs/coordinator/templates/#mapping-templates-to-pages)
  files that specifies which template to apply to a content set or specific
  pages within a content set when the content is served.
- *Redirect* files for maintaining link integrity when linked resources are
  moved or renamed.

Each domain has its own set of configuration files.

Coordinators also control the look and feel of each domain within the site.
They can maintain and update global assets such as such as stylesheets,
JavaScript files, or images that are referenced by the layout templates. For
details, see [Coordinating a Deconst
site](https://deconst.horse/writing-docs/coordinator/).

For detailed information about contributing to existing repositories, see the
[Contributing to the documentation](contributing-to-the-documentation).
