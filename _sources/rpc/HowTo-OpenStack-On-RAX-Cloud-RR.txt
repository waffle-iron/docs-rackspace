======================================
How-To: OpenStack on RAX Cloud Servers
======================================

(Based on Matt's doc)

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

-  Upload a public key.

Networks
~~~~~~~~

Create the following networks:

Note: The CIDR you assign does not have to match the CIDR initially
assigned to a network when the network is created in the RAX cloud
control panel. You can specify any valid subnet. Multiple networks can
use the same subnet without collision.

1. robb-test-net

-  192.168.20.0/24

2. robb-vmnet

-  192.168.27.0/24

3. robb-ext1

-  192.168.33.0/24

Launch servers
~~~~~~~~~~~~~~

Jump box node (robb-dev1)
-------------------------

1. Launch node.

| OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
|  Flavor: 1 GB Performance 1
|  Networks: PublicNet, ServiceNet, robb-test-net, robb-ext1

Note: Adding multiple tenant networks simultaneously yields inconsistent
network interface device names. This guide adds one tenant network at a
time as it becomes necessary. Also, changing tenant networks after
configuration erases changes made in this guide.

1. Access the node from the internet using the IP address assigned by
   RAX.

2. Update node.

``apt-get update && apt-get dist-upgrade``

1. Install additional packages.

``apt-get install ntp shorewall``

1.  Reboot node.

2.  Add the *robb-test-net* network to node.

3.  Add the *robb-ext1* network to node.

4.  Configure addtional network interfaces.

5.  Edit the /etc/network/interfaces file.

    .. code::

        # Label robb-test-net
        auto eth3
        iface eth2 inet static
            address 192.168.20.1
            netmask 255.255.255.0

        # Label robb-ext1
        auto eth4
        iface eth3 inet static
            address 192.168.33.1
            netmask 255.255.255.0

        # Label vxlan1
        auto vxlan1
        iface vxlan1 inet static
            pre-up ip link add vxlan1 type vxlan id 1 group 239.0.0.1 dev eth3
            address 192.168.28.1
            netmask 255.255.255.0
            post-down ip link del vxlan1

6.  Restart the network interfaces.

    | ``ifdown eth3 && ifup eth3``
    | ``ifdown eth4 && ifup eth4``

7.  Bring up the vxlan1 interface.

    ``ifup vxlan1``

8.  Configure the firewall service.

9.  Edit the /etc/shorewall/shorewall.conf file.

    ::

    ::

        IP_FORWARDING=Yes

10. Edit the /etc/shorewall/interfaces file.

    ::

    ::

        ext eth0 - routefilter,tcpflags
        snet eth1
        rtnet eth3
        rext1 eth4
        rvxln vxlan1

11. Edit the /etc/shorewall/masq file.

    ::

    ::

        eth0 192.168.20.0/24
        eth0 192.168.28.0/24
        eth0 192.168.33.0/24

12. Edit the /etc/shorewall/policy file.

    ::

    ::

        $FW all ACCEPT
        ext all REJECT
        snet all ACCEPT
        rtnet all ACCEPT
        rext1 all ACCEPT
        rvxln all ACCEPT

13. Edit the /etc/shorewall/rules file.

    ::

    ::

        Ping/ACCEPT ext $FW
        SMTP/ACCEPT ext $FW
        ACCEPT ext $FW tcp 32
        SSH/ACCEPT ext $FW
        HTTPS/ACCEPT ext $FW
        ACCEPT ext $FW udp 60001:61000
        DNAT ext rtnet:192.168.20.11 tcp www
        DNAT ext rtnet:192.168.20.11 tcp 6080

    Note: Uncomment the DNAT rules and restart Shorewall as necessary to
    enable remote access to the dashboard and instance consoles in the
    OpenStack environment.

14. Edit the /etc/shorewall/zones file.

    Note: Shorewall zone names are limited to 5 characters because
    stupid.

    ::

    ::

        fw firewall
        ext ipv4
        snet ipv4
        rtnet ipv4
        rext1 ipv4
        rvxln ipv4

15. Edit the /etc/default/shorewall file.

    ::

    ::

        startup=1

16. Check the shorewall configuration.

    ::

    ::

        # shorewall check

17. Start the firewall service.

    ``service shorewall start``

OpenStack controller node (robb-controller1)
--------------------------------------------

1. Launch node

| OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
|  Flavor: 4 GB Performance 1
|  Networks: robb-test-net

1. Access the node from the jump box node using the IP address assigned
   by RAX.

Note: The node cannot access the internet without additional
configuration.

1. Configure network interfaces.

2. Edit the /etc/network/interfaces file.

   .. code::

       # Label robb-test-net
       auto eth0
       iface eth0 inet static
           address 192.168.20.11
           netmask 255.255.255.0
           gateway 192.168.20.1
           dns-nameservers 72.3.128.241 72.3.128.240

3. Edit the /etc/hosts file.

::

::

       # robb-controller
       192.168.20.11   robb-controller

       # robb-net1
       192.168.20.21   robb-net1

       # robb-comp1
       192.168.20.31   robb-comp1

Note: Comment out or remove any existing lines containing
*robb-controller*.

4. Reboot node.

5. Access the node from the network services node using the new IP
   address on the *robb-test-net* network.

6. Test network connectivity to the internet.

7. Update node.

``apt-get update && apt-get dist-upgrade``

8. Reboot node.

OpenStack network node (robb-net1)
----------------------------------

1. Launch node.

| OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
|  Flavor: 1 GB Performance 1
|  Networks: robb-test-net

1. Access the node from the network services node using the IP address
   assigned by RAX.

Note: The node cannot access the internet without additional
configuration.

1.  Add the *robb-vmnet* network to node.

2.  Add the *robb-ext1* network to node.

3.  Configure network interfaces.

4.  Edit the /etc/network/interfaces file.

    .. code::

        # Label robb-test-net
        auto eth0
        iface eth0 inet static
            address 192.168.20.21
            netmask 255.255.255.0
            gateway 192.168.20.1
            dns-nameservers 72.3.128.241 72.3.128.240

        # Label robb-vmnet
        auto eth1
        iface eth1 inet static
            address 192.168.27.21
            netmask 255.255.255.0

        # Label robb-ext1
        auto eth2
        iface eth2 inet static
            address 192.168.33.21
            netmask 255.255.255.0

        # Label vxlan1
        auto vxlan1
        iface vxlan1 inet static
            pre-up ip link add vxlan1 type vxlan id 1 group 239.0.0.1 dev eth2
            address 192.168.28.21
            netmask 255.255.255.0
            post-down ip link del vxlan1

5.  Edit the /etc/hosts file.

    ::

    ::

        # robb-controller
        192.168.20.11   robb-controller

        # robb-net1
        192.168.20.21   robb-net1

        # robb-comp1
        192.168.20.31   robb-comp1

    Note: Comment out or remove any existing lines containing
    *robb-net1*.

6.  Reboot node.

7.  Access the node from the network services node using the new IP
    address on the *robb-test-net* network.

8.  Test network connectivity to the internet.

9.  Update node.

    ``apt-get update && apt-get dist-upgrade``

10. Reboot node.

OpenStack compute node (robb-comp1)
-----------------------------------

1. Launch the node.

| OS: Ubuntu 14.04 (Trusty Tahr) PVHVM
|  Flavor:
|  \* 2 GB Performance 1 (supports several CirrOS instances) \* 4 or 8
  GB Performance 1 (supports a couple of Ubuntu/Fedora instances)

Networks: robb-test-net

1. Access the node from the network services node using the IP address
   assigned by RAX.

Note: The node cannot access the internet without additional
configuration.

1. Add the *robb-vmnet* network to node.

2. Configure network interfaces.

3. Edit the /etc/network/interfaces file.

   .. code::

       # Label robb-test-net
       auto eth0
       iface eth0 inet static
           address 192.168.20.31
           netmask 255.255.255.0
           gateway 192.168.20.1
           dns-nameservers 72.3.128.241 72.3.128.240

       # Label robb-vmnet
       auto eth1
       iface eth1 inet static
           address 192.168.27.31
           netmask 255.255.255.0

4. Edit the /etc/hosts file.

   .. code::

       # robb-controller
       192.168.20.11   robb-controller

       # robb-net1
       192.168.20.21   robb-net1

       # robb-comp1
       192.168.20.31   robb-comp1

Note: Comment out or remove any existing lines containing *robb-comp1*.

5. Reboot node.

6. Access the node from the network services node using the new IP
   address on the *robb-test-net* network.

7. Test network connectivity to the internet.

8. Update node.

``apt-get update && apt-get dist-upgrade``

9. Reboot node.

Install and configure OpenStack services
----------------------------------------

1. Use the `OpenStack Installation Guide
   <http://docs.openstack.org/juno/install-guide/install/apt/content/>`_
   with the following changes:

2. Configuring the basic environment on all nodes:

-  Skip the network configuration sections.

-  Use 192.168.20.1 (jump box node) as the NTP server.

3. Configuring the Compute service on the compute node:

-  Use *qemu* instead of *kvm* virtualization.

4. Configuring the Networking service on the network node:

-  Add the *vxlan1* interface as a port on the *br-ex* bridge.

5. Creating initial networks.

-  Use the following command for the subnet on the external network:

   .. code::

       neutron subnet-create ext-net --name ext-subnet \
       --allocation-pool start=192.168.28.101,end=192.168.28.200 \
       --disable-dhcp --gateway 192.168.28.1 192.168.28.0/24

Note: After performing the initial tenant network creation procedure,
try pinging 192.168.28.101 from the network services node.
