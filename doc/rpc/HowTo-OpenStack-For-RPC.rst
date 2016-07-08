=========================
OpenStack Docs for RPCers
=========================

Contributing to OpenStack is documented across a number of places, and
very thoroughly documented on the OpenStack wiki. This page is an
attempt to round up and simplify all the steps for a first-time RPC (or
other Racker) OpenStack contributor.

Software prerequisites
----------------------

Before you dive in, you should ensure that you have the following
software prerequisites established:

**Mac**

-  `Xcode <https://developer.apple.com/xcode/>`_

Be sure to agree to the Xcode license:

``sudo xcodebuild -license``

-  `Macports <https://www.macports.org/>`_ or
   `Homebrew <http://brew.sh/>`_
-  `pip <https://pypi.python.org/pypi/pip>`_
-  Upgrade ``setuptools``:

   .. code::

      sudo pip install --upgrade setuptools

**Windows**

-  ?

Launchpad, CLAs, git, and more
------------------------------

The OpenStack wiki has a page for first-time docs contributors to walk
you through the initial setup steps:

http://docs.openstack.org/contributor-guide/first-timers-quickstart.html

.. note::

   To avert any possible confusion, use the same e-mail address
   EVERYWHERE that it asks you for one.

Once you've finished, you'll have the following prerequisites in place:

-  A Launchpad account on UbuntuOne, which enables the Gerrit Code
   Review system to identify you. It also enables OpenStack to credit
   you with bug fixes and patches
-  Membership in the OpenStack foundation
-  A signed CLA
-  Windows prereqs (only if you're using a Windows machine)
-  git and git-review
-  An SSH key
-  A local working copy of the ``openstack-manuals`` repository

The Stackalytics commit
-----------------------

This is the first OpenStack commit you should ever do. It's not a docs
commit, but it will give you a relatively simple introduction to the git
and gerrit process that applies whether you're doing documentation or
not.

[The Gerrit Workflow] page offers more documentation to help you
understand

#. Clone the ``stackalytics`` repo.

   .. code::

      git clone https://github.com/stackforge/stackalytics.git

#. Go to your local ``stackalytics`` working directory and make sure
   everything is up to date:

   .. code::

      cd stackalytics
      git remote update
      git checkout master
      git pull --ff-only origin master

#. Create a branch with a meaningful name, such as your username.

   .. code::

      git checkout -b new-user/<your_username>

#. Register yourself so stackalytics will track your future
   contributions by editing ``etc/default_data.json``.

   .. code::

      $EDITOR etc/default_data.json

   Update the file as follows:

   -  Add your entry in launchpad\_id sorted order
   -  Include your launchpad id
   -  Include your name
   -  Include your affiliation with our great company rackspace
   -  Include the email address(es) you will be making commits using (and
      your Rackspace email address, so our affiliation is secured)

#. Verify that the change is what you expect:

   .. code::

      git diff

#. Commit the change.

   Enter only 50 characters for the first line of the commit message, and
   no trailing full stop. A good sample commit message might be something
   like this: ``"<Your Name> (<launchpad_id>) works for Rackspace"``.

   .. code::

      git add etc/default_data.json
      git commit
      git review

   Congratulations! Your first commit has been submitted for review.

#. Post the gerrit review URL to #rcbaudocs so that your peers can
   review it.

After it's been reviewed and approved, it will be automatically merged
and applied.

Your first documentation patch
------------------------------

Before you start on docs patches, be sure to do the following:

-  Bookmark https://wiki.openstack.org/wiki/Documentation/HowTo. You'll
   refer to it frequently.
-  Join the `OpenStack Docs mailing list
   <http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-docs>`_.
   Sending out an email to introduce yourself is a good idea, too.
-  Join the `#openstack-doc IRC channel on Freenode
   <https://wiki.openstack.org/wiki/IRC#OpenStack_IRC_channels_.28chat.freenode.net.29>`_.
-  Set your command line text editor in your ``~.bashrc`` file. See
   http://stackoverflow.com/questions/20287331/how-can-i-define-my-text-editor-in-bashrc.
   `vi <http://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/>`_
   or `vim <http://www.vim.org/>`_ are good choices.

What should your first patch be?

-  Look at the
   `existing documentation <http://docs.openstack.org/>`_ for
   easy-to-fix problems, such as typos, spelling errors, or badly worded
   documentation. This is easier than trying to dive into technical
   content if you don't already have an area of expertise.
-  Check the `bug list <https://bugs.launchpad.net/openstack-manuals>`_ for
   low-hanging fruit.

Once you've picked something to work on, here's how you make the patch.

#. Navigate to your ``openstack-manuals`` directory.

#. Make sure it's up to date.

   .. code::

      git remote update
      git checkout master
      git pull --ff-only origin master

#. Create a branch in which to do your edits. Give it a meaningful name,
   including your username and the bug name if you're working on a bug:

   .. code::

      git checkout -b bug123456/username

#. In your preferred editor (oXygen or emacs recommended), open the file
   that you want to edit. Make your changes and be sure to adhere to
   `writing conventions <https://wiki.openstack.org/wiki/Documentation/Conventions#Writing_style>`_,
   `markup conventions <https://wiki.openstack.org/wiki/Documentation/Conventions#DocBook_markup_conventions>`_,
   and `whitespace conventions <https://wiki.openstack.org/wiki/Documentation/Conventions#DocBook_markup_conventions>`_.

#. `Build your output locally
   <https://wiki.openstack.org/wiki/Documentation/HowTo#Building_Output_Locally>`_
   to see what the change looks like and `use tox to check your code
   <https://wiki.openstack.org/wiki/Documentation/HowTo#Using_Tox_to_check_builds>`_.
   ``tox -e checkniceness`` is especially helpful in preventing patches
   from getting rejected for whitespace errors (a very common problem).

#. Commit the change with ``git commit``:

   .. code::

      git commit -a

This will open your default text editor so that you can add a commit
message. Follow this convention:

-  First line: Summary of the change
-  Second line: Empty
-  Third line: A longer description of the change
-  Fourth line: Empty
-  Fifth line: Backport information. Select the versions that need to be
   updated. If you're working on the Install Guide or the
   Config-Reference Guide, use backport: icehouse for now. Once we start
   working on Juno docs, you'll need to choose backport: juno backport:
   havana to backport to just one release backport: havana grizzly to
   backport to more than one release backport: none for no backporting
-  Sixth line: Bug information. This will automatically update the bug
   accordingly.

   -  Closes-Bug: #1234567 if the commit is intended to fully fix and
      close the bug being referenced.
   -  Partial-Bug: #1234567 if the commit is only a partial fix and more
      work is needed.
   -  Related-Bug: #1234567 if the commit is merely related to the
      referenced bug.

#. Submit your patch for review:

   .. code::

      git review

Jenkins will now test your changes and, provided you haven't broken the
build, your patch will beup for review. gerrit will provide you a link
to the patch in the form https://review.openstack.org/#/c/review-number/.

-  **If your patch gets a -1 or -2 review with a note not to merge it,
   you might need to do some changes.** In this case, follow the
   instructions at `How to amend a review in progress
   <https://wiki.openstack.org/wiki/Documentation/HowTo#How_to_amend_a_review-in-progress>`_
   to make the changes and resubmit your patch for review. If you get
   stuck, try asking your mentor, or in the #openstack-doc IRC channel
   for help.
-  **If you need to do a third (or fourth, or ...) patchset**, then
   follow the normal instructions above until you hit a error like this:

   .. code::

      fatal: A branch named 'review/yourname/bug/1234567' already exists.

   If this happens, you will need to delete the local branch on your system
   before you can check out the patch to work on it again. Take a note of
   the name of the local branch that the error gives you, and delete it by
   doing this:

   .. code::

      git branch -D review/yourname/bug/1234567

   You can then go ahead and do ``git review -d 123456`` with the review
   number as normal.

After the patch has been favorably reviewed by a minimum number of
reviewers, a core reviewer will merge the patch and it will go live. If
your patch updates or closes a bug it will be updated automatically
thanks to the bug line in your commit message.

Making changes to a stable branch
---------------------------------

If you need to make changes to older released documentation, such as
Icehouse documentation, refer to `How to make changes to a stable branch
<https://wiki.openstack.org/wiki/Documentation/HowTo#How_to_a_make_changes_to_a_stable_branch>`_.
If you follow the steps in the link and receive the error:

.. code::

   fatal: Cannot update paths and switch to branch <branch name> at the same time

Follow these steps.

#. Clone the repository to your local machine. For example:

   .. code::

      git clone https://github.com/openstack/openstack-manuals.git -b stable/havana my-havana-repo

#. Change the directory to your local folder. For example:

   .. code::

      cd ~/openstack-manuals/my-havana-repo

#. Create a branch to do your edits.

   .. code::

      git checkout -b <branchname>

#. Do your edits, build them locally to test, then commit your changes
   in the same way (don't forget the meaningful git commit message):

   .. code::

      git commit -a

#. Submit your patch for review with the git review command:

   .. code::

      git review

Doing docs reviews
------------------

Once you've become comfortable in the OpenStack world, you can review
docs.

OpenStack docs use exactly the same process as all other code. When
people propose patches to the documentation, it needs to be reviewed by
others before it will accepted into the build. While docs can be
slightly less rigorous than other code, there are still a lot of docs
patches that require review. Try to do at least two reviews a day.

#. Look for patches that require review. Use this `saved search
   <https://review.openstack.org/#/q/status:open+(project:openstack/openstack-manuals+OR+project:openstack/api-site+OR+project:openstack/object-api+OR+project:openstack/image-api+OR+project:openstack/identity-api+OR+project:openstack/compute-api+OR+project:openstack/volume-api+OR+project:openstack/netconn-api+OR+project:openstack/operations-guide),n,z>`_
   to find all patches currently waiting for review. You can also watch
   the #openstack-doc IRC channel for new patches as they come in.

#. Follow the steps at `Reviewing documentation
   <https://wiki.openstack.org/wiki/Documentation/HowTo#Reviewing_Documentation>`_
   to review patches.

A note on review rigour: There are very few guidelines about what
consists of a successful patch, but the general approach seems to be
that if it's technically accurate and better than the existing content,
then it should be approved. The main things to look for:

-  General spelling and grammar.
-  Technical accuracy. Where possible, test commands on your own VM to
   make sure they're accurate. Check any related bugs, and the Disqus
   comments on the doc site to see if there's anything else you might
   need to take into account.
-  The 'is it better than what we have already' test. Check the diff, or
   go look at the current document on the doc site, and determine if the
   changes are an improvement.

Provide corrections in-line by double-clicking on the offending line in
the diff viewer to write your suggested changes.

Note that if there's just one or two really minor changes (or in a
situation where the writer is either ESL or could be otherwise unable to
improve the doc themselves), consider checking out the patch and editing
it quickly yourself. Be nice.
