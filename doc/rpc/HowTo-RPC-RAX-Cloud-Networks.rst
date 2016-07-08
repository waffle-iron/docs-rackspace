=========================================
How-To: RPC Networks on RAX Cloud Servers
=========================================

This how-to provides instructions for creating neutron networks on RPC
all-in-one and multi-host environments on RAX cloud servers.

Prerequisites
~~~~~~~~~~~~~

#. Administrative (admin) and general (demo) tenants.
#. For all-in-one environments, the br-vlan interface contains
   gateway/router IP address (typically .1). For multi-node
   environments, each br-vlan interface contains a suitable IP address
   on the lower end of the subnet (e.g., 10.1.14.11, 10.1.14.12, etc.).
#. For multi-node environments, VXLAN tunnels among nodes must already
   exist.

Example /etc/network/interfaces file:

.. code::

    # Label rpc-mgmt1
    auto eth2
    iface eth2 inet manual
        up ip link set eth2 up
        down ip link set eth2 down

    # Label br-mgmt
    auto br-mgmt
    iface br-mgmt inet static
        bridge_stp off
        bridge_waitport 0
        bridge_fd 0
        address 10.1.11.11
        netmask 255.255.255.0
        bridge_ports eth2

    # Label br-storage
    auto br-storage
    iface br-storage inet static
        bridge_stp off
        bridge_waitport 0
        bridge_fd 0
        address 10.1.12.11
        netmask 255.255.255.0
        bridge_ports none

    # Label br-vxlan
    auto br-vxlan
    iface br-vxlan inet static
        bridge_stp off
        bridge_waitport 0
        bridge_fd 0
        address 10.1.13.11
        netmask 255.255.255.0
        bridge_ports none
        # To ensure ssh checksum is correct
        up /sbin/iptables -A POSTROUTING -t mangle -p tcp --dport 22 -j CHECKSUM --checksum-fill
        down /sbin/iptables -D POSTROUTING -t mangle -p tcp --dport 22 -j CHECKSUM --checksum-fill
        # To ensure dhcp checksum is correct
        up /sbin/iptables -A POSTROUTING -t mangle -p udp --dport 68 -j CHECKSUM --checksum-fill
        down /sbin/iptables -D POSTROUTING -t mangle -p udp --dport 68 -j CHECKSUM --checksum-fill
        # To provide internet connectivity to instances
        up /sbin/iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
        down /sbin/iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

    # Label br-vlan
    auto br-vlan
    iface br-vlan inet static
        bridge_stp off
        bridge_waitport 0
        bridge_fd 0
        address 10.1.14.11
        netmask 255.255.255.0
        bridge_ports none
        # Create veth pair, don't bomb if already exists
        pre-up ip link add br-vlan-veth type veth peer name eth12 || true
        # Set both ends UP
        pre-up ip link set br-vlan-veth up
        pre-up ip link set eth12 up
        # Set bridge UP/DOWN
        up ip link set $IFACE up
        down ip link set $IFACE down
        # Delete veth pair on DOWN
        post-down ip link del br-vlan-veth || true
        bridge_ports br-vlan-veth

Example /etc/rpc_deploy/rpc_user_config.yml file:

.. code::

    cidr_networks:
      container: 10.1.11.0/24
      storage: 10.1.12.0/24
      tunnel: 10.1.13.0/24

    used_ips:
      - 10.1.11.11
      - 10.1.12.11
      - 10.1.13.11

    global_overrides:
      internal_lb_vip_address: 10.1.11.11
      external_lb_vip_address: <public IP address>

    provider_networks:
      - network:
          group_binds:
            - all_containers
            - hosts
          type: "raw"
          container_bridge: "br-mgmt"
          container_interface: "eth1"
          ip_from_q: "container"
      - network:
          group_binds:
            - glance_api
            - cinder_api
            - cinder_volume
            - nova_compute
          type: "raw"
          container_bridge: "br-storage"
          container_interface: "eth2"
          ip_from_q: "storage"
      - network:
          group_binds:
            - neutron_linuxbridge_agent
          container_bridge: "br-vxlan"
          container_interface: "eth10"
          ip_from_q: "tunnel"
          type: "vxlan"
          range: "1:1000"
          net_name: "vxlan"
      - network:
          group_binds:
            - neutron_linuxbridge_agent
          container_bridge: "br-vlan"
          container_interface: "eth11"
          type: "vlan"
          range: "1:1000"
          net_name: "vlan"
      - network:
          group_binds:
            - neutron_linuxbridge_agent
          container_bridge: "br-vlan"
          container_interface: "eth12"
          type: "flat"
          net_name: "flat"

Flat external network and VXLAN tenant network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Source the admin tenant credentials.

#. Create the external network.

   .. code::

      neutron net-create ext-net --shared --router:external True \
      --provider:physical_network flat --provider:network_type flat

#. Create a subnet on the external network that uses the same subnet as
   the br-vlan interface.

   .. code::

      neutron subnet-create ext-net --name ext-subnet \
      --allocation-pool start=10.1.14.101,end=10.1.14.200 \
      --disable-dhcp --gateway 10.1.14.1 10.1.14.0/24

#. Source the demo tenant credentials.

#. Create the tenant network.

   .. code::

      neutron net-create demo-net-vxlan

#. Create a subnet on the tenant network.

   .. code::

      neutron subnet-create demo-net-vxlan --name demo-subnet-vxlan \
      --gateway 192.168.1.1 192.168.1.0/24

#. Create a router on the tenant network.

   .. code::

      neutron router-create demo-router-vxlan

#. Add an interface on the router to the subnet on the external network.

   .. code::

      neutron router-interface-add demo-router-vxlan demo-subnet-vxlan

#. Add a gateway on the router to the external network.

   .. code::

      neutron router-gateway-set demo-router-vxlan ext-net

#. On any node with the br-vlan interface, ping the tenant network
   router IP address, typically the lowest address in the external
   network subnet allocation.

#. Launch an instance using the demo tenant network.

#. Access the instance and ping a host on the internet.

Flat external network and VLAN tenant network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Source the admin tenant credentials.

#. Create the external network.

   .. code::

      neutron net-create ext-net --shared --router:external True \
      --provider:physical_network vlan --provider:network_type flat

#. Create a subnet on the external network that uses the same subnet as
   the br-vlan interface.

   .. code::

      neutron subnet-create ext-net --name ext-subnet \
      --allocation-pool start=10.1.14.101,end=10.1.14.200 \
      --disable-dhcp --gateway 10.1.14.1 10.1.14.0/24

#. Obtain the tenant ID of the demo tenant.

#. Create the tenant network.

   .. code::

      neutron net-create --tenant-id 0be9ed7344f54daba5bc34f63a082754 demo-net-vlan \
      --provider:network_type vlan --provider:physical_network vlan \
      --provider:segmentation_id 101

#. Source the demo tenant credentials.

#. Create a subnet on the tenant network.

   .. code::

      neutron subnet-create demo-net-vlan --name demo-subnet-vlan \
      --gateway 192.168.2.1 192.168.2.0/24

#. Create a router on the tenant network.

   .. code::

      neutron router-create demo-router-vlan

#. Add an interface on the router to the subnet on the external network.

   .. code::

      neutron router-interface-add demo-router-vlan demo-subnet-vlan

#. Add a gateway on the router to the external network.

   .. code::

      neutron router-gateway-set demo-router-vlan ext-net

#. On any node with the br-vlan interface, ping the tenant network
   router IP address, typically the lowest address in the external
   network subnet allocation.

#. Launch an instance using the demo tenant network.

#. Access the instance and ping a host on the internet.
