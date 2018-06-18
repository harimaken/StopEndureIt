import smtplib
import os
import sys
from configparser import ConfigParser


def send_email():
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    subject = "StopEndureIt message"
    to_addr = "harimaken@mail.ru"
    from_addr = "harimaken@mail.ru"
    body_text = "Dungeon found"
    host = cfg.get("smtp", "host")
    user = cfg.get("smtp", "user")
    password = cfg.get("smtp", "password")

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))

    server = smtplib.SMTP_SSL(host, 465)
    server.login(user, password)
    #server.connect("smtp.mail.ru", 465)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()