#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="target", help="Target IP / IP range.")
    options, arguments = parser.parse_args()
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # srp stands for send and receive the p just means you specify the Ether(dst mac)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list


def print_result(results_list):
    print("_" * 65)
    print("\t     IP\t\t\t   MAC Address\n_________________________________________________________________")
    for client in results_list:
        print("\t" + client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

# ----------------------------------------------------------------------------------------------------------------------
# same thing but using a dictionary
#
# #!/usr/bin/env python
#
# import scapy.all as scapy
#
#
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     # srp stands for send and receive the p just means you specify the Ether(dst mac)
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]
#
#
#     client_list = []
#     for element in answered_list:
#         client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
#         client_list.append(client_dict)
#     return client_list
#
# def print_result(results_list):
#     print("_" * 65)
#     print("\t     IP\t\t\t   MAC Address\n_________________________________________________________________")
#     for client in results_list:
#         print("\t" + client["ip"] + "\t\t" + client["mac"])
#
#
#
#
#
# scan_result = scan("192.168.1.0/24")
# print_result(scan_result)
#
#
#
# ----------------------------------------------------------------------------------------------------------------------
# #!/usr/bin/env python
#
# import scapy.all as scapy
#
#
# def scan(ip):
#     arp_request = scapy.ARP(pdst=ip)
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_request_broadcast = broadcast/arp_request
#     # srp stands for send and receive the p just means you specify the Ether(dst mac)
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]
#
#     print("_"*65)
#     print("\t     IP\t\t\t   MAC Address\n_________________________________________________________________")
#     for element in answered_list:
#         print("\t"+ element[1].psrc + "\t\t" + element[1].hwsrc)
#
#
#
#
#
# scan("192.168.1.0/24")
