#!/usr/bin/env python
import netfilterqueue


def process_packet(packet):
    print(packet)
    packet.drop()
    # packet.accept() will place the packets in the queue and still forward them out, packet.drop() will not forward
    # iptables -I FORWARD -j NFQUEUE --queue-num 0 is the command I used to create the queue that queue.bind refers to
    # Don't forget to do iptables --flush once you are done to reset the iptables back to normal.
    # use these iptable rules if the computer you are targeting is your own local computer
    # iptables -I OUTPUT -j NFQUEUE --queue-num 0
    # iptables -I INPUT -j NFQUEUE --queue-num 0
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
