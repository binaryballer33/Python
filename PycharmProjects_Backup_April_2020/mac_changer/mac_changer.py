#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error (meaning the person did not enter a interface)
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        # code to handle error (meaning the person did not enter a mac address)
        parser.error("[-] Please specify an MAC address, use --help for more info.")
    return options  # don't have to return arguments because we don't use it in our program.


def change_mac(interface, new_mac):
    print("[+] Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # \w is regex for match alphaNumeric. so \w\w: is a mac
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:  # if you found a mac address print it else display could not read mac address
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
# =====================================================================================================================
# Alot of small changed made in the refactoring and housekeeping video should rewatch for what got changed.
# #!/usr/bin/env python
#
# import subprocess
# import optparse
# import re
#
#
# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
#     parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#     (options, arguments) = parser.parse_args()
#     if not options.interface:
#         #code to handle error (meaning the person did not enter a interface)
#         parser.error("[-] Please specify an interface, use --help for more info.")
#     elif not options.new_mac:
#         #code to handle error (meaning the person did not enter a mac address)
#         parser.error("[-] Please specify an MAC address, use --help for more info.")
#     return options  #dont have to return arguments because we don't use it in our program
#
# def change_mac(interface, new_mac):
#     print("[+] Changing mac address for " + interface + " to " + new_mac)
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])
#
#
# def get_current_mac(interface):
#     ifconfig_result = subprocess.check_output(["ifconfig", interface])
#     # \w is regex for match alphaNumeric. so \w\w: is a mac
#     mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
#
#     if mac_address_search_result:  # if you found a mac address print it else display could not read mac address
#         return mac_address_search_result.group(0)
#     else:
#         print("[-] Could not read MAC address.")
#
#
# options = get_arguments()
# current_mac = get_current_mac(options.interface)
# print("Current MAC = " + str(current_mac))
#
# change_mac(options.interface, options.new_mac)
#
# =====================================================================================================================
# added regex to check if the mac got changed and show that to us
# #!/usr/bin/env python
#
# import subprocess
# import optparse
# import re
#
#
# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
#     parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#     (options, arguments) = parser.parse_args()
#     if not options.interface:
#         #code to handle error (meaning the person did not enter a interface)
#         parser.error("[-] Please specify an interface, use --help for more info.")
#     elif not options.new_mac:
#         #code to handle error (meaning the person did not enter a mac address)
#         parser.error("[-] Please specify an MAC address, use --help for more info.")
#     return options  #dont have to return arguments because we don't use it in our program
#
# def change_mac(interface, new_mac):
#     print("[+] Changing mac address for " + interface + " to " + new_mac)
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])
#
#
# options = get_arguments()
# change_mac(options.interface, options.new_mac)
#
# ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
# print(ifconfig_result)
#
# # \w is regex for match alphaNumeric. so \w\w: is a mac
# mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
#
# if mac_address_search_result:  #if you found a mac address print it else display could not read mac address
#     print(mac_address_search_result.group(0))
# else:
#     print("[-] Could not read MAC address.")
#
# =====================================================================================================================
# shows the change you made to the interface by using the subprocess.check_output method to display the
# changed interfaces output to the screen
# #!/usr/bin/env python
#
# import subprocess
# import optparse
#
#
# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
#     parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#     (options, arguments) = parser.parse_args()
#     if not options.interface:
#         #code to handle error (meaning the person did not enter a interface)
#         parser.error("[-] Please specify an interface, use --help for more info.")
#     elif not options.new_mac:
#         #code to handle error (meaning the person did not enter a mac address)
#         parser.error("[-] Please specify an MAC address, use --help for more info.")
#     return options #dont have to return arguments because we don't use it in our program
#
# def change_mac(interface, new_mac):
#     print("[+] Changing mac address for " + interface + " to " + new_mac)
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])
#
#
# options = get_arguments()
# change_mac(options.interface, options.new_mac)
#
# ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
# print(ifconfig_result)
#
# =====================================================================================================================
# adding conditional statements to the code and changing the tuple unpacking to just returning the options not
# the arguments because we only need the options to complete the mac change.
#
# #!/usr/bin/env python
#
# import subprocess
# import optparse
#
#
# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
#     parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#     (options, arguments) = parser.parse_args()
#     if not options.interface:
#         #code to handle error (meaning the person did not enter a interface)
#         parser.error("[-] Please specify an interface, use --help for more info.")
#     elif not options.new_mac:
#         #code to handle error (meaning the person did not enter a mac address)
#         parser.error("[-] Please specify an MAC address, use --help for more info.")
#     return options #dont have to return arguments because we don't use it in our program
#
# def change_mac(interface, new_mac):
#     print("[+] Changing mac address for " + interface + " to " + new_mac)
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])
#
#
# options = get_arguments()
# change_mac(options.interface, options.new_mac)
#
# =====================================================================================================================
# made the code more reusable by creating a function out of options and arguments called get_arguments()
# also did tuple unpacking with the parser.parse_args() function I return the value this time
#
# #!/usr/bin/env python
#
# import subprocess
# import optparse
#
#
# def get_arguments():
#     parser = optparse.OptionParser()
#     parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
#     parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#     return parser.parse_args()
#
#
# def change_mac(interface, new_mac):
#     print("[+] Changing mac address for " + interface + " to " + new_mac)
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])
#
#
# (options, arguments) = get_arguments()
# change_mac(options.interface, options.new_mac)
#
#
# =====================================================================================================================
# made the code more reusable by creating a function out of changing the mac address
# also did tuple unpacking with the parser.parse_args() function
#
# #!/usr/bin/env python
#
# import subprocess
# import optparse
#
#
# def change_mac(interface, new_mac):
#     print("[+] Changing mac address for " + interface + " to " + new_mac)
#     subprocess.call(["ifconfig", interface, "down"])
#     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#     subprocess.call(["ifconfig", interface, "up"])
#
# parser = optparse.OptionParser()
#
# parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
# parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#
# (options, arguments) = parser.parse_args()
#
# change_mac(options.interface,options.new_mac)
#
# =====================================================================================================================
# the way to make the program except options values and arguments using the parser.parse_args() and tuple unpacking
#
# #!/usr/bin/env python
#
# import subprocess
# import optparse
#
# parser = optparse.OptionParser()
#
# parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
# parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#
# (options, arguments) = parser.parse_args()
# interface = options.interface
# new_mac = options.new_mac
#
# print("Changing mac address for " + interface + " to " + new_mac)
#
# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])
#
# =====================================================================================================================
# proper way of using subprocess.call so that someone can't use are program to execute system commands
# can't use spaces have to keep the system commands by themselves with no spaces.
#
# #!/usr/bin/env python
#
# import subprocess
#
# interface = input("interface > ")
# new_mac = input("new MAC > ")
#
# print("Changing mac address for " + interface + " to " + new_mac)
# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])
#
# =====================================================================================================================
# un-secure way of creating the mac changer; someone can run their commands with it.
# print("Changing mac address for " + interface + " to " + new_mac)
#
# #!/usr/bin/env python
#
# import subprocess
#
# interface = input("interface > ")
# new_mac = input("new MAC > ")
#
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
