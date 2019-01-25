#Send ICMP packet from BackTrack machine to specified IP Address

import sys
from scapy.all import *

dst_IP = raw_input("Please enter the destination IP Address :")
icmp_packet = sr(IP(src="10.10.111.102",dst=dst_IP)/ICMP()/"HelloWorld")

icmp_packet