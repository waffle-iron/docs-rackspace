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

#. Launch node:

   -  OS: Fedora 21 PVHVM
   -  Flavor: 1 GB Performance 1
   -  Networks: PublicNet, ServiceNet

   .. note::

      Adding multiple tenant networks simultaneously yields inconsistent
      network interface device names. This guide adds one tenant network at a
      time as it becomes necessary. Also, changing tenant networks after
      configuration erases changes made in this guide.

#. Access the node using the IP address assigned by RAX:

   .. code::

      # ssh root@119.9.24.240

#. Update node.

   .. code::

     # yum update -y

#. Install additional packages.

   .. code::

      # yum install ntp shorewall -y

#. Reboot the node:

   .. code::

      # reboot now

#.  Add the *net-osmgmt1* network to the node.

#.  Add the *net-osext1* network to the node.

#.  Configure additional network interfaces.

#.  Shut down **eth2**:

    .. code::

       # ifdown eth2

#. Edit */etc/sysconfig/network-scripts/ifcfg-eth2*. Do not touch the
   HWADDR line, as this is determined by the system:

   .. code::

        # Label net-osmgmt1
        DEVICE=eth2
        BOOTPROTO=static
        HWADDR=bc:76:4e:18:03:b8
        IPADDR=10.1.11.1
        NETMASK=255.255.255.0
        ONBOOT=yes
        NM_CONTROLLED=no

#. Bring up **eth2**:

   .. code::

      # ifup eth2

#.  Shut down **eth3**:

    .. code::

       # ifdown eth3

#. Edit */etc/sysconfig/network-scripts/ifcfg-eth3*. Do not touch the
   HWADDR line, as this is determined by the system:

   .. code::

        # Label net-osext1
        DEVICE=eth3
        BOOTPROTO=static
        HWADDR=bc:76:4e:18:03:c2
        IPADDR=10.1.10.1
        NETMASK=255.255.255.0
        ONBOOT=yes
        NM_CONTROLLED=no

#. Bring up **eth3**:

   .. code::

      # ifup eth3

#.  Create *~/vxlan1.sh* with the following content:

    .. code::

        #!/bin/bash

        modprobe vxlan
        ip link add vxlan1 type vxlan id 1 group 239.0.0.1 dev eth3 dstport 4789
        ip addr add 10.1.13.1/24 brd 10.1.13.255 dev vxlan1

#.  Run the *vxlan1.sh* script:

    .. code::

       # bash -x ~/vxlan1.sh

    This script needs to be run every time the node boots.

#.  Configure the firewall service.

#.  Set the following options in the */etc/shorewall/shorewall.conf* file:

    .. code::

        STARTUP_ENABLED=Yes
        ...
        IP_FORWARDING=On

#. Edit the */etc/shorewall/interfaces* file:

   .. code::

        ext eth0 routefilter,tcpflags
        rax eth1
        osm1 eth2
        ose1 eth3
        os1t vxlan1

#. Edit the */etc/shorewall/masq* file:

   .. code::

        eth0 10.1.11.0/24
        eth0 10.1.13.0/24

#. Edit the */etc/shorewall/policy* file:

   .. code::

        $FW all ACCEPT
        ext all REJECT
        rax all ACCEPT
        osm1 all ACCEPT
        ose1 all ACCEPT
        os1t all ACCEPT

#. Edit the */etc/shorewall/rules* file:

   .. code::

        Ping/ACCEPT ext $FW
        SSH/ACCEPT ext $FW
        #DNAT ext osm1:10.1.11.11  tcp    www
        #DNAT ext osm1:10.1.11.11  tcp    6080

   .. note::

      Uncomment the DNAT rules and restart Shorewall as necessary to
      enable remote access to the dashboard and instance consoles in the
      OpenStack environment.

#. Edit the */etc/shorewall/zones* file:

   .. code::

        fw firewall
        ext ipv4
        rax ipv4
        osm1 ipv4
        ose1 ipv4
        os1t ipv4

#. Start the firewall service:

   .. code::

      service shorewall start

#. Edit */etc/resolv.conf* and add the Google DNS servers:

   .. code::

        nameserver 8.8.8.8
        nameserver 8.8.4.4

#. Test network connectivity to the internet by pinging openstack.org:

   .. code::

        # ping openstack.org
        PING openstack.org (162.242.140.107) 56(84) bytes of data.
        64 bytes from 162.242.140.107: icmp_seq=1 ttl=50 time=181 ms
        64 bytes from 162.242.140.107: icmp_seq=2 ttl=50 time=180 ms
        ...

#. Generate an ssh key for accessing other nodes:

   .. code::

      # ssh-keygen -t rsa -b 2048 -C "ns1" -P "" -f .ssh/id_rsa

OpenStack controller node (hst-os1ctl1)
---------------------------------------

#. Launch node, removing all networks except the **net-osmgmt1**
   network:

   -  OS: Fedora 21 PVHVM
   -  Flavor: 4 GB Performance 1
   -  Networks: net-osmgmt1

#. Using the IP address and root password assigned by RAX, run the
   following commands from **hst-ns1** to access **hst-os1ctl1** using
   ssh:

   .. code::

      # ssh-copy-id -i .ssh/id_rsa.pub root@10.1.11.2    # ssh root@10.1.11.2

   .. note::

      The node cannot access the internet without additional configuration.

#. Configure network interfaces.

#. Edit */etc/sysconfig/network-scripts/ifcfg-eth0*. Do not touch the
   HWADDR line, as this is determined by the system:

   .. code::

       # Label net-osmgmt1
       DEVICE=eth0
       BOOTPROTO=static
       HWADDR=bc:76:4e:18:03:b8
       IPADDR=10.1.11.11
       NETMASK=255.255.255.0
       GATEWAY=10.1.11.1
       ONBOOT=yes
       NM_CONTROLLED=no

#. Edit the /etc/hosts file:

   .. code::

       # hst-os1ctl1
       10.1.11.11  hst-os1ctl1

       # hst-os1net1
       10.1.11.21  hst-os1net1

       # hst-os1cpu1
       10.1.11.31  hst-os1cpu1

   .. note::

      Comment out or remove any existing lines containing *hst-os1ctl1*.

#. Edit */etc/resolv.conf* and add the Google DNS servers:

   .. code::

       nameserver 8.8.8.8
       nameserver 8.8.4.4

#. Reboot the node:

   .. code::

      # reboot now

#. Access the node from the network services node using the new IP
   address on the *net-osmgmt1* network:

   .. code::

      # ssh root@10.1.11.11

#. Test network connectivity to the internet by pinging openstack.org:

   .. code::

      # ping openstack.org
      PING openstack.org (162.242.140.107) 56(84) bytes of data.
      64 bytes from 162.242.140.107: icmp_seq=1 ttl=50 time=181 ms
      64 bytes from 162.242.140.107: icmp_seq=2 ttl=50 time=180 ms
      ...

#. Update the node:

   .. code::

      yum update -y

#. Reboot the node:

   .. code::

      # reboot now

OpenStack network node (hst-os1net1)
------------------------------------

#. Launch node, removing all networks except the **net-osmgmt1**
   network:

   -  OS: Fedora 21 PVHVM
   -  Flavor: 1 GB Performance 1
   -  Networks: net-osmgmt1

#. Using the IP address and root password assigned by RAX, run the
   following commands from **hst-ns1** to access **hst-os1net1** using
   ssh:

   .. code::

      # ssh-copy-id -i .ssh/id_rsa.pub root@10.1.11.2
      # ssh root@10.1.11.2``

   .. note::

      The node cannot access the internet without additional configuration.

#.  Add the *net-osint1* network to node.

#.  Add the *net-osext1* network to node.

#.  Configure network interfaces.

#.  Edit */etc/sysconfig/network-scripts/ifcfg-eth0*. Do not touch the
    HWADDR line, as this is determined by the system:

    .. code::

        # Label net-osmgmt1
        DEVICE=eth0
        BOOTPROTO=static
        HWADDR=bc:76:4e:18:03:b8
        IPADDR=10.1.11.21
        NETMASK=255.255.255.0
        GATEWAY=10.1.11.1
        ONBOOT=yes
        NM_CONTROLLED=no

#.  Edit */etc/sysconfig/network-scripts/ifcfg-eth1*. Do not touch the
    HWADDR line, as this is determined by the system:

    .. code::

        # Label net-osint1
        DEVICE=eth1
        BOOTPROTO=static
        HWADDR=bc:76:4e:18:03:b8
        IPADDR=10.1.12.21
        NETMASK=255.255.255.0
        GATEWAY=10.1.11.1
        ONBOOT=yes
        NM_CONTROLLED=no

#.  Edit */etc/sysconfig/network-scripts/ifcfg-eth2*. Do not touch the
    HWADDR line, as this is determined by the system:

    .. code::

        # Label net-osext1
        DEVICE=eth2
        BOOTPROTO=static
        HWADDR=bc:76:4e:18:03:b8
        IPADDR=10.1.10.21
        NETMASK=255.255.255.0
        GATEWAY=10.1.11.1
        ONBOOT=yes
        NM_CONTROLLED=no

#.  Create *~/vxlan1.sh* with the following content:

    .. code::

        #!/bin/bash

        modprobe vxlan
        ip link add vxlan1 type vxlan id 1 group 239.0.0.1 dev eth2 dstport 4789
        ip addr add 10.1.13.21/24 brd 10.1.13.255 dev vxlan1

#.  Run the *vxlan1.sh* script:

    .. code::

       # bash -x ~/vxlan1.sh

    This script needs to be run every time the node boots.

#.  Edit the */etc/hosts* file:

    .. code::

        # hst-os1ctl1
        10.1.11.11  hst-os1ctl1

        # hst-os1net1
        10.1.11.21  hst-os1net1

        # hst-os1cpu1
        10.1.11.31  hst-os1cpu1

    .. note::

       Comment out or remove any existing lines containing *hst-os1net1*.

#. Edit */etc/resolv.conf* and add the Google DNS servers:

   .. code::

        nameserver 8.8.8.8
        nameserver 8.8.4.4

#. Reboot the node:

   .. code::

      # reboot now

#. Access the node from the network services node using the new IP
   address on the *net-osmgmt1* network:

   .. code::

      # ssh root@10.1.11.21

#. Test network connectivity to the internet by pinging openstack.org:

   .. code::

      # ping openstack.org
      PING openstack.org (162.242.140.107) 56(84) bytes of data.
      64 bytes from 162.242.140.107: icmp_seq=1 ttl=50 time=181 ms
      64 bytes from 162.242.140.107: icmp_seq=2 ttl=50 time=180 ms
      ...

#. Update the node:

   .. code::

      yum update -y

#. Reboot the node:

   .. code::

      # reboot now

#. Access the node from the network servies node and run the *vxlan1.sh*
   script:

   .. code::

      # ssh root@10.1.11.21
      # bash -x ~/vxlan1.sh

OpenStack compute node (hst-os1cpu1)
------------------------------------

#. Launch node, removing all networks except the **net-osmgmt1**
   network:

   - OS: Fedora 21 PVHVM
   - 2 GB Performance 1 (supports several CirrOS instances)
   - 4 or 8 GB Performance 1 (supports a couple of Ubuntu/Fedora instances)
   -  Networks: net-osmgmt1

#. Using the IP address and root password assigned by RAX, run the
   following commands from **hst-ns1** to access **hst-os1cpu1** using
   ssh:

   .. code::

      # ssh-copy-id -i .ssh/id_rsa.pub root@10.1.11.4
      # ssh root@10.1.11.4

   .. note::

      The node cannot access the internet without additional configuration.

#. Add the *net-osint1* network to the node.

#. Configure network interfaces.

#. Edit */etc/sysconfig/network-scripts/ifcfg-eth0*. Do not touch the
   HWADDR line, as this is determined by the system:

   .. code::

       # Label net-osmgmt1
       DEVICE=eth0
       BOOTPROTO=static
       HWADDR=bc:76:4e:18:03:b8
       IPADDR=10.1.11.31
       NETMASK=255.255.255.0
       GATEWAY=10.1.11.1
       ONBOOT=yes
       NM_CONTROLLED=no

#. Edit */etc/sysconfig/network-scripts/ifcfg-eth1*. Do not touch the
   HWADDR line, as this is determined by the system:

   .. code::

       # Label net-osint1
       DEVICE=eth1
       BOOTPROTO=static
       HWADDR=bc:76:4e:18:03:b8
       IPADDR=10.1.12.31
       NETMASK=255.255.255.0
       GATEWAY=10.1.11.1
       ONBOOT=yes
       NM_CONTROLLED=no

#. Edit the */etc/hosts* file:

   .. code::

       # hst-os1ctl1
       10.1.11.11  hst-os1ctl1

       # hst-os1net1
       10.1.11.21  hst-os1net1

       # hst-os1cpu1
       10.1.11.31  hst-os1cpu1

   .. note:: Comment out or remove any existing lines containing *hst-os1cpu1*.


#. Edit */etc/resolv.conf* and add the Google DNS servers:

   .. code::

       nameserver 8.8.8.8
       nameserver 8.8.4.4

#. Reboot the node:

   .. code::

      # reboot now

#. Access the node from the network services node using the new IP
   address on the *net-osmgmt1* network:

   .. code::

      # ssh root@10.1.11.31

#. Test network connectivity to the internet by pinging openstack.org:

   .. code::

      # ping openstack.org
      PING openstack.org (162.242.140.107) 56(84) bytes of data.
      64 bytes from 162.242.140.107: icmp_seq=1 ttl=50 time=181 ms
      64 bytes from 162.242.140.107: icmp_seq=2 ttl=50 time=180 ms
      ...

#. Update the node:

   .. code::

      yum update -y

#. Reboot the node:

   .. code::

      # reboot now

Install and configure OpenStack services
----------------------------------------

#. Use the `OpenStack Installation Guide <http://docs.openstack.org>`_
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
