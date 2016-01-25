.. glossary-terms::

Terms
-------------

A
~~~~~

account
^^^^^^^^^^^

The portion of the Rackspace Cloud system designated for your use. The system is designed 
to be used by many different customers, and your user account is your portion of it.  
You must identify yourself with a valid user name and password or API access key. After you
are authenticated, you have full read/write access to the objects
stored in your account.

agent
^^^^^

*(Cloud Backup)* An executable located on your cloud server that
performs backups and restores. The agent must be installed on any
server that you want to back up using Cloud Backup.

*(Cloud Monitoring)* A service located on your cloud server that gathers
metrics based on `check`_ configurations and pushes those metrics to Cloud Monitoring.
The agent gathers server information regarding network configuration,
process tables, and disks, and server metrics such as swap, CPU,
disk, file system, and network device usage. The metrics can be
analyzed, can trigger alerts, and can be archived.

agent token
^^^^^^^^^^^^^^

*(Cloud Monitoring)* An authentication token used to identify a
monitoring agent when it communicates with Cloud Monitoring.

alarm
^^^^^^^

Contains a set of rules that determine when the monitoring system
sends a notification. You can create multiple alarms for the
each `check type`_ associated with an entity. For example, if your
entity is a web server that hosts your company's website, you can
create one alarm to monitor the server itself, and another alarm
to monitor the website. The alarms language provides you with
scoping parameters that let you pinpoint the value that will
trigger the alarm. The scoping parameters are inherently flexible,
so that you can set up multiple checks to trigger a single alarm.
The alarm language supplies an adaptable triggering system that
makes it easy for you to define different formulas for each alarm
that monitors an entity's uptime.

API
^^^^^^^

Application Program Interface. A set of programming instructions
and standards that enables application programs to interact with each
other and share data. Rackspace Cloud APIs are defined as RESTful
HTTP services that use all aspects of the HTTP protocol, including
methods, URIs, media types, and response codes.

API key
^^^^^^^^^^

A unique alphanumeric identifier associated with your account that
is used for universal authentication commands for all of your services.

authentication
^^^^^^^^^^^^^^^^^

The act of passing in credentials, confirming an identity, and
returning a token representation of the verified identity. In the
Rackspace Cloud, you authenticate by submitting a POST tokens API
request with valid credentials to a Rackspace Cloud Identity service
endpoint. Credentials are typically a user name and API key.
However, other types of credentials can be accepted based on service,
tenant, or user account configuration.

.. _authentication-token-term:

authentication token
^^^^^^^^^^^^^^^^^^^^^^

An encrypted string returned by the Rackspace Cloud Identity service
in response to an authentication request submitted with valid
credentials. The token stores information about the services and
operations available to the authenticated user and provides a secure
way to transmit authentication information when submitting API requests.

authorization
^^^^^^^^^^^^^^^^^

A process that determines the capabilities available to an
authenticated user, system, or process. In the Rackspace Cloud, the
Identity service provides centralized authorization to ensure
that clients have appropriate access to information and information
processing capabilities based on Identity service roles such as system
administrator and user administrator. The Rackspace Cloud also
supports Role Based Access Control (`RBAC`_ ), which defines
product-specific roles to authorize capabilities at the service level.

B
~~~~

backup
^^^^^^^^

*(Cloud Databases)* A copy of computer data for a database instance that
can be used to restore the original instance if necessary.

*(Cloud Backup)* A group of folders, files, or both stored on Cloud
Backup for a particular server and configuration.

backup configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Backup)* A definition of what to back up and when to perform the
backup. The backup configuration includes a schedule for the backup,
the files to back up, and notifications.

backup schedule
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Backup)* As part of a backup configuration, the specified
frequency and time of a backup. You can define a schedule to create
server images at regular intervals (daily and weekly). Backup
schedules are configurable per server.

*(Cloud Databases)* A schedule for running a weekly backup of a
database instance. An incremental backup runs at the end of every day,
and a full backup runs on the day defined by the backup schedule.

C
~~~

caching rule
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Rackspace CDN)* A rule that controls the time-to-live (TTL) of an
object. The TTL tells the :ref:`edge nodes <edge-node-term>` how long to cache the object
before checking the origin (the web server) for a fresh copy.
When the TTL expires for an object, the edge node pulls the
object from the origin again.

CDN
^^^^^^^^^^^^^^^^^^^^^^^^^

Content delivery network. A system of distributed servers (network)
that deliver web pages and other assets to a user based on the
geographic location of the user, the origin of the web page, and a
content delivery server. CDNs decrease the load time of assets by
caching them on :ref:`edge nodes <edge-node-term>`, also called edge servers or point of
presence (PoPs) servers.  Edge nodes are distributed around the globe,
so requests travel to a local location to get assets rather than to
and from a data center based far from the end user.

.. _cdn-enabled-container-term:

CDN-enabled containers
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Files)* Containers that serve content through the Akamai
content delivery network (CDN). When a `container`_ is CDN-enabled, any
files in the container are publicly accessible and do not require
an authentication token for read access. However, uploading content
into a CDN-enabled container is a secure operation and requires a
valid authentication token. Each published container has a unique
URL that can be combined with its object name and openly distributed
in web pages, emails, or other applications.

certificate authority
^^^^^^^^^^^^^^^^^^^^^^^^^

An issuer of online security certificates that show whether a
website is verified as safe.

check
^^^^^^^^^^^^^^^^^^^^^^^^^

The part of the monitoring system that explicitly specifies how you
want to monitor an `entity`_. The check specifies the parts of the
entity that you want to monitor, the monitoring frequency, how many
monitoring zones are launching the check, and so on. You can associate
one or more checks with an entity. An entity must have at least
one check, but by creating multiple checks for an entity, you can
monitor several different aspects of a single resource. For each
check you create within the monitoring system, you'll designate a
check type.

check type
^^^^^^^^^^^^^^^^^^^^^^^^^

A definition that specifies what kind of data a check collects. The
check type tells the monitoring system which method to use, such
as PING, HTTP, or SMTP, when investigating the monitored resource.

CIDR
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Networks)* Classless Inter-Domain Routing. A method for
allocating IP addresses and routing Internet Protocol packets.

claim
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* The process of a `worker`_ checking out a message to
perform a task. Claiming a message prevents other workers from
attempting to process the same message.

claim TTL
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* Time-to-live value that defines how long a message
will be in claimed state. A message can be claimed by only one
`worker`_ at a time.

cluster
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Big Data)* A group of virtual servers (nodes).

collector
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Monitoring)* An endpoint that collects data from the
`monitoring zone`_ and directly maps the data to an individual machine
or a virtual machine. Monitoring zones contain many collectors,
all of which are within the IP address range listed in the response.

**Note**: There may also be unallocated IP addresses or unrelated
machines within that IP address range.

configuration group
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Databases)* A collection of key/value pairs, where the valid
key and values are defined per datastore (such as MySQL). Some
directives can be applied dynamically, and other directives
require a server restart to take effect. The configuration group
can be applied to an instance at creation or applied to an existing
instance to modify the behavior of the running datastore on the
instance. A configuration group consists of a collection of
:ref:`configuration parameters <configuration-parameter-term>`.

.. _configuration-parameter-term:

configuration parameter
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Databases)* A key/value pair that represents settings that can
be applied to a database instance.

connection logging
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Load Balancers)* Feature that allows logs to be delivered
to a Cloud Files account every hour. For HTTP-based protocol traffic,
these are Apache-style access logs. For all other traffic, this
is connection-and-transfer logging.

.. _consumer-term:

consumer
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* A server that claims :ref:`messages <message-term>` 
from a `queue`_. In the `producer-consumer`_ model of
messaging, producers post messages
to a queue, and then consumers claim those messages and delete them
after they complete the actions associated with the messages. A
consumer is also referred to as a worker.

container
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Files)* A storage compartment that provides a way to organize
data. A container is similar to a folder in Windows or a directory
in UNIX. The primary difference between a container and these
other file system concepts is that containers cannot be nested.

convergence
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* The act of adding or removing enough servers to satisfy
the needed capacity.

convergence delta
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* The change in the number of servers that the system
makes when a `scaling policy`_ is executed. For example, if the
convergence delta is 2, the system adds 2 servers. If it is -10,
the system removes 10 servers.

cooldown
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* The configured length of time that either a
`scaling group`_ or a `scaling policy`_ must wait
before taking action. A group
cooldown is the configured length of time that a scaling group
must wait after scaling before beginning to scale again. A policy
cooldown is the configured length of time that a scaling policy
must wait before being executed again.

CPU alarm
^^^^^^^^^^^^^^^^^^^^^^^^^

An `alarm`_ that sends a notification when the average CPU usage of a
monitored server exceeds the set criteria.

CPU check
^^^^^^^^^^^^^^^^^^^^^^^^^

A `check`_ that monitors and displays your server's CPU usage. It
also displays your server's historical usage.

credentials
^^^^^^^^^^^^^^^^^^^^^^^^^

Data that belongs to and identifies a specific user. Because
credentials are assumed to be known by only one user, users who
present valid credentials are assumed to have proven that they
are who they say they are. Credentials include a matching user name
and password, a matching user name and API key, a unique token,
a secret question and answer, a digital certificate, and a fingerprint.

cURL
^^^^^^^^^^^^^^^^^^^^^^^^^

A command-line tool for transferring data with URL syntax. cURL
enables you to transmit and receive HTTP requests and responses
from the command line or from within a shell script. Using cURL, you
can work with any of the Rackspace REST APIs directly without
using one of the client APIs.


D
~~~~

data granularity
^^^^^^^^^^^^^^^^^^^^^^^^^

The increments at which metric data is measured. When you fetch 
`data point`_ metrics, you specify several parameters to control the granularity of data 
returned. The following granularities of data are supported: full resolution data and 
rollups computed at 5, 20, 60, 240 and 1440 minute intervals.

data point
^^^^^^^^^^^^^^^^^^^^^^^^^

A value that stores metrics. Metrics are stored as full resolution
data points, which are periodically rolled up (condensed) into
coarser data points. See also `data granularity`_.

database
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Databases)* The database engine running on your
`database instance`_. Currently the supported database
engines are MySQL, Percona, and MariaDB. Also referred to as a
`datastore`_.

database instance
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Databases)* An isolated database environment with compute and
storage resources in a single tenant environment on a shared
physical host machine. You can run a database instance with your
choice of one of the following database engines: MySQL, Percona,
or MariaDB.

datastore
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Databases)* The database engine running on your
`database instance`_. Currently the supported database
engines are MySQL, Percona, and MariaDB. Also referred to as a
`database`_.

DDI
^^^^^^^^^^^^^^^^^^^^^^^^^

The account number assigned to a Rackspace Cloud account. The DDI,
or account number, corresponds to the tenant ID, which can be
found on the Cloud Control Panel or by using the Rackspace Cloud
Identity API to view user credentials.

Note:: 
   
  Another name for DDI is Mosso ID.
  

distros
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Big Data)* A list of supported distributions and their
corresponding versions, as well as a list of supported services
and components per distribution.

domain
~~~~~~~~~~~~

*(Cloud Identity)* A domain represents an administrative boundary for identity management.


DNS
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud DNS)* Domain Name System. Determines Internet `domain`_ 
name-to-address and address-to-name resolutions. All
domains and their components, such as mail servers, use DNS to resolve to
the appropriate locations. DNS servers are usually set up in a
master-slave relationship; failure of the master invokes the slave.
DNS servers can also be clustered or replicated so that changes
made to one DNS server are automatically propagated to other
active servers.

DNS record
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud DNS)* A record that belongs to a particular `domain`_ and is
used to specify information about the domain. There are several types
of DNS records. Each record type contains particular information
used to describe that record's purpose. For example, mail exchange
(MX) records specify the mail server for a particular domain, and
name server (NS) records specify the authoritative name servers
for a domain.

domain
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud DNS)* An container of all DNS-related information
containing one or more records.

*(Cloud Identity)* A resource that establishes an administrative
boundary for a customer and a container for a customer's tenants
(accounts) and users. Individual domains can represent an
individual, company, or operator-owned space within the Rackspace
Cloud Identity service. In the Identity service API, the domain
resource provides a mechanism to expose administrative activities
directly to system users. Specifically, an Identity service
administrator can create tenants, users, and groups within a
domain and assign roles to users and groups. User administrators
that have domain administrator capabilities can view and manage
the domain associated with their Rackspace Cloud account.

domain owner
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud DNS)* The account that creates the `domain`_.

E
~~~~

.. _edge-node-term:

edge node
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Rackspace CDN)* Point of presence (PoP) servers located around
the world. Edge nodes cache content and serve it directly to
customers, reducing transit time to a customer's location. Also
known as an edge server.

endpoint
^^^^^^^^^^^^^^^^^^^^^^^^^

An entry point to an API. The endpoint is defined as a set of
base URLs, and API operations are defined relative to these
URLs. An API might offer several regional endpoints for a single API.

endpoint template
^^^^^^^^^^^^^^^^^^^^^^^^^

A template that a service administrator can use to manage API
service endpoints that apply to many or all tenants without having
to add each `endpoint`_ on each tenant manually. For example, a
service developer can define a global endpoint template that is
automatically included in the `service catalog`_ for all tenants
authorized to use that service. The endpoint template also
specifies the URLs for the internal, administrative, and public
endpoints that provide access to the service.

entity
^^^^^^^^^^^^^^^^^^^^^^^^^

The object or resource that you want to monitor. An entity is
commonly a web server, but it might also be a website, a web page,
or a web service. When you create an entity, you specify
characteristics that describe what you are monitoring.

error page
^^^^^^^^^^^^^^^^^^^^^^^^^

The HTML file that is shown to the end user when an error occurs
in the service. By default every virtual server is provided with a
default error file. It is also possible to submit a custom error page.


F
~~~~


Federation
^^^^^^^^^^^^^
See `FIdm`_.

FIdM
^^^^^^^^^^^^^^^^^^^^^^^^^

Federated Identity Management. A set of policies, practices,
and protocols that can be used to manage authentication and
authorization of users, processes, and devices across organizations.
The goal of identity federation is to enable users of one domain
to securely access data or systems of another domain seamlessly
by passing an authentication token that was issued by a
trusted Identity Provider.

file system alarm
^^^^^^^^^^^^^^^^^^^^^^^^^

An `alarm`_ that sends a notification when the disk space in your
specified directory exceeds the parameter that you set.

file system check
^^^^^^^^^^^^^^^^^^^^^^^^^

A `check`_ that monitors and displays disk usage in a directory
that you specify.

fine-grained access control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*(Cloud Identity)* Access restriction configured for an individual user or group of 
resources. 

flavor
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Servers)* An available hardware configuration for a server.
Each flavor is a unique combination of disk, memory, vCPUs, and
network bandwidth.

*(Cloud Databases)* An available hardware configuration for a database
instance. Each flavor is optimized for performance and has a
unique combination of memory capacity, priority for CPU time, and
network bandwidth.

G
~~~~

gateway
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Networks)* Hardware or software that connects two or more
networks, converting data to the protocol understood by each network.

group
~~~~~~~~

*(Cloud Identity)* A collection of users. Currently used by Rackspace for grouping users 
by API rate-limits (ex: ability to create 5 servers a day).

H
~~~~

HDFS
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Big Data)* Hadoop Distributed File System. From Apache, the
default file system that is used in Cloud Big Data.

health monitor
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Load Balancers)* A configurable feature of each load balancer
that is used to determine whether a back-end node is usable for
processing a request. The load balancing service currently
supports active health monitoring, which uses synthetic transactions
executed at periodic intervals to determine the condition of a node.

host
^^^^^^^^^^^^^^^^^^^^^^^^^

A computer or network facility that stores data and that is
available to be accessed by other computers.

I
~~~

identity assertion
^^^^^^^^^^^^^^^^^^^^^^^^^

A method for expressing the identity of the sender
(for example, user name) in a Simple Object Access Protocol
(SOAP) message. Identity assertions provide a mechanism for
exchanging authentication and authorization between an Identity
provider and a service provider to support federated identity management.

.. _identity-provider-term:

Identity provider
^^^^^^^^^^^^^^^^^^^^^^^^^

Identity Provider (IdP). A trusted provider that creates, maintains, and
manages identity information for principals
(users, services, or systems) and provides principal authentication
to other service providers (applications) within a federation
or distributed network. Identity providers issue identification
information on behalf of authenticated users who want to interact
with different service providers. This process is implemented
through an authentication module that verifies a security token
as an alternative to explicitly authenticating a user within a
security realm. Information is transmitted through federation
protocols such as SAML and OpenID Connect.

IdP
~~~~~~~

See `Identity provider`_.

IdP chaining
~~~~~~~~~~~~~~~~~

*(Cloud Identity)* IDP Chaining

IDP chaining involves authenticating against multiple 
:ref:`identity providers <identity-provider-term>` in succession, 
stopping once a successful authentication is reached

image
^^^^^^^^^^^^^^^^^^^^^^^^^

A collection of files for a specific operating system (OS)
that are used to create or rebuild a server. Rackspace provides
prebuilt images. You can also create custom images from servers
that you have launched. Custom images can be used for data
backups or as templates for additional servers.

.. _image-consumer-term:

image consumer
^^^^^^^^^^^^^^^^^^^^^^^^^

A user who has been given access to an `image`_. An
`image producer`_ 
shares an image with a consumer by making the consumer a
member of that image. The consumer then accepts or rejects the
image by changing the image member status. After it is accepted,
the image appears in the consumer’s image list.

image file
^^^^^^^^^^^^^^^^^^^^^^^^^

File that contains the raw binary data for a server `image`_.

image member
^^^^^^^^^^^^^^^^^^^^^^^^^

A user who has been given access to an image and has accepted
that access. Normally, if an image is not shared, only the owner
(image producer) can boot from the image.

image producer
^^^^^^^^^^^^^^^^^^^^^^^^^

A user who creates server images. The producer can share images
with :ref:`image consumers <image-consumer-term>` to allow the
consumer to use the shared image when booting a server.

image record
^^^^^^^^^^^^^^^^^^^^^^^^^

A record that provides information about the bootable binary
data of an `image`_, including format, size in bytes, checksum, and
operating system.

image tag
^^^^^^^^^^^^^^^^^^^^^^^^^

A string of characters used to identify a specific
`image`_ or images.

image task
^^^^^^^^^^^^^^^^^^^^^^^^^

A resource that enables you to perform asynchronous image-related
operations such as importing or exporting
an `image_`. The task
resource can be polled to determine the status of the import or
export operation, and the resource is deleted at a set time
identified by the expires-at parameter.

ingest
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Rackspace Metrics)* The process of obtaining, importing, and
processing data for later use or storage in the Metrics database.
This process can involve modifying individual files by editing
their content or formatting them to fit into a larger document.

instance
^^^^^^^^^^^^^^^^^^^^^^^^^

A virtual machine that runs inside the cloud.

instance type
^^^^^^^^^^^^^^^^^^^^^^^^^

A description of the compute, memory, and storage capacity of
computing instances.

internal URL
^^^^^^^^^^^^^^^^^^^^^^^^^

A URL that is accessible only from within the Rackspace Cloud
network. Access to an internal URL is always free of charge.
See also `ServiceNet`_.

.. _ip-address-term:

IP address
^^^^^^^^^^^^^^^^^^^^^^^^^

Internet Protocol address. For IPv4, an IP address is a 32-bit
number that identifies each sender or receiver of information that is
sent in packets across the Internet. In IPv6, an IP address is a
128-bit number.

isolated network
^^^^^^^^^^^^^^^^^^^^^^^^^

A virtual `layer-2 network`_ created through Cloud Networks that
can be attached to a new cloud server. An isolated network keeps
your server separate from the Rackspace network (`ServiceNet`_), the
Internet (`PublicNet`_), or both. When you create an isolated network,
it is associated with your tenant ID.

J
~~~~

JSON
^^^^^^^^^^^^^^^^^^^^^^^^^

JavaScript Object Notation. An open standard format that uses
human-readable text to transmit data objects consisting of
key-value pairs.

JSON pointer
^^^^^^^^^^^^^^^^^^^^^^^^^

The syntax for identifying a specific value within a `JSON`_ document.
A restricted JSON pointer is a Unicode string that contains a
sequence of exactly one reference token, prefixed by a '/' (%x2F)
character. Each reference token is a sequence of unreserved or
percent-encoded characters.


L
~~~~

language-specific API
^^^^^^^^^^^^^^^^^^^^^^^^^

An API that provides a layer of abstraction on top of the base
REST API, enabling programmers to work with a container and object
model instead of working directly with HTTP requests and responses.

launch configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* A configuration that contains the necessary details
for adding and removing servers from a `scaling group`_ in the
Rackspace Auto Scale API. The `launchConfiguration` object specifies
whether you are creating a server or a load balancer and the
necessary details about the configuration.

layer-2 network
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Networks)* A virtual Ethernet network that is managed by the
Cloud Networks service. You can create isolated networks that
are virtual layer-2 networks and attach them to cloud servers.

LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^

Lightweight Directory Access Protocol. An application protocol
for accessing and maintaining distributed directory information
services over an IP network. The Rackspace Identity service
can use an LDAP back end as a datastore.

load average alarm
^^^^^^^^^^^^^^^^^^^^^^^^^

An `alarm`_ that sends a notification when your system's load
exceeds a number that you specify for greater than n number of
minutes. n is generally set for 5 minutes.

load average check
^^^^^^^^^^^^^^^^^^^^^^^^^

A `check`_ that monitors and displays your server's load average.
This option is most often used with Linux machines.

load balancer
^^^^^^^^^^^^^^^^^^^^^^^^^

A logical device that belongs to a cloud account and distributes
workloads between multiple back-end systems or services,
based on the criteria defined as part of its configuration.


M
~~~~

MapReduce
^^^^^^^^^^^^^^^^^^^^^^^^^

A framework for performing calculations on the data in a distributed
file system. Map tasks run in parallel with each other. Reduce
tasks also run in parallel with each other.

media type
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Files)* A standard identifier used on the Internet to
indicate the type of data contained in a file. A media type is
composed of a type, a subtype, and zero or more optional parameters.

memory alarm
^^^^^^^^^^^^^^^^^^^^^^^^^

An `alarm`_ that notifies you when a server's memory usage goes above
the percentage that you set in the criteria.

memory check
^^^^^^^^^^^^^^^^^^^^^^^^^

A `check`_ that monitors and displays your server's memory use (RAM)
and historical usage.

.. _message-term:

message
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* A task, a notification, or any meaningful data
that a producer or publisher sends to a queue. A message exists
until it is deleted by a recipient or automatically by the system
based on a TTL (time-to-live) value. See also `producer-consumer`_ 
and `publisher-subscriber`_.

message TTL
^^^^^^^^^^^^^^^^^^^^^^^^^

Time-to-live value that defines how long a message is accessible.

metadata
^^^^^^^^^^^^^^^^^^^^^^^^^

Optional information that you can assign to accounts and objects
through the use of a metadata header or parameter.

metric series
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Rackspace Metrics)* A named set of data points. (See `data point`_.)
A series is identified by a unique name, which is
composed of elements separated
by periods that are used to display the collection of series
in a hierarchal tree.

monitoring zone
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Monitoring)* The point of origin for a monitoring `check`_.
When you create a check, you specify the monitoring zones that it
will launch from. A monitoring zone is similar to a data center,
but you can think of it more as a geographical region. You
can launch checks for a particular entity from multiple monitoring
zones. This allows you to observe the performance of an entity
from different regions of the world. It is also a way of
adding redundancy to make the alarm less sensitive to external factors.

Mosso ID
~~~~~~~~~~~~~

See `DDI`_.


N
~~~~

network
^^^^^^^^^^^^^^^^^^^^^^^^^

An isolated virtual layer-2 broadcast domain that is typically
reserved for the tenant who created it unless the network is
configured to be shared. Tenants can create multiple networks until
they reach the thresholds specified by per-tenant quotas.

network alarm
^^^^^^^^^^^^^^^^^^^^^^^^^

An `alarm`_ that sends a notification when either the network
receive rate or the network transmit rate alarm is triggered.

network check
^^^^^^^^^^^^^^^^^^^^^^^^^

A `check`_ that monitors your network receiving and transmitting
traffic. The unit of value for this check is megabits per
second (Mbit/s). This check also displays your traffic usage.

node
^^^^^^^^^^^^^^^^^^^^^^^^^

A back-end device that provides a service on a specified IP and port.

*(Cloud Big Data)* In a network, a connection point—either a
redistribution point or an end point—for data transmissions.
In general, a node has programmed or engineered capability to
recognize and process or forward transmissions to other nodes.
A node is a member of a cluster. *See also* `edge node`_.

notification
^^^^^^^^^^^^^^^^^^^^^^^^^

An informational message sent to one or more addresses by the
monitoring system when an `alarm`_ is triggered. You can set up
notifications to alert a single individual or an entire team.
Notification types include `webhook`_, email, and SMS.

notification plan
^^^^^^^^^^^^^^^^^^^^^^^^^

A plan that defines a set of notification rules to execute when an `alarm`_ is triggered. 
A notification plan can contain more than one `notification`_ for each of the
following states: Critical, Warning, OK.

O
~~~~

operations
^^^^^^^^^^^^^^^^^^^^^^^^^

The HTTP actions that you perform against your account by using the
REST API for a Rackspace service.

origin
^^^^^^^^^^^^^^^^^^^^^^^^^

An address (IP or domain) from which the CDN provider pulls
content. A service can have multiple origins.


P
~~~~

PoP
^^^^^^^^^^^^^^^^^^^^^^^^^

Point of Presence. The point at which two or more different
networks or communication devices connect. PoP mainly refers to an
access point, location, or facility that connects to and helps
other devices establish a connection with the Internet. CDN
providers have many PoP servers around the world, which cache
content and serve it directly to customers.

port
^^^^^^^^^^^^^^^^^^^^^^^^^

In computer networking, a port is a software construct serving
as a communications endpoint in a computer’s host operating system.
A port is always associated with an IP address of a host and
the protocol type of the communication. It completes the
destination or origination address of a communications session.
A port is identified for each address and protocol by a
16-bit number, commonly known as the port number.

policy
~~~~~~~~~~

*(Cloud Identity)* A structured data format that contains a subject (user, group, role) 
and the capabilities they can access. 

policy service
~~~~~~~~~~~~~~~~~~~

*(Cloud Identity)* A component of Identity that provides a rule-management interface 
and a rule-based authorization engine.


Policy-Based Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ability to setup a group of roles and/or capabilities to grant to identities.


private container
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Files)* A `container`_ that is accessible only by the account
holder. A private container is not the same as a 
:ref:`CDN-enabled container <cdn-enabled-container-term>`, and the files
in a private container are not publicly accessible.

.. _producer-term:

producer
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* A server or application that sends
messages to a `queue`_. In the `producer-consumer`_ model of messaging, producers
post messages to a queue and :ref:`consumers <consumer-term>` claim those messages.

producer-consumer
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* A messaging model in which :ref:`producers <producer-term>` 
post messages to a `queue`_ and
:ref:`consumers <consumer-term>` (workers) claim the messages in
order to prevent duplicate processing. Later, when work is done,
the consumer is responsible for deleting the message. If message
is not deleted in a predefined time, it can be claimed by other
consumers.

pseudo directories
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Files)* A simulated hierarchical structure within a Cloud
Files `container`_ that is created by adding a slash (/) in the object
name. Pseudo directories are used because directories cannot
be nested in a container.

public container
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Files)* A :ref:`CDN-enabled container <cdn-enabled-container-term>` that is 
publicly accessible.

public URL
^^^^^^^^^^^^^^^^^^^^^^^^^

A URL that is accessible from anywhere. Access to a public URL
usually incurs traffic charges.

PublicNet
^^^^^^^^^^^^^^^^^^^^^^^^^

A network interface that provides access to the Internet for
Rackspace services such as Cloud Monitoring, RackConnect, Cloud
Backup, and certain operating system updates. When you list
networks through Cloud Networks, PublicNet is labeled public.

publisher
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* A server or application that posts
:ref:`messages <message-term>` to a `queue`_ with the intent
to distribute information or updates to multiple
:ref:`subscribers <subscriber-term>`.
*See also* :`publisher-subscriber`_.

publisher-subscriber
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* A messaging model in which all worker
applications (:ref:`subscribers <subscriber-term>`) have access to all
:ref:`messages <message-term>` in the
`queue`_. Workers cannot delete or update messages.

purge
^^^^^^^^^^^^^^^^^^^^^^^^^

To remove content from CDN :ref:`edge nodes <edge-node-term>`,
which allows the content
to be refreshed from the origin server.


Q
~~~~

queue
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Queues)* The entity that holds :ref:`messages <message-term>`.
Ideally, a queue is
created per work type. For example, if you want to compress
files, you would create a queue dedicated to this job. Any
application that reads from this queue would only compress files.
*See also* `producer-consumer`_ and `publisher-subscriber`_.

R
~~~~

Rate limiting

Used to control the rate of traffic sent or received by a network interface controller.


.. _rbac-term:

RBAC
^^^^^^^^^^^^^^^^^^^^^^^^^

Role Based Access Control. A method for restricting service access
to only authorized users. RBAC allows customers to specify who
has access to resources and capabilities within their cloud
deployment, based on roles defined by Rackspace.

reboot
^^^^^^^^^^^^^^^^^^^^^^^^^

A soft or hard reboot of a server. A soft reboot is a graceful
shutdown and restart of your server's operating system. A hard
reboot power cycles your server, which performs an immediate shutdown
and restart.

rebuild
^^^^^^^^^^^^^^^^^^^^^^^^^

To remove all data on the server and replace it with the specified
`image`_. The server ID and IP addresses on the server remain the same.

replica
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Databases)* An exact copy of a `database instance`_ that is
kept synchronized with its database instance source.

resize
^^^^^^^^^^^^^^^^^^^^^^^^^

To convert an existing server to a different flavor, which scales
the server up or down. The original server is saved for a period
of time to allow rollback if a problem occurs. You can confirm
or revert a resize. A confirmed resize removes the original server,
while a reverted resize restores the original server. All
resizes are automatically confirmed after 24 hours if you do not
explicitly confirm or revert them.

resolution
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Rackspace Metrics)* The number of seconds per `data point`_ in a
`metric series`_. Series are created with a resolution, which determines
how often a data point can be stored. A series that stores one
data point per minute has a resolution of 60 seconds. Similarly,
a series that stores one data point per second has a resolution
of 1 second.

*(Cloud Monitoring)* [Need definition here; see Cloud Monitoring guide]

resource
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Orchestration)* A template artifact that represents some
component of your desired architecture, such as a cloud server, a
group of scaled cloud servers, a load balancer, or some
configuration management system.

resource group
~~~~~~~~~~~~~~~~~~~

*(Cloud Identity)* A group of resources that can be attached to a policy to limit access (the implementation 
method for `fine grained access control`_).

REST
^^^^^^^^^^^^^^^^^^^^^^^^^

Representational State Transfer. An architectural style for
large-scale software design.

RESTful
^^^^^^^^^^^^^^^^^^^^^^^^^

A kind of web service API that uses REST. RESTful APIs communicate
over HTTP with the same HTTP verbs (GET, POST, PUT, DELETE, and so on)
that web browsers use to retrieve web pages and to send data to
remote servers. Rackspace service APIs are RESTful.

restore
^^^^^^^^^^^^^^^^^^^^^^^^^

The process of bringing your system back to a previously saved
state, usually by using a backup as the checkpoint.

restore configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

Definition that describes the restore checkpoint and the where the
backup should be restored.

restriction
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Rackspace CDN)* Specification that enables you to define rules
about who can or cannot access content from the cache. An example
of a restriction is allowing requests only from certain domains
based on `HTTP Referrer` headers.

role
^^^^^^^^^^^^^^^^^^^^^^^^^

A common security construct for assigning a specific set of
access rights and privileges to a user or group of users. Service
administrators can create named roles, configure the rights
and privileges for each role, and manage the role without updating
individual user or group accounts assigned to the role. Rackspace
uses :ref:`Role Based Access Control <rbac-term>` (RBAC) to
control permissions.

Role Based Access Control
^^^^^^^^^^^^^^^^^^^^^^^^^

*See* `RBAC`_.

rollup
^^^^^^^^^^^^^^^^^^^^^^^^^

To perform functions on a set of data that has been ingested,
such as downsampling calculations and summarizing raw data to
condense the size of the original data sample.

G
~~~~


SAML assertion
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Identity)* Security Assertion Markup Language assertion.
A package of user security information that can be transferred
from identity providers to service providers to validate
authentication and authorization rights. The service provider uses
this information to make access-control decisions. The Rackspace
Cloud Identity service uses SAML assertions to provide authentication
tokens to federated users.

scaling
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* The process of adjusting a server configuration in
response to variations in workload.

scaling group
^^^^^^^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* A group of servers and load balancers that are
managed by a `scaling policy`_.

.. _scaling-policy-term:

scaling policy
^^^^^^^^^^^^^^^^^^^

*(Auto Scale)* A policy that manages a `scaling group`_.

schema
^^^^^^^^^^^^^^^^^^^

Documents that describe the JSON-encoded data structures that
represent domain objects. Rackspace APIs supply JSON schema so that
a client knows exactly what to expect in an API response.

SCP server proxy
^^^^^^^^^^^^^^^^^^^

*(Cloud Big Data)* An SCP service that runs on your Hadoop cluster
and distributes your files across the cluster.

segmentation
^^^^^^^^^^^^^

*(Cloud Files)* The process of segmenting a large file into a
number of smaller files for uploading to Cloud Files. The default
size limit of a single uploaded object is 5 GB; however, the
download size of a single object is virtually unlimited with the
use of segmentation. Segments of the larger object are uploaded
and a special manifest file is created that, when downloaded,
sends all the segments concatenated as a single object. Segmentation
also offers much greater upload speed with the possibility of
parallel uploads of the segments.

server
^^^^^^^^^^^^^

A computer that provides explicit services to the client software
running on that system. A server is a virtual machine (VM)
instance in the Cloud Servers environment. To create a server,
you must specify a name, flavor reference, and image reference.

service
^^^^^^^^^^^^^

A logical name for the internal and external capabilities provided
on a Cloud platform or product component. A service provides
one or more endpoints through which users can access resources
and perform operations.

service catalog
^^^^^^^^^^^^^^^^^^

The list of services available to you, returned with your
`authentication token`_ and an expiration date for that token. All
the services in your service catalog should recognize your token
as valid until it expires. The catalog list for each
service provides at least one endpoint URL for that service.
Other information—such as regions, versions, and tenants—is
provided if it is relevant to your access to this service.

ServiceNet
^^^^^^^^^^^^^

A network interface that provides access to Rackspace services,
such as Cloud Files, Cloud Databases, and Cloud Backup, and to
certain packages and patches through an internal-only, multi-tenant
network connection within each Rackspace data center. When
you list networks, ServiceNet is labeled as private.

session persistence
^^^^^^^^^^^^^^^^^^^^^^

*(Cloud Load Balancers)* A feature of the load balancing service
that attempts to force subsequent connections to a service to be
redirected to the same node as long as the node is online.

shared IP address
^^^^^^^^^^^^^^^^^^^^^

A public `IP address`_ that can be shared across multiple servers
for use in various high-availability scenarios. When an IP address
is shared with another server, the cloud network restrictions
are modified to allow each server to listen to and respond on that
IP address. You can also specify that the target server network
configuration be modified.

snapshot
^^^^^^^^^^^

A point-in-time copy of the data contained in a volume.

stack
^^^^^^^^^^^

*(Cloud Orchestration)* A group of resources, such as servers,
load balancers, and databases, combined to fulfill a useful purpose.
Based on a `template`_, the Cloud Orchestration engine creates an
instantiated set of resources (a stack) to run the application
framework or component specified (in the template).

subdomain
^^^^^^^^^^^

*(Cloud DNS)* A `domain`_ within a parent domain that cannot be
registered. Subdomains enable you to delegate domains. Subdomains
can themselves have subdomains, so third-level, fourth-level,
fifth-level, and deeper levels of nesting are possible.

subnet
^^^^^^^^^^^

An `IP address`_ block that can be used to assign IP addresses to
virtual instances. Each subnet must have a CIDR and be associated
with a network. IP addresses can be selected either from the
whole subnet CIDR or from allocation pools that can be specified
by the user.

.. _subscriber-term:

subscriber
^^^^^^^^^^^

*(Cloud Queues)* An observer that watches :ref:`messages <message-term>`
like an RSS feed but does not claim any messages. In a
`publisher-subscriber`_.
messaging model, all worker applications (subscribers) have
access to all messages in the queue.

template
^^^^^^^^^^^

*(Cloud Orchestration)* A portable file, written in a user-readable
language, that describes how a set of resources should be
assembled and what software should be installed to produce a
working `stack`_. The template specifies what resources should be
used, what attributes can be set, and other parameters that are
critical to the successful, repeatable automation of a
specific application stack.

tenant
^^^^^^^^^^^

A container used to group or isolate resources or identity
objects. Depending on the service operator, a tenant could map
to a customer, account, organization, or project.

token
^^^^^^^^^^^

*See* `authentication token`_.

TTL
^^^^^^^^^^^
Time-to-live value.

URI
^^^^^^^^^^^

Uniform Resource Identifier. A string of characters used to
identify the name of a web resource. The URI syntax consists of
a URI scheme name (such as http, ftp, or file) followed by a
colon character, and then by a scheme-specific part
(which varies depending on the context).

user
^^^^^^^^^^^

A digital representation of a person, system, or service that uses
cloud services. Users have `credentials`_ and can be assigned
:ref:`tokens <authentication-token-term>`. They can present this
information to the Identity
service or other cloud services to confirm identity and verify
permission to access the requested system resources.

Keystone is used to define users. Users are accounts for specific individuals, and 
typically have a password and email associated with them. Keystone allows you to list, 
create, delete, enable/disable, update email addresses, and change passwords of Users.

UUID
^^^^^^^^^^

Universal Unique Identifier. A 128-bit that is used to uniquely
identify an object on the Internet.

virtual IP address
^^^^^^^^^^^^^^^^^^^^^^
An Internet Protocol address (`IP address`_) configured
on the load
balancer for use by clients connecting to a service that is load
balanced. Incoming connections are distributed to back-end
nodes based on the configuration of the load balancer.

V
~~~~

volume
^^^^^^^^^^^

*(Cloud Block Storage)* A detachable block storage device. A volume
can be attached to only one instance at a time.

*(Cloud Databases)* User-specified storage that contains the
database engine data directory. Volumes are automatically
provisioned on shared Internet Small Computer System Interface
(iSCSI) storage area networks (SAN) that provide for increased
performance, scalability, availability, and manageability.
Applications with high I/O demands are performance optimized and
data is protected through both local and network RAID-10.
Additionally, network RAID provides synchronous replication of
volumes with automatic failover and load balancing across
available storage clusters.

volume type
*(Cloud Block Storage)* The type of a block storage `volume`_. There
are two types: SATA for standard performance and SSD for
high performance.

W
~~~~~~

webhook
^^^^^^^^^^^

*(Auto Scale)* An industry-standard protocol for sending events
between systems. For Auto Scale, they are used to execute
:ref:`scaling policies <scaling-policy-term>`. A
webhook consists of an HTTP callback that
is triggered by some user-defined event, such as an alarm that
is set through Cloud Monitoring or another monitoring service.
When that event occurs, the source site makes an HTTP request
to the URI configured for the webhook.

worker
^^^^^^^^^^^

*(Cloud Queues)* A client that gets messages from a queue and
performs actions based on those messages. *See also*
`producer-consumer`_ and `publisher-subscriber`_.
