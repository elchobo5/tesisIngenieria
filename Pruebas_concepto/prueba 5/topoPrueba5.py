
from mininet.topo import Topo
from rau_nodes import RAUSwitch, QuaggaRouter, RAUController, RAUHost

class CustomTopology( Topo ):
  def __init__( self ):
    Topo.__init__( self )

    # Hosts
    h0 = self.addHost('h0', ips=['10.0.1.2/24'], gw='10.0.1.1', cls=RAUHost)
    h1 = self.addHost('h1', ips=['10.1.1.2/24'], gw='10.1.1.1', cls=RAUHost)
    h2 = self.addHost('h2', ips=['10.2.1.2/24'], gw='10.2.1.1', cls=RAUHost)
    h3 = self.addHost('h3', ips=['10.3.1.2/24'], gw='10.3.1.1', cls=RAUHost)
    h4 = self.addHost('h4', ips=['10.4.1.2/24'], gw='10.4.1.1', cls=RAUHost)
    h5 = self.addHost('h5', ips=['10.5.1.2/24'], gw='10.5.1.1', cls=RAUHost)
    h6 = self.addHost('h6', ips=['10.6.1.2/24'], gw='10.6.1.1', cls=RAUHost)
    h7 = self.addHost('h7', ips=['10.7.1.2/24'], gw='10.7.1.1', cls=RAUHost)
    h8 = self.addHost('h8', ips=['10.8.1.2/24'], gw='10.8.1.1', cls=RAUHost)
    h9 = self.addHost('h9', ips=['10.9.1.2/24'], gw='10.9.1.1', cls=RAUHost)

    routerLan1 = self.addHost('routerLan1', ips=['10.0.0.1/24', '10.0.1.1/24'],
                                ce_mac_address='00:00:00:00:00:01',
                                gw='10.0.0.2', local_as="101", remote_as="100", cls=QuaggaRouter)

    routerLan2 = self.addHost('routerLan2', ips=['10.1.0.1/24', '10.1.1.1/24'],
                                ce_mac_address='00:00:00:00:00:02',
                                gw='10.1.0.2', local_as="102", remote_as="100", cls=QuaggaRouter)

    routerLan3 = self.addHost('routerLan3', ips=['10.50.0.1/24', '10.2.1.1/24'],
                                ce_mac_address='00:00:00:00:00:03',
                                gw='10.50.0.2', local_as="103", remote_as="100", cls=QuaggaRouter)

    routerLan4 = self.addHost('routerLan4', ips=['10.50.1.1/24', '10.3.1.1/24'],
                                ce_mac_address='00:00:00:00:00:04',
                                gw='10.50.1.2', local_as="104", remote_as="100", cls=QuaggaRouter)

    routerLan5 = self.addHost('routerLan5', ips=['10.50.2.1/24', '10.4.1.1/24'],
                                ce_mac_address='00:00:00:00:00:05',
                                gw='10.50.2.2', local_as="105", remote_as="100", cls=QuaggaRouter)

    routerLan6 = self.addHost('routerLan6', ips=['10.50.3.1/24', '10.5.1.1/24'],
                                ce_mac_address='00:00:00:00:00:06',
                                gw='10.50.3.2', local_as="106", remote_as="100", cls=QuaggaRouter)

    routerLan7 = self.addHost('routerLan7', ips=['10.50.4.1/24', '10.6.1.1/24'],
                                ce_mac_address='00:00:00:00:00:07',
                                gw='10.50.4.2', local_as="107", remote_as="100", cls=QuaggaRouter)

    routerLan8 = self.addHost('routerLan8', ips=['10.50.5.1/24', '10.7.1.1/24'],
                                ce_mac_address='00:00:00:00:00:08',
                                gw='10.50.5.2', local_as="108", remote_as="100", cls=QuaggaRouter)

    routerLan9 = self.addHost('routerLan9', ips=['10.50.6.1/24', '10.8.1.1/24'],
                                ce_mac_address='00:00:00:00:00:09',
                                gw='10.50.6.2', local_as="109", remote_as="100", cls=QuaggaRouter)

    routerLan10 = self.addHost('routerLan0', ips=['10.50.7.1/24', '10.9.1.1/24'],
                                ce_mac_address='00:00:00:00:00:0A',
                                gw='10.50.7.2', local_as="110", remote_as="100", cls=QuaggaRouter)

    switch1 = self.addHost('switch1', ips=['192.168.1.11/24','10.10.10.1/24', '10.10.11.1/24', '10.0.0.2/24'],
        dpid='0000000000000001', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01', local_as="100", remote_as="101",
        cls=RAUSwitch)
    

    switch2 = self.addHost('switch2', ips=['192.168.1.12/24','10.10.10.2/24','10.10.12.2/24', '10.1.0.2/24'],
          dpid='0000000000000002', controller_ip="192.168.1.10",
          border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02', local_as="100", remote_as="102",
          cls=RAUSwitch)


    switch3 = self.addHost('switch3', ips=['192.168.1.13/24','10.10.12.1/24','10.10.13.1/24','10.50.0.2/24'],
        dpid='0000000000000003', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.0.1', ce_mac_address='00:00:00:00:00:03', local_as="100", remote_as="103",
        cls=RAUSwitch)

    switch4 = self.addHost('switch4', ips=['192.168.1.14/24','10.10.13.2/24','10.10.14.2/24','10.50.1.2/24'],
        dpid='0000000000000004', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.1.1', ce_mac_address='00:00:00:00:00:04', local_as="100", remote_as="104",
        cls=RAUSwitch)

    switch5 = self.addHost('switch5', ips=['192.168.1.15/24','10.10.14.1/24','10.10.15.1/24','10.50.2.2/24'],
        dpid='0000000000000005', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.2.1', ce_mac_address='00:00:00:00:00:05', local_as="100", remote_as="105",
        cls=RAUSwitch)

    switch6 = self.addHost('switch6', ips=['192.168.1.16/24','10.10.15.2/24','10.10.16.2/24','10.50.3.2/24'],
        dpid='0000000000000006', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.3.1', ce_mac_address='00:00:00:00:00:06', local_as="100", remote_as="106",
        cls=RAUSwitch)

    switch7 = self.addHost('switch7', ips=['192.168.1.17/24','10.10.16.1/24','10.10.17.1/24','10.50.4.2/24'],
        dpid='0000000000000007', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.4.1', ce_mac_address='00:00:00:00:00:07', local_as="100", remote_as="107",
        cls=RAUSwitch)

    switch8 = self.addHost('switch8', ips=['192.168.1.18/24','10.10.17.2/24','10.10.18.2/24','10.50.5.2/24'],
        dpid='0000000000000008', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.5.1', ce_mac_address='00:00:00:00:00:08', local_as="100", remote_as="108",
        cls=RAUSwitch)

    switch9 = self.addHost('switch9', ips=['192.168.1.19/24','10.10.18.1/24','10.10.19.1/24','10.50.6.2/24'],
        dpid='0000000000000009', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.6.1', ce_mac_address='00:00:00:00:00:09', local_as="100", remote_as="109",
        cls=RAUSwitch)

    switch10 = self.addHost('switch10', ips=['192.168.1.20/24','10.10.19.2/24','10.10.11.2/24', '10.50.7.2/24'],
        dpid='000000000000000A', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.7.1', ce_mac_address='00:00:00:00:00:0A', local_as="100", remote_as="110",
        cls=RAUSwitch)
    

    # Controlador
    controller = self.addHost('0c', cls=RAUController, ips=['192.168.1.10/24','192.168.56.101/24'])
    
    # Switch de la red de gestion
    man_switch = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

    # Enlaces
    self.addLink(man_switch, switch1, 2, 0)
    self.addLink(man_switch, switch2, 3, 0)
    self.addLink(man_switch, switch3, 4, 0)
    self.addLink(man_switch, switch4, 5, 0)
    self.addLink(man_switch, switch5, 6, 0)
    self.addLink(man_switch, switch6, 7, 0)
    self.addLink(man_switch, switch7, 8, 0)
    self.addLink(man_switch, switch8, 9, 0)
    self.addLink(man_switch, switch9, 10, 0)
    self.addLink(man_switch, switch10, 11, 0)
    self.addLink(man_switch, controller, 1, 0)
    
    self.addLink(switch1, switch2, 1, 1)
    self.addLink(switch2, switch3, 2, 1)
    self.addLink(switch3, switch4, 2, 1)
    self.addLink(switch4, switch5, 2, 1)
    self.addLink(switch5, switch6, 2, 1)
    self.addLink(switch6, switch7, 2, 1)
    self.addLink(switch7, switch8, 2, 1)
    self.addLink(switch8, switch9, 2, 1)
    self.addLink(switch9, switch10, 2, 1)
    self.addLink(switch10, switch1, 2, 2)
   

    ## Enlaces CE
    self.addLink(switch1, routerLan1, 3, 0)
    self.addLink(switch2, routerLan2, 3, 0)
    self.addLink(switch3, routerLan3, 3, 0)
    self.addLink(switch4, routerLan4, 3, 0)
    self.addLink(switch5, routerLan5, 3, 0)
    self.addLink(switch6, routerLan6, 3, 0)
    self.addLink(switch7, routerLan7, 3, 0)
    self.addLink(switch8, routerLan8, 3, 0)
    self.addLink(switch9, routerLan9, 3, 0)
    self.addLink(switch10, routerLan10, 3, 0)

    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)
    self.addLink(h2, routerLan3, 0, 1)
    self.addLink(h3, routerLan4, 0, 1)
    self.addLink(h4, routerLan5, 0, 1)
    self.addLink(h5, routerLan6, 0, 1)
    self.addLink(h6, routerLan7, 0, 1)
    self.addLink(h7, routerLan8, 0, 1)
    self.addLink(h8, routerLan9, 0, 1)
    self.addLink(h9, routerLan10, 0, 1)


