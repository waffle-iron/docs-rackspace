===================================================
How-To: OpenStack on Rackspace Ubuntu Cloud Servers
===================================================

This how-to provides instructions for building the prerequisite
infrastructure for installing multi-host OpenStack environments on Rackspace
cloud servers using the official OpenStack installation guide.

The infrastructure contains two OpenStack nodes operating on private
(tenant) networks managed by a network services (jump/firewall) node.
The latter protects the OpenStack nodes from direct internet access and
provides internet connectivity to instances in the environment.

Overview
~~~~~~~~

-  Prepare the Rackspace cloud environment.
-  Build and configure the network services (jump/firewall) node.
-  Build and configure OpenStack nodes.
-  Install and configure OpenStack services with minor modifications to
   the official installation guide.

Network architecture
~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/openstack-rax-on-cloud-arch-v2.png
   :alt: Network architecture

   Network architecture

Prepare cloud environment
~~~~~~~~~~~~~~~~~~~~~~~~~

Keys
----

Upload a public key.

Networks
--------

In the Rackspace Cloud Control Panel, select :guilabel:`Networks` in the
:guilabel:`Networking` tab, and create the following networks:

#. net-osmgmt1

   -  10.1.11.0/24

#. net-osint1

   -  10.1.12.0/24

#. net-osext1

   -  10.1.13.0/24

Launch servers
~~~~~~~~~~~~~~

Network services node (network-services)
----------------------------------------

#. Create a cloud server.

   OS: Ubuntu 16.04 (Xenial Xerus) PVHVM
   Flavor: 1 GB General Purpose v1
   Networks: PublicNet, ServiceNet

   .. note::

      Adding multiple tenant networks simultaneously yields inconsistent
      network interface device names. This guide adds one tenant network at a
      time as it becomes necessary. Also, changing tenant networks after
      configuration erases changes made in this guide.

#. Access the node from the internet using the IP address assigned by
   Rackspace.

   .. code-block:: console

      ssh root@<hst-ns1_IP_ADDRESS>

#. Update node.

   .. code-block:: console

      apt-get update && apt-get dist-upgrade

#. Install additional packages.

   .. code-block:: console

      apt-get install ntp shorewall

#.  Reboot node.

#.  Add the *net-osmgmt1* network to node.

#.  Add the *net-osext1* network to node.

#.  Configure additional network interfaces.

#.  Edit the :file:`/etc/network/interfaces` file.

    .. code-block:: text

       # Label net-osmgmt1
       auto eth2
       iface eth2 inet static
       address 10.1.11.1
       netmask 255.255.255.

       # Label net-osext1
       auto eth3
       iface eth3 inet static
       address 10.1.10.1
       netmask 255.255.255.0

       # Label vxlan1
       auto vxlan1
       iface vxlan1 inet static
       pre-up ip link add vxlan1 type vxlan id 1 group 239.0.0.1 dev eth3
       address 10.1.13.1
       netmask 255.255.255.0
       post-down ip link del vxlan1

#.  Restart the network interfaces.

    .. code-block:: console

       ifdown eth2 && ifup eth2
       ifdown eth3 && ifup eth3

#.  Bring up the vxlan1 interface.

    .. code-block:: console

       ifup vxlan1

#.  Configure the firewall service.

#.  Edit the :file:`/etc/shorewall/shorewall.conf` file.

    .. code-block:: ini

       IP_FORWARDING=On

#. Create a :file:`/etc/shorewall/interfaces` file.

   .. code-block:: text

      ext eth0 - routefilter,tcpflags
      rax eth1
      osm1 eth2
      ose1 eth3
      os1t vxlan1

#. Create a :file:`/etc/shorewall/masq` file.

   .. code-block:: text

      eth0 10.1.11.0/24
      eth0 10.1.13.0/24

#. Create a :file:`/etc/shorewall/policy` file.

   .. code-block:: text

      $FW all ACCEPT
      ext all REJECT
      rax all ACCEPT
      osm1 all ACCEPT
      ose1 all ACCEPT
      os1t all ACCEPT

#. Create a :file:`/etc/shorewall/rules` file.

   .. code-block:: text

      Ping/ACCEPT ext $FW
      SSH/ACCEPT ext $FW
      #DNAT ext osm1:10.1.11.11  tcp    www
      #DNAT ext osm1:10.1.11.11  tcp    6080

   .. note::

      Uncomment the DNAT rules and restart Shorewall as necessary to
      enable remote access to the dashboard and instance consoles in the
      OpenStack environment.

#. Create a :file:`/etc/shorewall/zones` file.

   .. code-block:: text

      fw firewall
      ext ipv4
      rax ipv4
      osm1 ipv4
      ose1 ipv4
      os1t ipv4

#. Edit the :file:`/etc/default/shorewall` file.

   .. code-block:: ini

      startup=1

#. Check the shorewall configuration.

   .. code-block:: console

      # shorewall check

#. Start the firewall service.

   .. code-block:: console

      # service shorewall start

   .. note::

      Restart the firewall service whenever the network services
      node is rebooted.

#. Test network connectivity to the internet by pinging openstack.org:

   .. code-block:: console

      # ping openstack.org
      PING openstack.org (162.242.140.107) 56(84) bytes of data.
      64 bytes from 162.242.140.107: icmp_seq=1 ttl=50 time=181 ms
      64 bytes from 162.242.140.107: icmp_seq=2 ttl=50 time=180 ms
      ...

#. Generate an ssh key for accessing other nodes:

   .. code-block:: console

      # ssh-keygen -t rsa -b 2048 -C "ns1" -P "" -f .ssh/id_rsa

OpenStack controller node (controller)
---------------------------------------

#. Create a cloud server, removing all networks except the *net-osmgmt1*
   network:

   OS: Ubuntu 16.04 (Xenial Xerus) PVHVM
   Flavor: 4 GB General Purpose v1
   Network: net-osmgmt1

#. Access the node from the network services node (network-services) using the
   IP address assigned by Rackspace on the *net-osmgmt1* network:

   .. code-block:: console

      # ssh-copy-id -i .ssh/id_rsa.pub root@<controller_IP_ADDRESS>
      # ssh root@<controller_IP_ADDRESS>

   .. note::

      The node cannot access the internet without additional
      configuration.

#.  In the cloud control panel, add the *net-osint1* network to the
    node.

#.  In the cloud control panel, add the *net-osext1* network to the
    node.

#.  Configure network interfaces.

#.  Edit the :file:`/etc/network/interfaces` file.

   .. code-block:: text

      # Label net-osmgmt1
      auto eth0
      iface eth0 inet static
          address 10.1.11.11
          netmask 255.255.255.0
          gateway 10.1.11.1
          dns-nameserver 72.3.128.241 72.3.128.240

      # Label net-osint1
      auto eth1
      iface eth1 inet static
          address 10.1.12.21
          netmask 255.255.255.0

      # Label net-osext1
      auto eth2
      iface eth2 inet static
          address 10.1.10.21
          netmask 255.255.255.0

      # Label vxlan1
      auto vxlan1
      iface vxlan1 inet static
          pre-up ip link add vxlan1 type vxlan id 1 group 239.0.0.1 dev eth2
          address 10.1.13.21
          netmask 255.255.255.0
          post-down ip link del vxlan1

#.  Edit the :file:`/etc/hosts` file.

    .. code-block:: text

       # controller
       10.1.11.11 controller

       # compute
       10.1.11.21 compute

       .. note::

         Comment out or remove any existing lines containing
         *controller*.

#.  Reboot the node.

#.  Access the node from the network services node using the new IP
    address on the *net-osmgmt1* network.

    .. code-block:: console

       ssh root@10.1.11.11

#.  Test network connectivity to the internet. For example:

    .. code-block:: console

       ping -c 4 openstack.org

#.  Update the node.

    .. code-block:: console

       apt-get update && apt-get dist-upgrade

#. Reboot the node.

OpenStack compute node (compute)
------------------------------------

#. Create a cloud server, removing all networks except the *net-osmgmt1*
   network:

   OS: Ubuntu 16.04 (Xenial Xerus) PVHVM
   Flavor:
   * 3.75 GB Compute v1 (supports several CirrOS instances)
   * 7.5 GB Compute v1 (supports a couple of Ubuntu/Fedora instances)
   Network: net-osmgmt1

#. Access the node from the network services node (network-services) using the
   IP address assigned by RAX on *net-osmgmt1* network.

   .. code-block:: console

      # ssh-copy-id -i .ssh/id_rsa.pub root@<compute_IP_ADDRESS>
      # ssh root@<compute_IP_ADDRESS>

   .. note::

      The node cannot access the internet without additional
      configuration.

#. Add the *net-osint1* network to the node.

#. Configure network interfaces.

#. Edit the :file:`/etc/network/interfaces` file.

   .. code-block:: text

      # Label net-osmgmt1
      auto eth0
      iface eth0 inet static
          address 10.1.11.21
          netmask 255.255.255.0
          gateway 10.1.11.1
          dns-nameserver 72.3.128.241 72.3.128.240

      # Label net-osint1
      auto eth1
      iface eth1 inet static
          address 10.1.12.31
          netmask 255.255.255.0

#. Edit the :file:`/etc/hosts` file.

   .. code-block:: text

      # hst-os1ctl1
      10.1.11.11 controller

      # compute
      10.1.11.21 compute

   .. note::

      Comment out or remove any existing lines containing
      *compute*.

#. Reboot the node.

#. Access the node from the network services node using the new IP
   address on the *net-osmgmt1* network.

   .. code-block:: console

      ssh root@10.1.11.21

#. Test network connectivity to the internet. For example:

   .. code-block:: console

      ping -c 4 openstack.org

#. Update the node.

   .. code-block:: console

      apt-get update && apt-get dist-upgrade

#. Reboot the node.

Install and configure OpenStack services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the `installation
guides <http://docs.openstack.org/project-install-guide/draft/>`_ with
the following changes:

- Configuring the basic environment on all nodes:

  -  Skip the network configuration sections.

  -  Use 10.1.11.1 (network services node) as the NTP server.

- Configuring the Compute service on the compute node:

  -  Use *qemu* instead of *kvm* virtualization.

- Configuring the Networking service on the network node:

  -  Add the *vxlan1* interface as a port on the *br-ex* bridge.

- Creating initial networks.

  - Use the following command for the subnet on the external network:

    .. code-block:: console

       neutron subnet-create ext-net --name ext-subnet \
       --allocation-pool start=10.1.13.101,end=10.1.13.200 \
       --disable-dhcp --gateway 10.1.13.1 10.1.13.0/24

  .. note::

     After performing the initial tenant network creation procedure,
     try pinging 10.1.13.101 from the network services node.

