======================================
How-To: OpenStack on RAX Cloud Servers
======================================

This how-to provides instructions for building the prerequisite
infrastructure for installing multi-host OpenStack environments on RAX
cloud servers using the official installation guide.

The infrastructure contains three OpenStack nodes operating on private
(tenant) networks managed by a network services (jump/firewall) node.
The latter protects the OpenStack nodes from direct internet access and
provides internet connectivity to instances in the environment.

Overview
~~~~~~~~

-  Prepare RAX cloud environment.
-  Build and configure network services (jump/firewall) node.
-  Build and configure OpenStack nodes.
-  Install and configure OpenStack services with minor modifications to
   the official installation guide.

Network architecture
~~~~~~~~~~~~~~~~~~~~

.. figure:: figures/openstack-on-rax-cloud-arch.png
   :alt: Network architecture


Prepare cloud environment
~~~~~~~~~~~~~~~~~~~~~~~~~

**Keys**

-  Upload a public key.

**Networks**

Create the following networks:

#. net-osmgmt1

   -  10.1.11.0/24

#. net-osint1

   -  10.1.12.0/24

#. net-osext1

   -  10.1.13.0/24

Launch servers
~~~~~~~~~~~~~~

Network services node (hst-ns1)
-------------------------------

#. Launch node.

   OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
   Flavor: 1 GB Performance 1
   Networks: PublicNet, ServiceNet, net-osmgmt1

   .. note::

      Adding multiple tenant networks simultaneously yields inconsistent
      network interface device names. This guide adds one tenant network at a
      time as it becomes necessary. Also, changing tenant networks after
      configuration erases changes made in this guide.

#. Access the node from the internet using the IP address assigned by
   RAX.

#. Update node.

   .. code::

      apt-get update && apt-get dist-upgrade

#. Install additional packages.

   .. code::

      apt-get install ntp shorewall

#.  Reboot node.

#.  Add the *net-osmgmt1* network to node.

#.  Add the *net-osext1* network to node.

#.  Configure addtional network interfaces.

#.  Edit the /etc/network/interfaces file.

    .. code::

        # Label net-osmgmt1
        auto eth2
        iface eth2 inet static
            address 10.1.11.1
            netmask 255.255.255.0

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

    .. code::

       ifdown eth2 && ifup eth2
       ifdown eth3 && ifup eth3

#.  Bring up the vxlan1 interface.

    .. code::

       ifup vxlan1

#.  Configure the firewall service.

#.  Edit the /etc/shorewall/shorewall.conf file.

    .. code::

       IP_FORWARDING=Yes

#. Edit the /etc/shorewall/interfaces file.

   .. code::

        ext eth0 - routefilter,tcpflags
        rax eth1
        osm1 eth2
        ose1 eth3
        os1t vxlan1

#. Edit the /etc/shorewall/masq file.

   .. code::

        eth0 10.1.11.0/24
        eth0 10.1.13.0/24

#. Edit the /etc/shorewall/policy file.

   .. code::

        $FW all ACCEPT
        ext all REJECT
        rax all ACCEPT
        osm1 all ACCEPT
        ose1 all ACCEPT
        os1t all ACCEPT

#. Edit the /etc/shorewall/rules file.

   .. code::

        Ping/ACCEPT ext $FW
        SSH/ACCEPT ext $FW
        #DNAT ext osm1:10.1.11.11  tcp    www
        #DNAT ext osm1:10.1.11.11  tcp    6080

    .. note::

       Uncomment the DNAT rules and restart Shorewall as necessary to
       enable remote access to the dashboard and instance consoles in the
       OpenStack environment.

#. Edit the /etc/shorewall/zones file.

   .. code::

        fw firewall
        ext ipv4
        rax ipv4
        osm1 ipv4
        ose1 ipv4
        os1t ipv4

#. Edit the /etc/default/shorewall file.

   .. code::

      startup=1

#. Start the firewall service.

   .. code::

      service shorewall start

OpenStack controller node (hst-os1ctl1)
---------------------------------------

#. Launch node

   OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
   Flavor: 4 GB Performance 1
   Networks: net-osmgmt1

#. Access the node from the network services node using the IP address
   assigned by RAX.

   .. note::

      The node cannot access the internet without additional
      configuration.

#. Configure network interfaces.

#. Edit the /etc/network/interfaces file.

   .. code::

       # Label net-osmgmt1
       auto eth0
       iface eth0 inet static
           address 10.1.11.11
           netmask 255.255.255.0
           gateway 10.1.11.1
           dns-nameserver 72.3.128.241 72.3.128.240

#. Edit the /etc/hosts file.

   .. code::

       # hst-os1ctl1
       10.1.11.11  hst-os1ctl1

       # hst-os1net1
       10.1.11.21  hst-os1net1

       # hst-os1cpu1
       10.1.11.31  hst-os1cpu1

   .. note:: Comment out or remove any existing lines containing *hst-os1ctl1*.

#. Reboot node.

#. Access the node from the network services node using the new IP
   address on the *net-osmgmt1* network.

#. Test network connectivity to the internet.

#. Update node.

   .. code::

      apt-get update && apt-get dist-upgrade

#. Reboot node.

OpenStack network node (hst-os1net1)
------------------------------------

#. Launch node.

   OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
   Flavor: 1 GB Performance 1
   Networks: net-osmgmt1

#. Access the node from the network services node using the IP address
   assigned by RAX.

   .. note::

      The node cannot access the internet without additional
      configuration.

#.  Add the *net-osint1* network to node.

#.  Add the *net-osext1* network to node.

#.  Configure network interfaces.

#.  Edit the /etc/network/interfaces file.

    .. code::

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

#.  Edit the /etc/hosts file.

    .. code::

        # hst-os1ctl1
        10.1.11.11  hst-os1ctl1

        # hst-os1net1
        10.1.11.21  hst-os1net1

        # hst-os1cpu1
        10.1.11.31  hst-os1cpu1

    .. note::

       Comment out or remove any existing lines containing *hst-os1net1*.

#.  Reboot node.

#.  Access the node from the network services node using the new IP
    address on the *net-osmgmt1* network.

#.  Test network connectivity to the internet.

#.  Update node.

    .. code::

       apt-get update && apt-get dist-upgrade

#. Reboot node.

OpenStack compute node (hst-os1cpu1)
------------------------------------

#. Launch the node.

   OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
   Flavor:
   2 GB Performance 1 (supports several CirrOS instances)
   4 or 8 GB Performance 1 (supports a couple of Ubuntu/Fedora instances)

Networks: net-osmgmt1

#. Access the node from the network services node using the IP address
   assigned by RAX.

   .. note::

      The node cannot access the internet without additional configuration.

#. Add the *net-osint1* network to node.

#. Configure network interfaces.

#. Edit the /etc/network/interfaces file.

   .. code::

       # Label net-osmgmt1
       auto eth0
       iface eth0 inet static
           address 10.1.11.31
           netmask 255.255.255.0
           gateway 10.1.11.1
           dns-nameserver 72.3.128.241 72.3.128.240

       # Label net-osint1
       auto eth1
       iface eth1 inet static
           address 10.1.12.31
           netmask 255.255.255.0

#. Edit the /etc/hosts file.

   .. code::

       # hst-os1ctl1
       10.1.11.11  hst-os1ctl1

       # hst-os1net1
       10.1.11.21  hst-os1net1

       # hst-os1cpu1
       10.1.11.31  hst-os1cpu1

   .. note::

      Comment out or remove any existing lines containing *hst-os1cpu1*.

#. Reboot node.

#. Access the node from the network services node using the new IP
   address on the *net-osmgmt1* network.

#. Test network connectivity to the internet.

#. Update node.

   .. code::

      apt-get update && apt-get dist-upgrade

#. Reboot node.

Install and configure OpenStack services
----------------------------------------

#. Use the `OpenStack Installation Guide
   <http://docs.openstack.org/juno/install-guide/install/apt/content/>`_
   with the following changes:

#. Configuring the basic environment on all nodes:

   -  Skip the network configuration sections.
   -  Use 10.1.11.1 (network services node) as the NTP server.

#. Configuring the Compute service on the compute node:

   -  Use *qemu* instead of *kvm* virtualization.

#. Configuring the Networking service on the network node:

   -  Add the *vxlan1* interface as a port on the *br-ex* bridge.

#. Creating initial networks.

   -  Use the following command for the subnet on the external network:

   .. code::

       neutron subnet-create ext-net --name ext-subnet \
       --allocation-pool start=10.1.13.101,end=10.1.13.200 \
       --disable-dhcp --gateway 10.1.13.1 10.1.13.0/24

   .. note::

      After performing the initial tenant network creation procedure,
      try pinging 10.1.13.101 from the network services node.
