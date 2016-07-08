==============
RPC and DocBot
==============

Current structure :sub:`~\ :sub:`:sub:`:sub:`:sub:`:sub:`~``````\ ~

Our current repo structure looks like this:

-  Work for the current and upcoming release is done in ``master``.
-  Changes are picked from ``master`` to ``v11`` as it's completed.
-  Changes specific to v9 are created as PRs directly against the v9
   branch.
-  v10 has not yet been added as a branch in the rpcdocs tree.

New structure :sub:`:sub:`:sub:`:sub:`:sub:`~`````\ ~~

With DocBot, a change made against a publishing branch is *immediately*
published to the site. To avert the obvious hazards with this, we
propose the following change to branch structure and methodology.

-  The ``master`` branch continues to be the working and staging branch
   for the current/upcoming release. A publishing branch is created for
   that release.
-  A ``vN-stage`` branch is created for the previous release. Changes
   specific to that release will be created as PRs against the
   ``vN-stage`` branch, and picked to the ``vN`` publishing branch when
   ready.

This diagram shows what the structure will look like for v11 (not shown:
v9/v9-stage branches):

This diagram shows what the structure will look like when work begins on
v12 (sometime in 2016):

This diagram shows how this methodology would be applied when work
begins on v13:
