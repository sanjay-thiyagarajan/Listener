from .detect_human import look_for_human
from .telegram_utils import sight_bot
import pandas as pd 
import time
import os 
import json

class colors:
    red = '\033[91m'
    green = '\33[92m'
    end = '\033[0m'


def format_time(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    f = open('usr_data.json','r')
    j = json.loads(f.read())
    student_name = j['fullname']
    student_roll_number = j['username']
    bot = sight_bot()
    # message = "Name = " + student_name +  " \nID  = " + student_roll_number + "\nattention status : " + str(foo)
    intro_message = student_name + " `{" + "ID: "+ student_roll_number +  "}`" + " just joined the class"
    resp = bot.send_message(intro_message)
    print("Started monitoring, press Ctrl+C to end :)")
    class_start_time = time.time()
    total_uptime = 0
    while True:
        try:
            if look_for_human() == True:
                clear_terminal()
                print(colors.green, "Found student :)  [press ctrl + C to quit]", colors.end)
                start_time = time.time()
                while True:
                    h = look_for_human()
                    if h == False:
                        end_time = time.time()
                        # print("uptime was :", end_time - start_time)
                        total_uptime += end_time - start_time
                        clear_terminal()
                        print(colors.red , "Student not found  [press ctrl + C to quit]", colors.end)
                        break
                    else:
                        pass
        except KeyboardInterrupt:
            class_end_time = time.time()
            downtime = class_end_time - class_start_time - total_uptime
            end_message = student_name + " `{" + "ID: "+ student_roll_number +  "}`" + " left the class \n`Uptime: " + str(format_time(total_uptime)) + "` \n`Downtime: " + str(format_time(downtime)) + "`"
            resp = bot.send_message(end_message)
            clear_terminal()
            print("\nClass ended \nUptime: " , format_time(total_uptime), "\nDowntime: ", format_time(downtime))
            break
