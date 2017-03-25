"""
Topologia 3
1 RAUSwitch
3 hosts
2 switch
1 controlador
"""

from mininet.topo import Topo
from rau_nodes import RAUSwitch, QuaggaRouter, RAUController, RAUHost


class CustomTopology( Topo ):
	def __init__( self ):
		Topo.__init__( self )

		# Hosts
    		origen = self.addHost('origen', ips=['10.10.11.1/24'], gw='10.10.11.2', cls=RAUHost)
    		surrogate = self.addHost('surrogate', ips=['10.10.12.1/24'], gw='10.10.12.2', cls=RAUHost)
		cliente = self.addHost('cliente', ips=['10.10.13.1/24'], gw='10.10.13.2', cls=RAUHost)
		surrogate2 = self.addHost('surrogate2', ips=['10.10.18.1/24'], gw='10.10.18.2', cls=RAUHost)

		#RAUSwitches
		r1 = self.addHost('r1', ips=['192.168.1.11/24','10.0.2.1/30','10.0.0.1/30','10.20.0.1/30'],
		      dpid='0000000000000001', controller_ip="192.168.1.10",
		      border=1, ce_ip_address='10.20.0.2', ce_mac_address='00:00:00:00:00:01',
		      cls=RAUSwitch)
		r2 = self.addHost('r2', ips=['192.168.1.12/24','10.0.2.2/30','10.0.1.2/30','10.20.1.1/30'],
		      dpid='0000000000000002', controller_ip="192.168.1.10",
                      border=1, ce_ip_address='10.20.1.2', ce_mac_address='00:00:00:00:00:02',
		      cls=RAUSwitch)

		r3 = self.addHost('r3', ips=['192.168.1.13/24','10.0.0.2/30','10.0.1.1/30','10.20.2.1/30'],
		      dpid='0000000000000003', controller_ip="192.168.1.10",
                      border=1, ce_ip_address='10.20.2.2', ce_mac_address='00:00:00:00:00:03',
		      cls=RAUSwitch)

		rl1 = self.addHost('rl1', ips=['10.20.0.2/30','10.10.11.2/24'],
		      ce_mac_address='00:00:00:00:00:01', gw='10.20.0.1',
		      cls=QuaggaRouter)

		rl2 = self.addHost('rl2', ips=['10.20.1.2/30','10.10.12.2/24','10.10.18.2/24'],
		      ce_mac_address='00:00:00:00:00:02', gw='10.20.1.1',
		      cls=QuaggaRouter)

		rl3 = self.addHost('rl3', ips=['10.20.2.2/30','10.10.13.2/24'],
		      ce_mac_address='00:00:00:00:00:03', gw='10.20.2.1',
		      cls=QuaggaRouter)

		# Controlador
    		controller = self.addHost('controller', cls=RAUController, ips=['192.168.1.10/24'])

		# Switches
    		s1 = self.addSwitch('s1', protocols='OpenFlow13', failMode='standalone')

		s2 = self.addSwitch('s2', protocols='OpenFlow13', failMode='standalone')



		# Enlaces
		self.addLink(s1, controller, 1, 0)
		self.addLink(s1, r1, 2, 0)
		self.addLink(s1, r2, 3, 0)
		self.addLink(s1, r3, 4, 0)


		self.addLink(r1, r2, 1, 1)
		self.addLink(r1, r3, 2, 1)
		self.addLink(r3, r2, 2, 2)
		
		
		self.addLink(rl1, r1, 0, 3)
		self.addLink(rl2, r2, 0, 3)
		self.addLink(rl3, r3, 0, 3)
	
		self.addLink(origen, rl1, 0, 1)
		self.addLink(rl2, surrogate, 1, 0)
		self.addLink(rl3, cliente, 1, 0)
		self.addLink(rl2, surrogate2, 2, 0)
		

		

	
