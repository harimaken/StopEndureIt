import os
import os.path
import datetime
import time

from multiprocessing import freeze_support

import open_cv_SEI
import send_email_SEI
import image_upload_to_firebase_SEI
import catch_audio_SEI
import send_push_SEI

def modification_date(path_to_filename):

    start_time = os.path.getmtime(path_to_filename)  # тип float

    while True:
        print("Начальное время: " + str(datetime.datetime.fromtimestamp(start_time)))
        change_time = os.path.getmtime(path_to_filename)
        print("Измененное время: " + str(datetime.datetime.fromtimestamp(change_time)))
        if change_time != start_time:
            start_time = change_time
            #do something
            with open(path_to_file, 'r', encoding="utf-8") as f:
                my_lines = f.readlines()
                find_string = my_lines[-2].strip()
                find_string.split(",")
                print(find_string)

        time.sleep(5)
        print("---------")

#path_to_file = os.path.abspath('addontest.txt')
#path_to_file = os.path.abspath('C:\\Program Files (x86)\\World of Warcraft\\WTF\\Account\\414381077#1\\SavedVariables\\AAASfs.lua')
#modification_date(path_to_file)

if __name__ == '__main__':
    freeze_support()
    if(catch_audio_SEI.listen()):
        screenshot_name = open_cv_SEI.make_screenshot()
        image_upload_to_firebase_SEI.upload_to_fb(screenshot_name)
        send_push_SEI.send_push()
        send_email_SEI.send_email()
        print("Success")
