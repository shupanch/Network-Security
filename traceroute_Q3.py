#TRACEROUTE IMPLEMENTATION USING SCAPY

import sys
from scapy.all import *

test_IP = raw_input("please enter the IP address of the internal linux machine :")

for i in range(1, 30):
    pkt = IP(dst=test_IP, ttl=i) / TCP()
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        break
    elif reply.type == 3:
        # We've reached our destination
        print("Done!", reply.src)
        break
    else:
        # We're in the middle somewhere
        print("%d hops away: " % i , reply.src)

