#!/bin/bash

if [ "$TRAVIS_REPO_SLUG" == "rackerlabs/docs-rackspace" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_BRANCH" == "master" ]; then

  echo -e "Publishing gh-pages...\n"

  cp -R _build/docs/html $HOME/html

  cd $HOME
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "travis-ci"
  git clone --quiet --branch=gh-pages https://${GH_TOKEN}@github.com/rackerlabs/docs-rackspace gh-pages > /dev/null

  cd gh-pages
  find * -not -name ".*" -delete
  cp -Rf $HOME/html ./
  git add -f .
  git commit -m "Latest doc on successful travis build $TRAVIS_BUILD_NUMBER auto-pushed to gh-pages"
  git push -fq origin gh-pages > /dev/null

  tput setaf 2; echo "Docs published to http://rackerlabs.github.io/docs-rackspace/."
  tput sgr0

fi