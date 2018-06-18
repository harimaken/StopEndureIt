from pyfcm import FCMNotification
from configparser import ConfigParser
import os
import sys


def send_push(title ="Dungeon found", body="Gratz"):
    #config block
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    #FCM block
    push_service = FCMNotification(api_key=cfg.get("FCM", "api_key"))

    registration_id = cfg.get("FCM", "registration_id")
    message_title = title
    message_body = body
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)