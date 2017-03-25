
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ipv4
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
from ryu.lib.packet import icmp
from ryu.lib.packet import lldp
from ryu.lib.packet import arp
from ryu.ofproto import ether


class CdnSdnSwitch13(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(CdnSdnSwitch13, self).__init__(*args, **kwargs)
        # initialize mac address table.
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # install the table-miss flow entry.
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # construct flow_mod message and send it.
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # get Datapath ID to identify OpenFlow switches.
        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})

        # analyse the received packets using the packet library.
        pkt = packet.Packet(msg.data)

        eth_pkt = pkt.get_protocol(ethernet.ethernet)
	ipv4_pkt = pkt.get_protocol(ipv4.ipv4)
	tcp_pkt = pkt.get_protocol(tcp.tcp)
	udp_pkt = pkt.get_protocol(udp.udp)
	icmp_pkt = pkt.get_protocol(icmp.icmp)
	lldp_pkt = pkt.get_protocol(lldp.lldp)
	arp_pkt = pkt.get_protocol(arp.arp)

        dst = eth_pkt.dst
        src = eth_pkt.src
	if (ipv4_pkt) and (tcp_pkt):
		dst_tcp = tcp_pkt.dst_port
		src_tcp = tcp_pkt.src_port
		dst_ipv4 = ipv4_pkt.dst
		src_ipv4 = ipv4_pkt.src

        # get the received port number from packet_in message.
        in_port = msg.match['in_port']

        #self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

        # learn a mac address to avoid FLOOD next time.
        self.mac_to_port[dpid][src] = in_port

        # if the destination mac address is already learned,
        # decide which port to output the packet, otherwise FLOOD.
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        # construct action list.
        actions = [parser.OFPActionOutput(out_port)]


	if  ((ipv4_pkt) and (tcp_pkt) and (ipv4_pkt.dst == "10.0.0.1") and (dst_tcp == 80)):
		match = parser.OFPMatch(eth_dst=dst,eth_type=ether.ETH_TYPE_IP,tcp_dst=dst_tcp,ip_proto=ipv4_pkt.proto,ipv4_dst=ipv4_pkt.dst)
		actions2 = [parser.OFPActionSetField(ipv4_dst="10.0.0.2"),parser.OFPActionSetField(eth_dst="00:00:00:00:00:02"),parser.OFPActionOutput(2)]				
		self.logger.info("Actions 2: %s", actions2)				
		self.add_flow(datapath, 1, match, actions2)
		actions3 = [parser.OFPActionSetField(ipv4_dst="10.0.0.2"),parser.OFPActionSetField(eth_dst="00:00:00:00:00:02"),parser.OFPActionOutput(2)]				
        	out = parser.OFPPacketOut(datapath=datapath,
                                  buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=in_port, actions=actions3,
                                  data=msg.data)
        	datapath.send_msg(out)
	elif  ((ipv4_pkt) and (tcp_pkt) and (ipv4_pkt.src == "10.0.0.2") and (src_tcp == 80)):
		match = parser.OFPMatch(eth_src=src,eth_type=ether.ETH_TYPE_IP,tcp_src=src_tcp,ip_proto=ipv4_pkt.proto,ipv4_src=ipv4_pkt.src)
		actions2 = [parser.OFPActionSetField(ipv4_src="10.0.0.1"),parser.OFPActionSetField(eth_src="00:00:00:00:00:01"),parser.OFPActionOutput(out_port)]				
		self.logger.info("Actions 2B: %s", actions2)				
		self.add_flow(datapath, 1, match, actions2)
		actions3 = [parser.OFPActionSetField(ipv4_src="10.0.0.1"),parser.OFPActionSetField(eth_src="00:00:00:00:00:01"),parser.OFPActionOutput(out_port)]				
        	out = parser.OFPPacketOut(datapath=datapath,
                                  buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=in_port, actions=actions3,
                                  data=msg.data)
        	datapath.send_msg(out)
	else:
		out = parser.OFPPacketOut(datapath=datapath,
                                  buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=in_port, actions=actions,
                                  data=msg.data)
        	datapath.send_msg(out)
