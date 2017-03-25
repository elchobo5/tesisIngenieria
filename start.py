#!/usr/bin/python

import os
import re
import sys
import atexit
import imp
import mininet.util
sys.modules['mininet.util'] = mininet.util

from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info, error
from mininet.util import quietRun

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Intf
net = None


def checkIntf( intf ):
    "Make sure intf exists and is not configured."
    config = quietRun( 'ifconfig %s 2>/dev/null' % intf, shell=True )
    if not config:
        error( 'Error:', intf, 'does not exist!\n' )
        exit( 1 )
    ips = re.findall( r'\d+\.\d+\.\d+\.\d+', config )
    if ips:
        error( 'Error:', intf, 'has an IP address,'
               'and is probably in use!\n' )
        exit( 1 )

def startNetwork():
  # Se levanta la topologia

  info('** Creating test topology\n')
  topology = imp.load_source('CustomTopology', sys.argv[1])
  topo = topology.CustomTopology()

  info('** Starting the network\n')
  global net
  
  intfName = 'eth1'
  info( '*** Connecting to hw intf: %s' % intfName )

  info( '*** Checking', intfName, '\n' )
  #checkIntf( intfName )

  net = Mininet(topo, controller=None)
  

  controller = net.hosts[ 0 ]
  info( '*** Adding hardware interface', intfName, 'to controller',
          controller.name, '\n' )
  _intf = Intf( intfName, node=controller )

  net.start()

  # Se borra el archivo json de inicializacion viejo
  if os.path.exists('utils/init_json.json'):
    os.remove('utils/init_json.json')
  
  # Invocar el metodo start en cada nodo
  info('** Starting RAU nodes\n')
  for node in topo.hosts():
    n = net.get(node)
    n.start()

  # info('** Dumping host connections\n')
  # dumpNodeConnections(net.hosts)

  info('\n** Running CLI\n')
  CLI(net)


def stopNetwork():
  # Se detiene el entorno y se terminan todos los procesos
  if net is not None:
      info('** Tearing down network\n')
      net.stop()

if __name__ == '__main__':
  # Force cleanup on exit by registering a cleanup function
  atexit.register(stopNetwork)

  # Tell mininet to print useful information
  setLogLevel('info')
  startNetwork()
