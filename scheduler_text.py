import datetime as dt
import time
import pywhatkit as whatsapp

from scheduler import Scheduler
import scheduler.trigger as trigger # Use to trigger specfic days ("Monday", "Tuesday")

phone_number = input('Enter your phone Number\n')

def WhatsApp_Message():
    whatsapp.sendwhatmsg_to_group_instantly(phone_number,"Hay.",15,True,2)
    #Opens whatsapp web & sends the Message to the recipent.
    print("testing")

schedule = Scheduler()

# schedule.minutely(dt.time(second=15), foo)
schedule.daily(dt.time(hour=14, minute=20), WhatsApp_Message) #Schedules the message daily at 2:20pm

while True:
    schedule.exec_jobs()
    time.sleep(1)