__author__ = "Richard O'Dwyer"
__email__ = "richard@richard.do"
__version__ = "1.0"
__license__ = "WTFPL, Version 2 (http://www.gnu.org/licenses/license-list.html#WTFPL)"

from datetime import datetime
import winsound
import time
import re

game_over = None
alarm_set = None
active = None

def start():
    global alarm_set

    if alarm_set:
        valid_time = re.match("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", alarm_set)
        if valid_time:
            current_time = str(datetime.time(datetime.now()))

            if active is None:
                print("Alarm active for " + alarm_set)

            if len(alarm_set) < 5:
                alarm_set = "0" + alarm_set

            if current_time.startswith(alarm_set):
                #sound the alarm
                sos()

            return True
        else:
            print("The time you entered was invalid, please enter a valid time e.g. 08:45")
            alarm_set = None
    else:
        alarm_set = input("Enter time to set alarm for: ")

#sos morse
def sos():
    for i in range(0, 3):
        winsound.Beep(2000, 100)
    for i in range(0, 3):
        winsound.Beep(2000, 400)
    for i in range(0, 3):
        winsound.Beep(2000, 100)

#start
print("__Welcome to Pylarm__")

#keep alive
while game_over is None:
    if start():
        active = True
    time.sleep(4)

