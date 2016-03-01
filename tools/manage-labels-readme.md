# Importing and exporting labels

Instead of manually copying and updating each label in a GitHub repository, you can 
use the [github-label-manager npm module](https://www.npmjs.com/package/github-label-manager) 
to manage your GitHub label configuration across repositories.

- Export label configuration from an existing repository to a JSON schema file.
- Copy new labels from one repo to another repo without overwriting the existing labels. 
- Delete all labels and import a replacement set from an existing label configuration file. 

## Prerequisites

- Install Node.js and npm 
- Configure system to [install and use global npm packages](http://www.sitepoint.com/beginners-guide-node-package-manager/)


## Set up
Complete the following steps to install the Github label manager software and configure environment variables required to authenticate and run commands against GitHub repositories that you have permission to update.

#. Follow the instructions to install the 
   [github-label-manager npm module](https://www.npmjs.com/package/github-label-manager).

#. Generate a [GitHub personal access token](https://github.com/settings/tokens) or copy 
   an existing one so that you can authenticate when submitting requests. 

#. Export your GitHub username and personal access token value to environment variables, or 
   add them to your ``~/.bash_profile`` .  

You can find existing label configuration files in the 
[docs-rackpace repository](https://github.com/rackerlabs/docs-rackspace/tree/master/tools/GitHub-infra-templates).  
To import these configurations to a repository, download them to your system.  


For command examples and more information, see the [github-label-manager documentation](https://www.npmjs.com/package/github-label-manager). 




