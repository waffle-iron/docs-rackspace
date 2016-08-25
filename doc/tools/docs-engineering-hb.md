**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Documentation for applications and services](#documentation-for-applications-and-services)
	- [Types of documentation and delivery](#types-of-documentation-and-delivery)
	- [Continuous integration and delivery](#continuous-integration-and-delivery)
	- [GitHub source repositories for documentation](#github-source-repositories-for-documentation)
	- [Delivering documentation to a Deconst site](#delivering-documentation-to-a-Deconst-site)
	   - [Writing content](#writing-content)
	   - [Managing content build and delivery](#managing-content-build-and-delivery)
	- [Contributing to documentation](#contributing-to-documentation)
		- [High-level contribution process](#high-level-contribution-process)
			- [New product, new content](#)
			- [Existing product, new feature, new content](#)
			- [Existing product, fix or update](#)
			- [Existing content, fixes and updates](#)

# Documentation for applications and services

As a developer, you create and update applications and services to provide new and additional functionality for customers. Often that functionality needs to be documented so that customers can use it effectively. In these cases, you collaborate with the Information Development (Info Dev) team to create and deliver customer-facing documentation like user and administrator guides, expert How-To articles, and API reference documentation. The Info Dev team can help you with tasks like the following ones:

- Determining what kind of documentation customers need
- Coordinating publishing with product release schedules
- Developing and delivering documentation

Like other teams in Engineering, the Info Dev team provides a framework of common standards and practices and a shared build environment that supports a continuous integration and delivery (CI/CD) workflow. Using this framework allows you to focus on documenting your product or service for customers rather than figuring out new ways to create and deliver documentation.

In this collaborative process, people like you that have domain expertise and product knowledge perform as much of the content production cycle as they reasonably can and, in turn, the Info Dev team provides:

- Guidance in using the documentation tools and CI/CD workflow
- Templates and writing guidance
- Expertise in information development and architecture
- Reviews, editorial feedback, and publication approval

## Types of documentation and delivery

Rackspace currently provides the following types of customer-facing content on the following sites:

Site | Types of content | Format |
---- | ---------------- | ------ |
[developer.rackspace.com](https://developer.rackspace.com/docs/) | Private Cloud end-user documentation <br> Public Cloud API guides <br> Public Cloud SDK quickstart guides| Sphinx documentation project (reStructuredText)
[support.rackspace.com](https://support.rackspace.com/how-to/) | Articles for using and troubleshooting Rackspace services | Jekyll (markdown) |
[getcarina.com](https://getcarina.com/docs/) | Articles for using Carina | Jekyll
[pages.github.rackspace.com](https://pages.github.rackspace.com/IX/internal-docs-landing-page/) | Private Cloud support documentation <br> Public Cloud service admin guides <br> Product services guides | Sphinx |

For more high-level information about the content that is currently provided to customers, see the following topics:

- [Documentation FAQ for Rackspace Public Cloud](http://rackerlabs.github.io/docs-rackspace/contributor-collateral/publiccloud-docteam-FAQ.html)
- [Documentation FAQ for Rackspace Private Cloud](http://rackerlabs.github.io/docs-rackspace/contributor-collateral/privatecloud-docteam-FAQ.html)

## Continuous integration and delivery

Rackspace uses the *Deconst* documentation platform created by the Developer Experience team to support continuous integration and delivery (CI/CD) of documentation. This platform allows you to treat docs like code, which means you can use GitHub issue and pull request workflows and CI/CD processes like the ones you use to develop, update, review, build, and deploy code.

[Deconst](https://github.com/deconst) is a continuous-delivery pipeline that assembles documentation source projects from individual GitHub repositories to a single site hosted on a Deconst instance. Deconst can also host multiple domains within the site and manage content independently for each domain. The Deconst instance currently deployed hosts a site that serves content for the following Rackspace documentation domains:

- [Rackspace Developer Docs](https://developer.rackspace.com/docs/)
- [Support How-To](https://support.rackspace.com/how-to/)
- [Carina Docs](https://getcarina.com/docs/)
- [Staging server](https://staging.developer.rackspace.com/) for
  pull request previews

Deconst provides the following services for building and managing the content deployed to these domains and serving it to customers:

- A control repository for centralized management of site-wide
  concerns like setting up
  build jobs for documentation projects sourced from  distributed content repositories, configuring and managing the paths where content is deployed on each domain, assigning templates to content, and managing assets such as stylesheets, JavaScript files, or images that are referenced by the layout templates.

  The control repository for the Rackspace developer and Support How-To documentation is hosted in the
  [nexus-control](https://github.com/rackerlabs/nexus-control) GitHub repository.

- [Preparers](https://deconst.horse/developing/architecture/#term-preparer)
that convert content repositories in different formats
  to a common JSON format that allows content generated by different documentation engines to be built, integrated, and deployed using the same CI/CD process. Preparers extend the native documentation engine to support additional functionality that Deconst needs to integrate the compiled content with the rest of the system.

  Deconts provides a preparer for Sphinx documentation projects authored in restructured text format](``.rst``) and another preparer for Jekyll
  projects authored in GitHub Flavored markdown (``.md``). The preparer is executed by the deconst CI/CD system on each commit to the repository.

  You can extend the Deconst platform to support other formats by [creating other preparers](https://deconst.horse/developing/preparer/).

- A content service that provides content storage and retrieval for content deployed to a Deconst instance. You can use the content service  [API](https://github.com/deconst/content-service#api) to create, read, or update content manually and to run queries to get information about currently deployed content.

- Common, Rackspace-branded  [Templates](https://deconst.horse/writing-docs/coordinator/templates/)
  that determine the branding, navigation,and HTML boilerplate used for each page. Templates are applied at runtime when the content is served by the content service API.

- Automated build services powered by
  [Strider](https://www.npmjs.com/package/strider), a continuous integration server integrated with Deconst to prepare the content and submit it to the content service for storage and retrieval.

- A presenter service uses the content service API to respond to HTTP requests from users. The presenter uses the URL requested by the user to retrieve content mapped to that path, assemble it, and return complete HTML documents to end users. For details, see [Lifecycle of an HTTP request](https://deconst.horse/developing/architecture/#lifecycle-of-an-http-request).

- An nginx server provides a reverse proxy that accepts requests from the host, terminates TLS, and delegates to the local presenter and content service.

For more detailed information about these features and how the deconst continuous-delivery pipeline works, see the [Architecture section](https://deconst.horse/developing/architecture/) of the Deconst documentation.

## GitHub source repositories for documentation
You can find the GitHub source repository for published documentation by clicking on the **Edit on GitHub** or **Submit an issue** link available on the website. Because some repositories are private, you might need help
getting access or finding the repository. In that case, open an
[issue](https://github.com/rackerlabs/docs-rackspace/issues/new) to get help from the Info Dev team.

A content repository can contain multiple documentation projects.

- Each project must be in its own folder or on its own branch.
- Source files within a folder must be written in one of the supported formats, for example Sphinx or Jekyll.
- Each project must have a deconst configuration file (``deconst.json``) that specifies a unique content ID and  other project metadata.

**Note:** The easiest path to creating a new deliverable is to copy an existing template and update the deconst configuration file to add a unique content ID.

The content repository must also be added to the control configuration repository for the Deconst instance to enable the Strider build job, and to specify where the content will deployed and what templates will be applied when the content is rendered. Typically, a Deconst site coordinator manages control configuration updates and changes.

After a content repository has been added to the control configuration, the documentation projects in the repository will build and deploy a staging version of the content each time someone submits a GitHub pull-request to the repository. When the pull request is merged, the content is deployed to the production site. If your content is in beta or early access, you can also configure the content so that it deploys only to a  to a development server only.

## Delivering documentation to a Deconst site
The work required to deliver documentation by using Deconst depends on whether you are authoring content or managing the site configuration settings that enable the CI/CD workflow automation.


### Writing content
Authors create content by writing and committing documentation source files written in the appropriate format to a content repository. They perform tasks like the following:

- Use existing Info Dev documentation project and content type templates to create [markdown content in Jekyll](https://deconst.horse/writing-docs/author/jekyll/) or [restructured text content in Sphinx](https://deconst.horse/writing-docs/author/sphinx/) in new or existing content repositories.

- Create and maintain the deconst configuration file in the root of the content directory. This file tells Deconst important details about the content within this directory. Place the configuration in the same directory as your ``conf.py`` or ``_config.yml`` files.

- Add new content repositories to the [automatic build list](https://github.com/rackerlabs/nexus-control/blob/master/content-repositories.json) in the Deconst control repository to configure the Strider build.

For details, see [Authoring content for deconst](https://deconst.horse/writing-docs/author/).

#### Managing content build and delivery
Site coordinators assemble content from many sources into a single site by configuring the following items in the control repository for the Deconst instance:
- A [content mapping](https://deconst.horse/writing-docs/coordinator/mapping/) that specifies the path where Deconst will display the content
- A [template mapping](https://deconst.horse/writing-docs/coordinator/templates/#mapping-templates-to-pages) that specifies which template to apply to a content set or specific pages within a content set when the content is served.

Coordinators also control the look and feel of each domain within the site. They can maintain and update global assets such as such as stylesheets, JavaScript files, or images that are referenced by the layout templates.

For details, see [Coordinating a Deconst site](https://deconst.horse/writing-docs/coordinator/).

For detailed information about contributing to existing repositories, see the [Contributing to the documentation](contributing-to-the-documentation).


For detailed information about contributing to existing repositories, see the [Contributing to the documentation](contributing-to-the-documentation).

## Contributing to documentation

How you contribute to documentation depends on what you are developing:

- **New product or service**: All the content is new.
- **New feature for an existing product and service**: New content is added to an existing documentation project.
- **Fixes or updates for an existing product or service**: Small changes and updates are made to an existing documentation project.

You can also contribute to documentation by fixing mistakes that you discover. This section provides a high-level overview of the contribution process and then describes how to approach each type of contribution.

### High-level contribution process

The Info Dev team welcomes contributions to Rackspace documentation. Most documentation source repositories (repos) include README and CONTRIBUTING files that provide the following information:

- List of documentation deliverables and links to published content
- Explanation of the source format and tools for authoring and building the content
- Outline of the project organization so that contributors can determine what
  files to update and where to add new sections
- GitHub workflow instructions for submitting pull requests
- Review guidelines

When you write customer-facing documentation, follow the writing and style
guidelines specified in the
[Rackspace Documentation Guides](http://rackerlabs.github.io/docs-rackspace/style-guide/index.html).

**General contribution workflow**

The following process provides an overview of the general contribution
model for updating customer-facing documentation for Rackspace products and
services. For more detailed contribution information, see the CONTRIBUTING guidelines in the documentation source repo.

1. **Create an issue for your work.**
    - You can skip this step for trivial changes.
    - If available, reuse an existing issue on the topic.
    - If you are planning to do the work, assign yourself to the task.
    - If you need help, clearly state the work you want done and the
      context in which the work needs to be completed.

2. **Create a fork of the repo.**

    When you are ready to make create or revise content, follow the contribution guidelines in the repo to create a fork of the repo, clone it locally, and create a branch on the cloned repo where you can do your work.

3. **Make and commit your changes.**
   - Add your changes to the appropriate location in the project.
     For example, if you are adding a topic to an existing section, ensure that it is in the same folder as the other topics in that section. If you are updating an existing topic, be sure to add your content in the appropriate place in the file, adding or adjusting heading levels as necessary.
   - Name your file meaningfully, using lowercase letters and dashes.
   - If you are contributing to a Sphinx project, use reStructuredText. If
     you are contributing to a Jekyll project, use GitHub-flavored Markdown.
   - Include diagrams where appropriate. Diagrams are required to be in the
     PNG or JPG format, but we encourage the inclusion of SVG format to make editing easier.
   - For new sections or topics, use other sections and topics as models to
     follow.
   - Before committing your changes, check the file syntax to
     prevent build errors. You can use a locally installed linter or follow
     the instructions to build content locally.
   - Push your changes to your fork on GitHub.

4. **Create a pull request (PR)** against the upstream repo's **master**
   branch and wait for review feedback.

#### New product, new content
Whether you are working on a new cloud service or a new type of offering, such as Carina, you first work with the Info Dev team to determine what kind of customer-facing content is needed.

Depending on the offering, a minimum set of content is defined. For example, a new cloud service requires introductory content, an FAQ, and basic control panel tasks documented and delivered to the Rackspace Support site, as well as API reference information documented and delivered to the Rackspace Developer site.

The Info Dev team works closely with the development team to determine the content set and the information architecture. The Info Dev team then provides templates and guidelines to help you draft the content that is needed.

When you want to create documentation for a new product or service, open an [issue](https://github.com/rackerlabs/docs-rackspace/issues/new) or send an
[email](mailto:group-laura-clymer@rackspace.com) with the general requirements, context, and timeline for the project.

#### Existing product, new feature, new content
When you update an existing product to add a feature or functionality that
requires customer-facing documentation, you update the existing documentation project to add content.

For this type of change, you can scope the work yourself or work with the Info Dev team. In either case, follow the [general contribution workflow](#general-contribution-workflow) to submit an issue about the required updates.

#### Existing product, fix or update
Fixing or updating the code for an existing product might or might not require updates to the customer-facing documentation. If the change affects the ways that users interact with the product, review the existing content to determine whether it needs to be updated. If so, follow the [general contribution workflow](#general-contribution-workflow) to submit changes.

#### Existing content, fixes and updates
As you create and work with documentation, you will find mistakes and outdated information. You can easily fix the content yourself by following the [general contribution workflow](#general-contribution-workflow).
