==========================================================
A Guide to Use Case Solutions with Rackspace Private Cloud
==========================================================

Introduction
~~~~~~~~~~~~

Rackspace(R) Private Cloud (RPC) Software delivers the agility,
reliability, and efficiency of a public cloud with the enhanced
security, control, and performance of a private cloud.  RPC provides
cost-effective solutions for several important cloud use cases, all
backed by Fanatical Support(R).  In this paper, we explore how RPC
delivers solutions to running web tier applications: scaling using
Rackspace hybrid clouds, completing the development cycle, and
managing big data.


Web-tier applications
~~~~~~~~~~~~~~~~~~~~~

Web applications are typically architected into multiple tiers: a
presentation or interface tier, a business logic tier, and a database
tier.  Multiple tiers can exist on a single server; however, if this
server fails, the web application will go down.  You can protect from
this kind of failure by distributing components of the web application
across multiple servers.  Adding servers and a load balancer will
extend the ability of the web application to to handle a large number
of clients.

Large numbers of clients accessing the database tier increases the
number of reads and writes, which can eventually push the limits of
vertical scaling.  Horizontally scaling database tiers across multiple
servers can be difficult.  Galera, which is a scalable database
clustering tool, makes the process easier.  Galera enables application
resilience. Your applications can better withstand high-volume access.

Supporting additional databases with horizontal scaling can eventually
reach a point where running web applications on a public cloud becomes
less cost effective.  RPC offers a comprehensive solution to managing
web applications once they reach this point.  The cost of running
workloads on RPC remains relatively fixed each month. Costs are
typically only increased when you add additional hardware to your
cloud.

Another use case is growth and expansion of sensitive data on your
servers.  More database reads and writes can increase concern about
compliance and secure storage of private data.  The benefits of
running a database on RPC include dedicated firewalls, extensive
physical security (if hosted in Rackspace data centers), and an
architecture designed by OpenStack experts.

Connected to the issue of security is a need for single-tenancy. The
"noisy-neighbor effect" describes a loss of performance in situations
where web applications running in a public cloud are affected by the
activity of other application outside of your control.  RPC servers
are single-tenant servers.  OpenStack instances can be distributed as
it suits your needs without performance concerns from other tenants.


Hybrid cloud
~~~~~~~~~~~~

You may want to run applications on a private cloud, but expand or
burst into the public cloud under certain conditions.  As your project
plans change over time, a hybrid approach can increase flexibility.
Rackspace Rackconnect services allow you to extend applications from a
private to public cloud as needed.  Automation and monitoring settings
can transform this extension into a dynamic process, driven by
policies based on schedules or events.

Creating an *Autoscale Group* allows you to select which load balancer
to attach to a cloud server, which image to run, and specific *cloud
flavors*.  You can specify the number of cloud servers that will be
created as part of the Autoscale Group.  After you set up all the
parameters for the Autoscale Group, activate the feature switches on
a web hook. Attached to an alarm, the web hook triggers the Autoscale
Group.

The *alarm* is the second part of the Hybrid Cloud feature that works
closely with an Autoscale Group.  Information gathered about cloud
activity - metrics - signals the alarm, and activates the Autoscale
Group.  Load average, for example, is an essential metric that you can
monitor.  You can set alarms to activate when the load average on the
server reaches a certain level.

A *notification plan* is the third part of the hybrid feature that
works closely with the Autoscale Group and alarm.  Triggered by an
alarm, the notification plan is a feature that uses the web hook
initiated when choosing the Autoscale Group parameters.  The key
feature of the notification plan is that it switches the Autoscale
Group parameters off after server activity drops below the trigger set
for the alarm.


Development cycle
~~~~~~~~~~~~~~~~~

RPC provides a robust platform that manages the discovery, design,
development, testing, and release stages of your development life
cycle.  For startups, new software and applications are the center of
your business.  RPC provides a common environment to store Git,
Gerrit, and Jenkins to manage version control.  RPC also helps protect
and safeguard essential and vital test products.  Control over the
environment is entirely yours, without noisy neighbor problems that
can occur in a public cloud.

If you have heightened security or compliance requirements, RPC can be
hosted and managed from a data center of your choosing.  Partitions
can be created within the private cloud to wall off departments within
your business to help prevent interference or disruptions.  Web
applications can be designed and architected in a multi-tiered method
for increased availability.

Tenants, also called projects, allow administrators to separate groups
of users into isolated and discrete subsets.  For example, you can
isolate tenants and compute nodes to create separate development and
production environments.  This represents a solution to the problem of
common infrastructure, or working within test environment
infrastructure that is as similar as possible to the production
environment.  The OpenStack Neutron service creates tenant networks,
which are networks completely isolated from other networks.  Neutron
routers, which are virtual networking devices, connect these isolated
networks together if needed.

Cloud administrators can create OpenStack host aggregates that are
exposed to users as availability zones.  Host aggregates group compute
nodes with specific definable characteristics, for example nodes with
SSDs or faster processors, or older nodes with legacy hardware.  For
redundancy, nodes can be grouped that use separate power supplies or
networks.  Users can then bring up an instance on a node in the most
efficient or cost effective availability zone.  For example, compute
intensive workloads can be tasked to a subset of high performance
servers, or workloads can be restricted to servers in a certain
physical location.  Or, separate zones can house critical computing
workloads and non-critical development and testing workloads to
increase availability and efficiency. Zones can also separate
different compute nodes for specific parts of the development cycle.

Host aggregates can be set up to allow different flavors to run with
different CPU and RAM allocations.  When high-intensity compute loads
and low-intensity development and testing systems share the same
cloud, they can operate without consuming the high-use systems or
wasting resources on low-use systems.


Big data
~~~~~~~~

Data that moves too quickly, shows large variety, and is potentially
large in size can be difficult to handle with traditional software
tools such as transactional databases.  RPC helps you take advantage
of broad, diverse, and high-velocity data.  Large data sets that are
crucial to business require enhanced privacy and security.  Workload
management is essential for handling big data.  RPC helps ensure
consistent performance compared to a public cloud.

Accumulated big data can be stored securely; however, without the
right configuration to sort and retrieve results, users may face
serious control problems.  Raw data might require specific server and
database configurations to allow you to access and analyze your
accumulated information.  RPC gives you the ability to customize and
adapt your choice of spindle hard drives or SSD hard drives in compute
nodes, 1 Gb or 10 Gb networking, and the ability to exactly define
OpenStack flavors.  The instances generated with these settings offer
flexibility and control over the amount of CPU, RAM, and storage
capacity available.

In regards to cost, big data processing tools running on a private
cloud are traditionally charged at a flat rate, independent of the
process run time.  Running large-scale databases on a public cloud can
become costly, particularly if the project runs for an extended amount
of time.  Public cloud costs continually increase until the workload
ends.  In contrast, you can create as many instances as you need in
RPC, and costs are only added when you add physical hardware to your
environment.  Rackspace can help you analyze your needs to select a
cost-effective solution.

For more information about how Rackspace can help manage and support
your private cloud, please see http://www.rackspace.com/cloud/private.


References
~~~~~~~~~~

RPC Insights 3.1 - Use Case 1 - Web Tier Applications, web cast.
http://youtu.be/mknyC4tccBQ

RPC Insights 3.1 - Use Case 1 - Web Tier Applications, blog.
https://developer.rackspace.com/blog/using-rpc-host-web-tier-apps/

RPC Insights 3.2 - Use Case 2 - Software Development Life cycle, web cast.
http://youtu.be/s9GNgYUpXyU

RPC Insights 3.2 - Use Case 2 - Software Development Life cycle, blog.
https://developer.rackspace.com/blog/using-rpc-software-dev-lifecycle/

RPC Insights 3.3 - Use Case 3 - Big Data Solutions, web cast.
http://youtu.be/V55gzeBxmwE

RPC Insights 3.3 - Use Case 3 - Big Data Solutions, blog.
https://developer.rackspace.com/blog/big-data-solution-running-on-rpc/
