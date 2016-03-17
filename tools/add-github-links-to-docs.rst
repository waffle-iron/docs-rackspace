
Adding support for contributions
---------------------------------

Add GitHub links to the documentation navigation menu to make it easy for 
readers to propose changes or submit feedback directly to the GitHub repository 
where you manage the project. 

.. note::
     These instructions apply to Sphinx documentation projects that are deployed 
     by the Nexus publishing platform. 
     

You can add either of the following GitHub links: 

- An **Edit on GitHub** link opens an editable copy of the source file for the 
  current topic so that people can update the source and submit 
  a GitHub pull request for review. 
  
  Add support for *Edit on GitHub* link if your documentation is in a public repository 
  and you want active, direct contributions. This type of link works best for projects 
  that use a topic-based content architecture where each major topic is displayed on its 
  own page.
  
- The **Submit an Issue** link opens a GitHub issue page so that people can report a bug 
  or provide feedback about the documentation. 
  
  Add support for *Submit an issue* links if your project is in a private repository,  
  or if you prefer people to report issues or problems rather than updating content  
  directly.  This link type works best for projects that display a large collection of 
  topics in a single view. In these projects, the *Edit on GitHub* link is less useful 
  because it opens the source file for the first topic, which can make it difficult 
  for contributors to find the content they want to change. 
  
  
Configuring GitHub links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
 You configure GitHub links for a documentation project by updating the ``_deconst.json`` 
 file in the same directory as your documentation project configuration file as shown 
 in the following examples.
 
**Example: Configuring an "Edit on GitHub link"**
 
.. code::
 
      {
        "contentIDBase": "https://github.com/rackerlabs/$reponame/$version/",
        "githubUrl": "https://github.com/rackerlabs/$reponame/",
        "githubBranch": "master",
        "meta": {
        "preferGithubIssues": false
       }
      }

The *$reponame* and *$version* variables represent the values for each project. 
Not all projects have a version in the path.  


**Example: Configuring a "Submit an issue" link**

.. code::

      {
        "contentIDBase": "https://github.com/rackerlabs/$reponame/$version",
        "githubUrl": "https://github.com/rackerlabs/docs-rackspace/",
        "githubBranch": "master",
        "meta": {
        "preferGithubIssues": true
        }
      }
      

**Configuration parameters**

``contentIDBase``
      A unique ID that identifies the content repository to the Nexus publishing platform. 
      The value specified must match the one specified in the `deconst control repository 
      configuration file <https://github.com/rackerlabs/nexus-control/tree/master/config/content.d>`_ 
      for the site where content is deployed. This value is required to build and deploy the content.
       
``githubUrl``
     The base URL for constructing the GitHub links to display in the navigation menu. For 
     *Edit on GitHub* links, specify the URL for the documentation source repository. 
     For *Submit an issue* links, decide whether you want issues to be created in the 
     documentation project repository or in a different respository. Then, specify the 
     URL for the target repository. 
     
     .. note:: 
          If your repository is private, specify the URL for 
          another repository. Otherwise, the link target 
          returns a 404 for users that cannot access the private repository. 
     
     
``githubBranch``
     The target branch that determines the branch for submitting changes. 
     If this value is not specified, it defaults to master. To override the default, set 
     this parameter to the branch name.
     
``preferGithubIssues``
     Indicates the GitHub link type. Set this value to true 
     to include the *Submit an issue* link. Set it to false to include an *Edit on 
     GitHub* link." 
  
   
   .. note:: 
   
      For more information about the _deconst.json configuration parameters, see 
      `Authoring Content for Deconst <`https://deconst.horse/writing-docs/author/>`_ in the Deconst documentation. 
