#!/usr/bin/env python
import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as out_file: # wb because this is a image and images are binary files
        out_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


download("https://www.electrive.com/wp-content/uploads/2020/01/lucid-air-2020-01-min.png")
