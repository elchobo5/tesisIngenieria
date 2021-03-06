'''
Created on Feb 26, 2015

@author: efviodo
'''

import json
import logging
import time
from ryu.base import app_manager
from webob import Response
from ryu.app.wsgi import ControllerBase, WSGIApplication, route
from dataTypes import DTNode, DTInterface, DTLink, DTLSNode, DTLSInterface, DTLSLink
from external_interfaces import SNMPAgents
from util import listOfNodesToJSON, listOfServicesToJSON, listOfServicesLSPsToJSON, listOfNHLEToJSON, JSONToDTInterfaceReduced
from util import listOfFTNJSON, listOfILMJSON, JSONToListOfNodes, JSONToDTService, getHTTPBody, JSONToDTNodeReduced 
from controllers import TopologyController
from patterns import Singleton
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, DEAD_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib.packet import ethernet
from ryu.ofproto import ether
from ryu.lib.packet import ipv4
from ryu.lib.packet import tcp
from ryu.lib.packet import packet
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import mpls
from ryu.controller import dpset
import os
from webob.static import DirectoryApp
from ryu.app.wsgi import ControllerBase, WSGIApplication, route
from ryu.base import app_manager
#####
from socket import error as SocketError
from ryu.contrib.tinyrpc.exc import InvalidReplyError
from ryu.app.wsgi import (
    ControllerBase,
    WSGIApplication,
    websocket,
    WebSocketRPCClient
)
from ryu.topology import event, switches
from ryu.controller.handler import set_ev_cls
from datetime import datetime

#API REST config
URI_API_REST_TOPOLOGY = '/topology'
URI_API_REST_TOPOLOGY_NODE = URI_API_REST_TOPOLOGY + '/node'
URI_API_REST_TOPOLOGY_NODE_INTERFACE = URI_API_REST_TOPOLOGY_NODE + '/interfaces'
URI_API_REST_TOPOLOGY_NODE_MPLS = URI_API_REST_TOPOLOGY_NODE + '/mpls'
URI_API_REST_TOPOLOGY_NODE_MPLS_ILM = URI_API_REST_TOPOLOGY_NODE_MPLS + '/ilm'
URI_API_REST_TOPOLOGY_NODE_MPLS_FTN = URI_API_REST_TOPOLOGY_NODE_MPLS + '/ftn'
URI_API_REST_TOPOLOGY_NODE_MPLS_NHLFE = URI_API_REST_TOPOLOGY_NODE_MPLS + '/nhlfe'
URI_API_REST_TOPOLOGY_DATAPATHS = URI_API_REST_TOPOLOGY + '/datapaths'
URI_API_REST_SERVICES = '/services'
URI_API_REST_SERVICE = URI_API_REST_SERVICES + '/service'
URI_API_REST_SERVICES_LSPS = URI_API_REST_SERVICES + '/lsps'
URI_API_REST_TOPOLOGY_NODE_OF = URI_API_REST_TOPOLOGY_NODE + '/of'
URI_API_REST_SERVICES_LOAD = URI_API_REST_SERVICES + '/load'

PATH = os.path.dirname(__file__)

class Proxy(Singleton, object):

    management_app = SNMPAgents(debug_mode=False)
    topo_controller = TopologyController(management_app)

    def __init__(self):
        super(Proxy, self).__init__()

        # Utilizado para emular la red como un stub de memoria
        #self.initialize_management_app()
        #lsdb = {}
        #self.initialize_lsdb()
        
        #self.topo_controller.update_ls_topology(self.lsdb)
        #self.topo_controller.redistribute_mpls_labels()
       
        #topology = self.topo_controller.get_topology()
        #self.topo_controller.initialize_services()

        #self.topo_controller.update_lsps()

        #self.topoc = TopologyController(self.mngapp)

        #topo_update = self.lsdb.update_ls_topology()
        #self.topoc.update_ls_topology(topo_update)

    ########## TOPOLOGY ######################################################
    def get_topology_node(self, router_id):
        return self.topo_controller.get_topology_node(router_id)

    def get_topology(self):
        return self.topo_controller.get_topology()

    def update_ls_topology(self, topo):
        return self.topo_controller.update_ls_topology(topo)

    def get_topology_nodes_datapaths(self):
        return self.topo_controller.get_topology_nodes_datapaths()

    def get_topology_nodes_interfaces(self, router_id):
        return self.topo_controller.get_topology_nodes_interfaces(router_id)

    def modify_topology_node(self, router_id, node_data):
        return self.topo_controller.modify_topology_node(router_id, node_data)

    def modify_topology_node_interface(self, router_id, interface_data):
        return self.topo_controller.modify_topology_node_interface(router_id, interface_data)

    ########## MPLS ##########################################################
    def get_node_mpls_tables_nhlfe(self, router_id):
        return self.topo_controller.get_node_mpls_tables_nhlfe(router_id)

    def get_node_mpls_tables_ilm(self, router_id):
        return self.topo_controller.get_node_mpls_tables_ilm(router_id)

    def get_node_mpls_tables_ftn(self, router_id):
        return self.topo_controller.get_node_mpls_tables_ftn(router_id)

    ########## Services ######################################################
    def add_service(self, service):
        '''
        doc
        '''
        return self.topo_controller.add_service(service)

    def update_service(self, service):
        '''
        doc
        '''
        return self.topo_controller.update_service(service)

    def get_services(self):
        '''
        doc
        '''
        return self.topo_controller.get_services()     

    def delete_service(self, sid):
        '''
        doc
        '''
        return self.topo_controller.delete_service(sid)  

    ########## LSPs #########################################################
    def get_service_lsps(self, service_ID):
        '''
        '''
        return self.topo_controller.get_service_lsps(service_ID) 

    def get_services_lsps(self):
        '''
        '''
        return self.topo_controller.get_services_lsps()  

    def update_services_lsps(self):
        '''
        '''
        return self.topo_controller.update_services_lsps()

    ########## OpenFlow #####################################################

    def get_topology_node_of_table(self, dpid):
        '''
        '''
        return self.topo_controller.get_topology_node_of_table(dpid)

##########################################################################
class WebSocketTopologyController(ControllerBase):

    def __init__(self, req, link, data, **config):
        super(WebSocketTopologyController, self).__init__(
            req, link, data, **config)
        self.app = data['app']

    @websocket('topology', '/v1.0/topology/ws')
    def _websocket_handler(self, ws):
        rpc_client = WebSocketRPCClient(ws)
        self.app.rpc_clients.append(rpc_client)
        rpc_client.serve_forever()

##########################################################################
##########################################################################
########## RYU MAIN APP
########################################################################## 
class GUIServerApp(app_manager.RyuApp):
    _CONTEXTS = {
        'wsgi': WSGIApplication,
        'dpset': dpset.DPSet,
        'switches': switches.Switches,
    }

    def __init__(self, *args, **kwargs):
        super(GUIServerApp, self).__init__(*args, **kwargs)

        # GET Proxy reference
        self.proxy = Proxy()

        wsgi = kwargs['wsgi']
        wsgi.register(GUIServerController, {'Proxy' : self.proxy, 'app': self})
        wsgi.register(WebSocketTopologyController, {'app': self})

        #For web socket connections
        self.rpc_clients = []

	self.ip_to_port = {}
	self.origen_to_surrogate = {}
	self.origen_to_surrogate["10.10.12.1"] = "10.10.11.1"
	self.origenes = {}
	self.origenes["10.10.11.1"] = 1

    ##########################################################################
    ########## OPENFLOW events handllers
    ########################################################################## 
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        print str(datapath.id) + ' is connected'

        #Se agrega flujo, de que todo lo que vaya para el puerto 80 de tcp vaya al controlador
        match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP,tcp_dst=80,ip_proto=6)
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 1, match, actions)
	match2 = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP,tcp_src=80,ip_proto=6)
	self.add_flow(datapath, 1, match2, actions)
        
        #Notify to OFController that new node has reported
        #self.of_controller.report_of_switch(datapath.id)
        #Upgrade node state to OF Ready if node
        self.proxy.topo_controller.register_of_node(str(datapath.id), datapath)

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
        

        # analyse the received packets using the packet library.
        pkt = packet.Packet(msg.data)

        in_port = msg.match['in_port']

        ipv4_pkt = pkt.get_protocol(ipv4.ipv4)
        tcp_pkt = pkt.get_protocol(tcp.tcp)
	
        if (ipv4_pkt) and (tcp_pkt):
                self.ip_to_port.setdefault(dpid, {})
		ip_src = ipv4_pkt.src
                ip_dst = ipv4_pkt.dst
                tcp_dst = tcp_pkt.dst_port
                tcp_src = tcp_pkt.src_port

		if not ip_src in self.ip_to_port[dpid]:
			self.ip_to_port[dpid][ip_src] = in_port

		if ip_dst in self.ip_to_port[dpid]:
                	out_port = self.ip_to_port[dpid][ip_dst]
                else:
                	out_port = ofproto.OFPP_FLOOD
		self.logger.info("ip src: %s, datapathid: %s, in_port: %d, ip_dst: %s", ip_src,dpid,in_port,ip_dst)
                if ((ip_dst == "10.10.11.1") and (tcp_dst == 80)):
			# construct action list.
			match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP,tcp_dst=tcp_dst,ip_proto=ipv4_pkt.proto,ipv4_dst=ip_dst)
			actions = [parser.OFPActionSetField(ipv4_dst="10.10.12.1"),parser.OFPActionSetField(eth_dst="00:00:00:00:00:02"),parser.OFPActionOutput(out_port)]

			out = parser.OFPPacketOut(datapath=datapath,
				                  buffer_id=ofproto.OFP_NO_BUFFER,
				                  in_port=in_port, actions=actions,
				                  data=msg.data)
			datapath.send_msg(out)

			if (out_port != ofproto.OFPP_FLOOD):
				#agrego el flujo
                                self.add_flow(datapath, 100, match, actions)
		elif ((ip_src == "10.10.12.1") and (tcp_src == 80)):
			# construct action list.
			match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP,tcp_src=tcp_src,ip_proto=ipv4_pkt.proto,ipv4_src=ip_src)
			actions = [parser.OFPActionSetField(ipv4_src="10.10.11.1"),parser.OFPActionSetField(eth_dst="00:00:00:00:00:03"),parser.OFPActionOutput(out_port)]

			out = parser.OFPPacketOut(datapath=datapath,
				                  buffer_id=ofproto.OFP_NO_BUFFER,
				                  in_port=in_port, actions=actions,
				                  data=msg.data)
			datapath.send_msg(out)

			if (out_port != ofproto.OFPP_FLOOD):
				#agrego el flujo
                                self.add_flow(datapath, 100, match, actions)
		elif (tcp_dst == 80):
			match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP,tcp_dst=tcp_dst,ip_proto=ipv4_pkt.proto,ipv4_dst=ip_dst,ipv4_src=ip_src)
			actions = [parser.OFPActionOutput(out_port)]

			out = parser.OFPPacketOut(datapath=datapath,
					          buffer_id=ofproto.OFP_NO_BUFFER,
					          in_port=in_port, actions=actions,
					          data=msg.data)
			datapath.send_msg(out)

			if (out_port != ofproto.OFPP_FLOOD):
				#agrego el flujo
	                        self.add_flow(datapath, 100, match, actions)
		elif (tcp_src == 80):
			match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP,tcp_src=tcp_src,ip_proto=ipv4_pkt.proto,ipv4_dst=ip_dst,ipv4_src=ip_src)
			actions = [parser.OFPActionOutput(out_port)]

			out = parser.OFPPacketOut(datapath=datapath,
					          buffer_id=ofproto.OFP_NO_BUFFER,
					          in_port=in_port, actions=actions,
					          data=msg.data)
			datapath.send_msg(out)

			if (out_port != ofproto.OFPP_FLOOD):
				#agrego el flujo
	                        self.add_flow(datapath, 100, match, actions)
				

    #OTRA FORMA POR AHORA    
    @set_ev_cls(dpset.EventDP, dpset.DPSET_EV_DISPATCHER)
    def handler_datapath(self, ev):
        if ev.enter:
            print 'datapath join'
        else:
            print 'datapath leave'
            datapath = ev.dp
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser
            print str(datapath.id) + ' se ha desconectado'

            self.proxy.topo_controller.unregister_of_node(str(datapath.id), datapath)

    def update_ws_clients_topology(self, nodes, links):
        '''
        '''

        #Update Links
        for l in links:
            self._event_link_delete_handler(l)

        #Updates nodes
        for n in nodes:
            self._event_switch_leave_handler(n)

        return True

#######################################################################################
################# WEB SERVICES API REST ###############################################
##### 
##### Description: api rest interfaces for differents components of 
##### application
#######################################################################################
class GUIServerController(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(GUIServerController, self).__init__(req, link, data, **config)
        
        #Get reference to Web app to redirect
        path = "%s/html/" % PATH
        self.static_app = DirectoryApp(path)

        #Get reference to Proxy instance
        self.proxy = data['Proxy']

        self.mainapp = data['app']
         
    #Redirect to Home web app
    @route('topology', '/{filename:.*}')
    def static_handler(self, req, **kwargs):
        print str(kwargs['filename'])
        if kwargs['filename']:
            req.path_info = kwargs['filename']
        return self.static_app(req)

    ##########################################################################
    ########## TOPOLOGY API REST
    ########################################################################## 
    @route('ws_topology', URI_API_REST_TOPOLOGY, methods=['GET'])
    def get_topology(self, req, **kwargs):
          
        print 'REST Service: GET Topology'

        proxy = self.proxy
        topology = proxy.get_topology()
        if topology is None:
            return Response(status=404)

        try:    
            body = listOfNodesToJSON(topology)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_topology', URI_API_REST_TOPOLOGY, methods=['PUT'])
    def actualizar_topology(self, req, **kwargs):
          
        print 'REST Service: PUT Topology'

        #Separetes HTTP header from HTTP body
        data = getHTTPBody(req)

        #Get topology data from JSON format data
        topo = JSONToListOfNodes(data) 

        proxy = self.proxy
        #resul = proxy.update_ls_topology(topo)
        nodes,links = proxy.update_ls_topology(topo)

        #Actualiza los caminos de los servicios
        proxy.update_services_lsps()

        result = True
        if not result:
            return Response(status=404)

        try:    
            body = 'Update complete succefully'
            return Response(content_type='application/json', body=body, status=200)
        except Exception as e:
            return Response(status=500)

    @route('ws_topology_node', URI_API_REST_TOPOLOGY_NODE + '/{rid}', methods=['GET'], requirements={'rid':''})
    def get_topology_node(self, req, **kwargs):
        
        router_id = kwargs['rid']   
        print 'REST Service: GET Node by router_id ('+router_id+')'

        proxy = self.proxy
        node = proxy.get_topology_node(router_id)
        if node is None:
            return Response(status=404)

        try:    
            body = node.to_JSON()
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_topology_node', URI_API_REST_TOPOLOGY_NODE + '/{rid}', methods=['POST'], requirements={'rid':''})
    def modify_topology_node(self, req, **kwargs):
        
        router_id = kwargs['rid']   
        print 'REST Service: POST Node extra data for router_id ('+router_id+')'

        #Separetes HTTP header from HTTP body
        data = getHTTPBody(req)

        node_data = JSONToDTNodeReduced(data)

        proxy = self.proxy
        result = proxy.modify_topology_node(router_id, node_data)
        if result is None or result is False:
            return Response(status=404)

        try:    
            body = json.dumps({'Result': 'OK'}, 2)
            return Response(content_type='json', body=body, status=200)
        except Exception as e:
            return Response(status=500)

    @route('ws_topology_node', URI_API_REST_TOPOLOGY_DATAPATHS, methods=['GET'])
    def get_topology_nodes_dpid(self, req, **kwargs):
         
        print 'REST Service: GET Nodes datapath_id' 

        proxy = self.proxy
        datapath_ids = proxy.get_topology_nodes_datapaths()
        if datapath_ids is None:
            return Response(status=404)
        try:    
            body = json.dumps(datapath_ids, indent=2)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_topology_node_by_datapath_interfaces', URI_API_REST_TOPOLOGY_NODE_INTERFACE + '/{rid}', methods=['GET'],  requirements={'rid':''})
    def get_topology_node_interfaces_get(self, req, **kwargs):
         
        print 'REST Service: GET Nodes interfaces by datapath_id' 

        rid = kwargs['rid']   
        proxy = self.proxy
        interfaces = proxy.get_topology_nodes_interfaces(rid)
        if interfaces is None:
            return Response(status=404)
        try:    
            body = json.dumps(interfaces, indent=2)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_topology_node_by_datapath_interfaces', URI_API_REST_TOPOLOGY_NODE_INTERFACE + '/{rid}', methods=['POST'],  requirements={'rid':''})
    def get_topology_node_interfaces(self, req, **kwargs):
         
        print 'REST Service: POST Nodes interfaces extra data' 

        rid = kwargs['rid']   

        #Separetes HTTP header from HTTP body
        data = getHTTPBody(req)

        interface_data = JSONToDTInterfaceReduced(data)

        proxy = self.proxy
        result = proxy.modify_topology_node_interface(rid, interface_data)
        if result is None or result is False:
            return Response(status=404)

        try:    
            body = json.dumps({'Result': 'OK'}, 2)
            return Response(content_type='json', body=body, status=200)
        except Exception as e:
            return Response(status=500)

    ##########################################################################
    ########## MPLS API REST
    ########################################################################## 
    @route('ws_mpls_services', URI_API_REST_SERVICES_LOAD + '/{start_index}/{end_index}', methods=['GET'], requirements={'start_index':'', 'end_index':''})
    def load_services(self, req, **kwargs):
          
        print 'Loading custom services..'

        start_index = int(kwargs['start_index'])
        end_index = int(kwargs['end_index'])

        nodo1 = "192.168.1.14"
        nodo2 = "192.168.1.12"
        interfazNodo1 = "10.0.0.2"
        interfazNodo2 = "10.1.0.2"

        json_template = {}
        json_template['ingress_node'] = ""
        json_template['egress_node'] = ""
        json_template['ingress_interface'] = ""
        json_template['egress_interface'] = ""
        json_template['eth_src'] = ""
        json_template['eth_dst'] = ""
        json_template['eth_type'] = ""
        json_template['vlan_vID'] = ""
        json_template['vlanPCP'] = ""
        json_template['ARP_spa'] = ""
        json_template['ARP_tpa'] = ""
        json_template['IPv4_src'] = ""
        json_template['IPv4_dst'] = ""
        json_template['IPv6_src'] = ""
        json_template['IPv6_dst'] = ""
        json_template['ICMPv4_type'] = ""
        json_template['ICMPv4_code'] = ""
        json_template['ICMPv6_type'] = ""
        json_template['ICMPv6_code'] = ""
        json_template['TCP_src'] = ""
        json_template['TCP_dst'] = ""
        json_template['UDP_src'] = ""
        json_template['UDP_dst'] = ""
        json_template['SCTP_src'] = ""
        json_template['SCTP_dst'] = ""
        json_template['service_name'] = ""
        json_template['service_color'] = "RGB(60,96,122)"
        json_template['ID'] = ""
        json_template['IP_proto'] = ""
        json_template['VPN_service_type'] = 2

        for i in range(start_index,end_index):

            datos = json_template
            datos['ingress_node'] = nodo1
            datos['egress_node'] = nodo2
            datos['ingress_interface'] = interfazNodo1
            datos['egress_interface'] = interfazNodo2
            datos['service_name'] = "VPN" + str(i) + "Ida"
            # datos['IPv4_src'] = "1.1." + str(i/256) + "." + str(i%256)
            datos['vlan_vID'] = hex(i)[2:]
            datos['vlanPCP'] = hex(i/4096)[2:]
        
            print "******************************************"
            print "Creando Servicio de ida de VPN " + str(i)
            print "******************************************"
            #Get topology data from JSON format data
            service = JSONToDTService(json.dumps(datos))
            proxy = self.proxy
            result = proxy.add_service(service)
            if result is None or not result:
                return Response(status=500)

            # time.sleep(0.5)

            datos = json_template
            datos['ingress_node'] = nodo2
            datos['egress_node'] = nodo1
            datos['ingress_interface'] = interfazNodo2
            datos['egress_interface'] = interfazNodo1
            datos['service_name'] = "VPN" + str(i) + "Vuelta"
            # datos['IPv4_src'] = "1.1." + str(i/256) + "." + str(i%256)
            datos['vlan_vID'] = hex(i)[2:]
            datos['vlanPCP'] = hex(i/4096)[2:]

            print "******************************************"
            print "Creando Servicio de vuelta de VPN " + str(i)
            print "******************************************"
            #Get topology data from JSON format data
            service = JSONToDTService(json.dumps(datos))
            proxy = self.proxy
            result = proxy.add_service(service)
            if result is None or not result:
                return Response(status=500)

            # time.sleep(0.5)

        try:    
            body = json.dumps({'Result': 'OK'}, 2)
            return Response(content_type='json', body=body, status=200)
        except Exception as e:
            return Response(status=500)







    @route('ws_mpls_services', URI_API_REST_SERVICES, methods=['GET'])
    def get_services(self, req, **kwargs):
          
        print 'REST Service: GET Services'

        proxy = self.proxy
        servcs = proxy.get_services()
        if servcs is None:
            return Response(status=404)

        try:    
            body = listOfServicesToJSON(servcs)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)


    @route('ws_mpls_services', URI_API_REST_SERVICES, methods=['POST'])
    def add_service(self, req, **kwargs):
          
        print 'REST Service: POST Services'
        print "Servicio invocado: " + str(datetime.now().time())

        #Separetes HTTP header from HTTP body
        data = getHTTPBody(req)

        #Get topology data from JSON format data
        service = JSONToDTService(data) 

        proxy = self.proxy
        
        result = proxy.add_service(service)
        if result is None or not result:
            return Response(status=500)

        try:    
            body = json.dumps({'Result': 'OK'}, 2)
            print "Servicio creado: " + str(datetime.now().time())
            return Response(content_type='json', body=body, status=200)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_services', URI_API_REST_SERVICES, methods=['PUT'])
    def actualizar_service(self, req, **kwargs):
          
        print 'REST Service: PUT Service'

        #Separetes HTTP header from HTTP body
        data = getHTTPBody(req)

        #Get topology data from JSON format data
        service = JSONToDTService(data) 

        proxy = self.proxy
        
        result = proxy.update_service(service)
        if result is None or not result:
            return Response(status=500)

        try:    
            body = json.dumps({'Result': 'OK'}, 2)
            return Response(content_type='json', body=body, status=200)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_services', URI_API_REST_SERVICE + '/{sid}', methods=['GET'], requirements={'sid':''})
    def get_service(self, req, **kwargs):
          
        print 'REST Service: GET Service Complete Data'

        sid = kwargs['sid']   
        proxy = self.proxy
        servcs = proxy.get_services()
        if servcs is None:
            return Response(status=404)

        try:    
            body = listOfServicesToJSON(servcs)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_services', URI_API_REST_SERVICE + '/{sid}', methods=['DELETE'], requirements={'sid':''})
    def delete_service(self, req, **kwargs):
        
        print 'REST Service: DELETE Service'

        sid = kwargs['sid']   
        proxy = self.proxy
        result = proxy.delete_service(sid)
        if result is None or result is False:
            return Response(status=404)

        try:    
            body = json.dumps({'Result': 'OK'}, 2)
            return Response(content_type='json', body=body, status=200)
        except Exception as e:
            return Response(status=500)

    

    @route('ws_mpls_services', URI_API_REST_SERVICES_LSPS, methods=['GET'])
    def get_services_lsps(self, req, **kwargs):
          
        print 'REST Service: GET Servicess lsps: '

        proxy = self.proxy
        servs_lsps = proxy.get_services_lsps()
        
        if servs_lsps is None:
            return Response(status=404)

        try:    
            body = listOfServicesLSPsToJSON(servs_lsps)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_services', URI_API_REST_SERVICES_LSPS + '/{ID}', methods=['GET'], requirements={'ID':''})
    def get_service_lsps(self, req, **kwargs):
          
        service_ID = kwargs['ID']   
        print 'REST Service: GET Services lsps: ' + service_ID

        proxy = self.proxy
        lsps = proxy.get_service_lsps(service_ID)
        
        if lsps is None:
            return Response(status=404)

        try:    
            body = body= listOfServicesLSPsToJSON2(lsps)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_node', URI_API_REST_TOPOLOGY_NODE_MPLS_NHLFE + '/{ID}', methods=['GET'], requirements={'ID':''})
    def get_mpls_tables_nhlfe(self, req, **kwargs):
          
        print 'REST Service: GET MPLS node tables NHLFE'

        router_id = kwargs['ID']

        proxy = self.proxy
        nhlfe = proxy.get_node_mpls_tables_nhlfe(router_id)

        if nhlfe is None:
            return Response(status=404)

        try:    
            body = body= listOfNHLEToJSON(nhlfe)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_node', URI_API_REST_TOPOLOGY_NODE_MPLS_FTN + '/{ID}', methods=['GET'], requirements={'ID':''})
    def get_mpls_tables_ftn(self, req, **kwargs):
          
        print 'REST Service: GET MPLS node tables FTN'

        router_id = kwargs['ID']

        proxy = self.proxy
        nhlfe = proxy.get_node_mpls_tables_ftn(router_id)

        if nhlfe is None:
            return Response(status=404)

        try:    
            body = body= listOfFTNJSON(nhlfe)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

    @route('ws_mpls_node', URI_API_REST_TOPOLOGY_NODE_MPLS_ILM + '/{ID}', methods=['GET'], requirements={'ID':''})
    def get_mpls_tables_ilm(self, req, **kwargs):
          
        print 'REST Service: GET MPLS node tables ILM'

        router_id = kwargs['ID']

        proxy = self.proxy
        nhlfe = proxy.get_node_mpls_tables_ilm(router_id)

        if nhlfe is None:
            return Response(status=404)

        try:    
            body = body= listOfILMJSON(nhlfe)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)


    @route('ws_mpls_node', URI_API_REST_TOPOLOGY_NODE_OF + '/{dpid}', methods=['GET'], requirements={'dpid':''})
    def get_topology_node_of(self, req, **kwargs):
          
        print 'REST Service: GET OF node table'

        dpid = kwargs['dpid']

        proxy = self.proxy
        of_table = proxy.get_topology_node_of_table(dpid)

        if of_table is None:
            return Response(status=404)

        try:    
            body= listOfILMJSON(of_table)
            return Response(content_type='application/json', body=body)
        except Exception as e:
            return Response(status=500)

app_manager.require_app('ryu.app.rest_topology')
app_manager.require_app('ryu.app.ws_topology')
app_manager.require_app('ryu.app.ofctl_rest')

  
