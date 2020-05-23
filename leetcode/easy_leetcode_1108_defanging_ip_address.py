# https://leetcode.com/problems/defanging-an-ip-address/

ipv4_address = "192.168.1.33"


def defang_ip_address(address):
    delimiter = "."
    for octet in address:
        if octet != ".":
            print(octet, end="")
        else:
            print("[ " + delimiter + " ]", end="")


defang_ip_address(ipv4_address)