

#Generate a set of packets for the given IP address and subnet
import sys
from scapy.all import *
from netaddr import IPNetwork

dst_network = raw_input("Please enter the subnet for packet generation")
dst_ips=[]
ip_range = IPNetwork(dst_network)

for i in ip_range:
    if i !=ip_range.broadcast:
        dst_ips.append(i)


        packets = Ether()/IP(dst=dst_ips)/TCP(dport=[80,53])

        [p for p in packets]

