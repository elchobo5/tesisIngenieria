"""
Topologia de ejemplo
Fuente: http://www.topology-zoo.org/maps/Bellcanada.jpg
52 RAUSwitch
9 routers Quagga
10 hosts
1 controlador
"""

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

    routerLan9 = self.addHost('routerLan9', ips=['10.50.6.1/24', '10.8.1.1/24', '10.9.1.1/24'],
                                ce_mac_address='00:00:00:00:00:09',
                                gw='10.50.6.2', local_as="109", remote_as="100", cls=QuaggaRouter)
    

    switch1 = self.addHost('switch1', ips=['192.168.1.11/24','10.10.1.1/24'],
		  dpid='0000000000000101', controller_ip="192.168.1.10",
		  cls=RAUSwitch)

    switch2 = self.addHost('switch2', ips=['192.168.1.12/24','10.10.1.2/24','10.10.2.1/24'],
	      dpid='0000000000000102', controller_ip="192.168.1.10",
	      cls=RAUSwitch)
    

    switch3 = self.addHost('switch3', ips=['192.168.1.13/24','10.10.3.1/24','10.10.8.1/24','10.10.9.1/24'],
		  dpid='0000000000000103', controller_ip="192.168.1.10",
		  cls=RAUSwitch)
    

    switch4 = self.addHost('switch4', ips=['192.168.1.14/24','10.10.2.2/24','10.10.3.2/24','10.10.4.1/24','10.10.6.1/24'],
		  dpid='0000000000000104',controller_ip="192.168.1.10",
		  cls=RAUSwitch)

    switch5 = self.addHost('switch5', ips=['192.168.1.15/24','10.10.4.2/24','10.10.5.1/24'],
        dpid='0000000000000105',controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch6 = self.addHost('switch6', ips=['192.168.1.16/24','10.10.5.2/24','10.10.7.1/24','10.47.47.1/24'],
        dpid='0000000000000106',controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch7 = self.addHost('switch7', ips=['192.168.1.17/24','10.10.6.2/24','10.10.7.2/24','10.10.25.1/24'],
        dpid='0000000000000107',controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch8 = self.addHost('switch8', ips=['192.168.1.18/24','10.10.8.2/24','10.10.10.1/24','10.10.14.1/24'],
        dpid='0000000000000108',controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch9 = self.addHost('switch9', ips=['192.168.1.19/24','10.10.10.2/24','10.10.11.1/24','10.49.49.1/24'],
        dpid='0000000000000109',controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch10 = self.addHost('switch10', ips=['192.168.1.20/24','10.10.11.2/24','10.10.12.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch11 = self.addHost('switch11', ips=['192.168.1.21/24','10.10.12.2/24','10.10.13.1/24','10.88.88.1/24','10.48.48.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch12 = self.addHost('switch12', ips=['192.168.1.22/24','10.10.19.2/24','10.88.88.2/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)

    switch13 = self.addHost('switch13', ips=['192.168.1.23/24','10.10.14.2/24','10.10.13.2/24','10.10.19.1/24','10.10.20.1/24','10.10.18.1/24','10.10.21.1/24','10.1.0.2/24'],
          dpid='0000000000000002', controller_ip="192.168.1.10",
          border=1, ce_ip_address='10.1.0.1', ce_mac_address='00:00:00:00:00:02', local_as="100", remote_as="102",
          cls=RAUSwitch)
    

    switch14 = self.addHost('switch14', ips=['192.168.1.24/24','10.10.20.2/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch15 = self.addHost('switch15', ips=['192.168.1.25/24','10.10.18.2/24','10.10.17.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch16 = self.addHost('switch16', ips=['192.168.1.26/24','10.10.9.2/24','10.10.17.2/24','10.10.15.1/24','10.10.16.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch17 = self.addHost('switch17', ips=['192.168.1.27/24','10.10.15.2/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch18 = self.addHost('switch18', ips=['192.168.1.28/24','10.10.16.2/24','10.10.22.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch19 = self.addHost('switch19', ips=['192.168.1.29/24','10.10.21.2/24','10.10.23.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch20 = self.addHost('switch20', ips=['192.168.1.30/24','10.10.22.2/24','10.10.24.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch21 = self.addHost('switch21', ips=['192.168.1.31/24','10.10.23.2/24','10.10.24.2/24','10.10.29.1/24','10.10.31.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch22 = self.addHost('switch22', ips=['192.168.1.32/24','10.10.29.2/24','10.10.26.1/24','10.10.30.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch23 = self.addHost('switch23', ips=['192.168.1.33/24','10.10.26.2/24','10.10.27.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch24 = self.addHost('switch24', ips=['192.168.1.34/24','10.10.27.2/24','10.10.28.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch25 = self.addHost('switch25', ips=['192.168.1.35/24','10.10.31.2/24','10.10.32.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch26 = self.addHost('switch26', ips=['192.168.1.36/24','10.10.32.2/24','10.10.33.1/24','10.50.50.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch27 = self.addHost('switch27', ips=['192.168.1.37/24','10.10.30.2/24','10.10.33.2/24','10.10.34.1/24','10.10.35.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch28 = self.addHost('switch28', ips=['192.168.1.38/24','10.10.34.2/24','10.10.36.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch29 = self.addHost('switch29', ips=['192.168.1.39/24','10.10.25.2/24','10.10.28.2/24','10.10.37.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch30 = self.addHost('switch30', ips=['192.168.1.40/24','10.10.35.2/24','10.10.39.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch31 = self.addHost('switch31', ips=['192.168.1.41/24','10.10.36.2/24','10.10.37.2/24','10.10.38.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch32 = self.addHost('switch32', ips=['192.168.1.42/24','10.10.39.2/24','10.10.38.2/24','10.10.41.1/24','10.10.40.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch33 = self.addHost('switch33', ips=['192.168.1.43/24','10.10.41.2/24','10.10.42.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch34 = self.addHost('switch34', ips=['192.168.1.44/24','10.10.40.2/24','10.10.42.2/24','10.10.43.1/24','10.10.45.1/24','10.10.44.1/24','10.51.51.1/24','10.52.52.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch35 = self.addHost('switch35', ips=['192.168.1.45/24','10.10.43.2/24','10.10.46.1/24'],
          controller_ip="192.168.1.10",
          cls=RAUSwitch)
    

    switch36 = self.addHost('switch36', ips=['192.168.1.46/24','10.10.46.2/24','10.10.47.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)
    

    switch37 = self.addHost('switch37', ips=['192.168.1.47/24','10.10.47.2/24','10.10.48.1/24'],
              controller_ip="192.168.1.10",
              cls=RAUSwitch)

    switch38 = self.addHost('switch38', ips=['192.168.1.48/24','10.10.48.2/24','10.0.0.2/24'],
        dpid='0000000000000001', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.0.0.1', ce_mac_address='00:00:00:00:00:01', local_as="100", remote_as="101",
        cls=RAUSwitch)

    switch39 = self.addHost('switch39', ips=['192.168.1.49/24','10.10.45.2/24','10.10.49.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch40 = self.addHost('switch40', ips=['192.168.1.50/24','10.10.49.2/24','10.10.50.1/24','10.10.51.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch41 = self.addHost('switch41', ips=['192.168.1.51/24','10.10.44.2/24','10.10.50.2/24','10.10.53.1/24','10.10.52.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch42 = self.addHost('switch42', ips=['192.168.1.52/24','10.10.53.2/24','10.10.54.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch43 = self.addHost('switch43', ips=['192.168.1.53/24','10.10.52.2/24','10.10.54.2/24','10.10.55.1/24','10.10.56.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)
    

    switch44 = self.addHost('switch44', ips=['192.168.1.54/24','10.10.51.2/24','10.10.55.2/24','10.10.57.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch45 = self.addHost('switch45', ips=['192.168.1.55/24','10.10.56.2/24','10.10.57.2/24','10.24.48.1/24'],
        controller_ip="192.168.1.10",
        cls=RAUSwitch)

    switch46 = self.addHost('switch46', ips=['192.168.1.56/24','10.24.48.2/24','10.50.0.2/24'],
        dpid='0000000000000003', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.0.1', ce_mac_address='00:00:00:00:00:03', local_as="100", remote_as="103",
        cls=RAUSwitch)

    switch47 = self.addHost('switch47', ips=['192.168.1.57/24','10.47.47.2/24','10.50.1.2/24'],
        dpid='0000000000000004', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.1.1', ce_mac_address='00:00:00:00:00:04', local_as="100", remote_as="104",
        cls=RAUSwitch)

    switch48 = self.addHost('switch48', ips=['192.168.1.58/24','10.48.48.2/24','10.50.2.2/24'],
        dpid='0000000000000005', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.2.1', ce_mac_address='00:00:00:00:00:05', local_as="100", remote_as="105",
        cls=RAUSwitch)

    switch49 = self.addHost('switch49', ips=['192.168.1.59/24','10.49.49.2/24','10.50.3.2/24'],
        dpid='0000000000000006', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.3.1', ce_mac_address='00:00:00:00:00:06', local_as="100", remote_as="106",
        cls=RAUSwitch)

    switch50 = self.addHost('switch50', ips=['192.168.1.60/24','10.50.50.2/24','10.50.4.2/24'],
        dpid='0000000000000007', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.4.1', ce_mac_address='00:00:00:00:00:07', local_as="100", remote_as="107",
        cls=RAUSwitch)

    switch51 = self.addHost('switch51', ips=['192.168.1.61/24','10.51.51.2/24','10.50.5.2/24'],
        dpid='0000000000000008', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.5.1', ce_mac_address='00:00:00:00:00:08', local_as="100", remote_as="108",
        cls=RAUSwitch)

    switch52 = self.addHost('switch52', ips=['192.168.1.62/24','10.52.52.2/24','10.50.6.2/24'],
        dpid='0000000000000009', controller_ip="192.168.1.10",
        border=1, ce_ip_address='10.50.6.1', ce_mac_address='00:00:00:00:00:09', local_as="100", remote_as="109",
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
    self.addLink(man_switch, switch11, 12, 0)
    self.addLink(man_switch, switch12, 13, 0)
    self.addLink(man_switch, switch13, 14, 0)
    self.addLink(man_switch, switch14, 15, 0)
    self.addLink(man_switch, switch15, 16, 0)
    self.addLink(man_switch, switch16, 17, 0)
    self.addLink(man_switch, switch17, 18, 0)
    self.addLink(man_switch, switch18, 19, 0)
    self.addLink(man_switch, switch19, 20, 0)
    self.addLink(man_switch, switch20, 21, 0)
    self.addLink(man_switch, switch21, 22, 0)
    self.addLink(man_switch, switch22, 23, 0)
    self.addLink(man_switch, switch23, 24, 0)
    self.addLink(man_switch, switch24, 25, 0)
    self.addLink(man_switch, switch25, 26, 0)
    self.addLink(man_switch, switch26, 27, 0)
    self.addLink(man_switch, switch27, 28, 0)
    self.addLink(man_switch, switch28, 29, 0)
    self.addLink(man_switch, switch29, 30, 0)
    self.addLink(man_switch, switch30, 31, 0)
    self.addLink(man_switch, switch31, 32, 0)
    self.addLink(man_switch, switch32, 33, 0)
    self.addLink(man_switch, switch33, 34, 0)
    self.addLink(man_switch, switch34, 35, 0)
    self.addLink(man_switch, switch35, 36, 0)
    self.addLink(man_switch, switch36, 37, 0)
    self.addLink(man_switch, switch37, 38, 0)
    self.addLink(man_switch, switch38, 39, 0)
    self.addLink(man_switch, switch39, 40, 0)
    self.addLink(man_switch, switch40, 41, 0)
    self.addLink(man_switch, switch41, 42, 0)
    self.addLink(man_switch, switch42, 43, 0)
    self.addLink(man_switch, switch43, 44, 0)
    self.addLink(man_switch, switch44, 45, 0)
    self.addLink(man_switch, switch45, 46, 0)
    self.addLink(man_switch, switch46, 47, 0)
    self.addLink(man_switch, switch47, 48, 0)
    self.addLink(man_switch, switch48, 49, 0)
    self.addLink(man_switch, switch49, 50, 0)
    self.addLink(man_switch, switch50, 51, 0)
    self.addLink(man_switch, switch51, 52, 0)
    self.addLink(man_switch, switch52, 53, 0)
    self.addLink(man_switch, controller, 1, 0)
    
    self.addLink(switch1, switch2, 1, 1)
    self.addLink(switch2, switch4, 2, 1)
    self.addLink(switch3, switch4, 1, 2)
    self.addLink(switch3, switch8, 2, 1)
    self.addLink(switch3, switch16, 3, 1)
    self.addLink(switch4, switch5, 3, 1)
    self.addLink(switch4, switch7, 4, 1)
    self.addLink(switch5, switch6, 2, 1)
    self.addLink(switch7, switch29, 3, 1)
    self.addLink(switch8, switch9, 2, 1)
    self.addLink(switch8, switch13, 3, 1)
    self.addLink(switch9, switch10, 2, 1)
    self.addLink(switch10, switch11, 2, 1)
    self.addLink(switch11, switch13, 2, 2)
    self.addLink(switch11, switch12, 3, 2)
    self.addLink(switch13, switch12, 3, 1)
    self.addLink(switch13, switch14, 4, 1)
    self.addLink(switch13, switch15, 5, 1)
    self.addLink(switch13, switch19, 6, 1)
    self.addLink(switch15, switch16, 2, 2)
    self.addLink(switch16, switch17, 3, 1)
    self.addLink(switch16, switch18, 4, 1)
    self.addLink(switch6, switch7, 2, 2)
    self.addLink(switch18, switch20, 2, 1)
    self.addLink(switch19, switch21, 2, 1)
    self.addLink(switch20, switch21, 2, 2)
    self.addLink(switch21, switch22, 3, 1)
    self.addLink(switch21, switch25, 4, 1)
    self.addLink(switch22, switch23, 2, 1)
    self.addLink(switch22, switch27, 3, 1)
    self.addLink(switch23, switch24, 2, 1)
    self.addLink(switch24, switch29, 2, 2)
    self.addLink(switch25, switch26, 2, 1)
    self.addLink(switch26, switch27, 2, 2)
    self.addLink(switch27, switch28, 3, 1)
    self.addLink(switch27, switch30, 4, 1)
    self.addLink(switch28, switch31, 2, 1)
    self.addLink(switch29, switch31, 3, 2)
    self.addLink(switch30, switch32, 2, 1)
    self.addLink(switch31, switch32, 3, 2)
    self.addLink(switch32, switch33, 3, 1)
    self.addLink(switch32, switch34, 4, 1)
    self.addLink(switch33, switch34, 2, 2)
    self.addLink(switch34, switch35, 3, 1)
    self.addLink(switch34, switch39, 4, 1)
    self.addLink(switch34, switch41, 5, 1)
    self.addLink(switch35, switch36, 2, 1)
    self.addLink(switch36, switch37, 2, 1)
    self.addLink(switch37, switch38, 2, 1)
    self.addLink(switch39, switch40, 2, 1)
    self.addLink(switch40, switch41, 2, 2)
    self.addLink(switch40, switch44, 3, 1)
    self.addLink(switch41, switch42, 3, 1)
    self.addLink(switch41, switch43, 4, 1)
    self.addLink(switch42, switch43, 2, 2)
    self.addLink(switch43, switch44, 3, 2)
    self.addLink(switch43, switch45, 4, 1)
    self.addLink(switch44, switch45, 3, 2)
    self.addLink(switch46, switch45, 1, 3)
    self.addLink(switch47, switch6, 1, 3)
    self.addLink(switch48, switch11, 1, 4)
    self.addLink(switch49, switch9, 1, 4)
    self.addLink(switch50, switch26, 1, 3)
    self.addLink(switch51, switch34, 1, 6)
    self.addLink(switch52, switch34, 1, 7)

    ## Enlaces CE
    self.addLink(switch38, routerLan1, 2, 0)
    self.addLink(switch13, routerLan2, 7, 0)
    self.addLink(switch46, routerLan3, 2, 0)
    self.addLink(switch47, routerLan4, 2, 0)
    self.addLink(switch48, routerLan5, 2, 0)
    self.addLink(switch49, routerLan6, 2, 0)
    self.addLink(switch50, routerLan7, 2, 0)
    self.addLink(switch51, routerLan8, 2, 0)
    self.addLink(switch52, routerLan9, 2, 0)
    self.addLink(h0, routerLan1, 0, 1)
    self.addLink(h1, routerLan2, 0, 1)
    self.addLink(h2, routerLan3, 0, 1)
    self.addLink(h3, routerLan4, 0, 1)
    self.addLink(h4, routerLan5, 0, 1)
    self.addLink(h5, routerLan6, 0, 1)
    self.addLink(h6, routerLan7, 0, 1)
    self.addLink(h7, routerLan8, 0, 1)
    self.addLink(h8, routerLan9, 0, 1)
    self.addLink(h9, routerLan9, 0, 2)


