#!/usr/bin/python
# -*- coding: utf-8 -*-

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController, Ryu
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def scenario_basic():
    net = Mininet(  topo = None,
                    build = False,
                    host = CPULimitedHost,
                    link = TCLink,
                    ipBase = '10.0.0.0/8')

    info('*** Add Controller ***\n')
    c0 = net.addController( name = 'c0')

    info('*** Add three switchs ***\n')
    s1 = net.addSwitch('s1', cls = OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls = OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls = OVSKernelSwitch)

    info('*** Add Host and C2 ***\n')
    C2 = net.addHost('C2', cls = Host, ip = '10.0.0.1', defaultRoute = None)
    h2 = net.addHost('h2', cls = Host, ip = '10.0.0.2', defaultRoute = None)
    h3 = net.addHost('h3', cls = Host, ip = '10.0.0.3', defaultRoute = None)
    h4 = net.addHost('h4', cls = Host, ip = '10.0.0.4', defaultRoute = None)


    info('*** Add links ***\n')
    net.addLink(s1, C2, bw = 10)
    net.addLink(s1, s2, bw = 10)
    net.addLink(s3, s2, bw = 10)
    net.addLink(s3, h2, bw = 10)
    net.addLink(s3, h3, bw = 10)
    net.addLink(s3, h4, bw = 10)


    info('\n*** Build it ***\n')
    net.build()

    info('*** Start the controller ***\n')
    for controller in net.controllers:
        controller.start()

    info('*** Set controllers ***\n')
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s1').start([c0])

    # Lets start full tunneling 
    net.get('C2').cmd('iodined -f -P 1234 172.16.0.1 test.com &')
    net.get('h2').cmd('iodine -f -r -P 1234 10.0.0.1 test.com &')
    net.get('h3').cmd('iodine -f -r -P 1234 10.0.0.1 test.com &')
    net.get('h4').cmd('iodine -f -r -P 1234 10.0.0.1 test.com &')

    info('\n*** RUN Mininet\'s CLI ***\n')
    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    scenario_basic()