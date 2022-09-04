#!/usr/bin/env python3
import smtplib
import os
from email.mime.text import MIMEText

import requests
import logging
from typing import Optional
from typing import Union
from fastapi import FastAPI, Response

#from enum import Enum


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




def send_mail_api(inputmailToid, bodymessage):

    port=465
    smtp_server = os.environ.get("SMTP_ADDRESS")
    USER_EMAIL = os.environ.get("USER_EMAIL")
    USER_PASSWORD = os.environ.get("USER_PASSWORD")
    sender_email = "hemanth22hemu@gmail.com "
    receiver_email = inputmailToid
    message = MIMEText(bodymessage)
    
    message["Subject"] = "[High] keepalive_jfrog status"
    message["From"] = sender_email
    message["To"] = receiver_email


    with smtplib.SMTP_SSL(smtp_server,port) as mailserver:
        mailserver.login(USER_EMAIL,USER_PASSWORD)
        mailserver.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return "mail successfully sent"

app = FastAPI()

@app.get('/send_email')
async def send_email(inputemail: str, inputmsg: str):
    return send_mail_api(inputemail,inputmsg)
