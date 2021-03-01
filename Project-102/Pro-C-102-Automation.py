# time tracker..
# 07.45 : wake up
# 08.00 - 9.40 : Attend school 
# 10.00 : Goofey's morning walk
# 10.30 : Goofey's breakfast
# 11.10 - 1.30 : attend school again
# 14.00 : Lunch
# 14.30 : study
# 17.30 : break
# 18.00 : Goofey's evening walk
# 18.30 : outdoor activity
# 20.00 : return home
# 20.30 : dinner
# 21.00 : Goofey's dinner
# 22.00 : sleep time 

import os
import datetime
from playsound import playsound

sound = "notification_sound.mp3"
date = datetime.datetime.now()
time = date.hour
minute = date.minute

if time == 7 and minute == 45:
    print("Time to Wake up !!")
    playsound(sound)
elif time == 8:
    print("Time to attend your Classes !!")
    playsound(sound)
elif time == 10:
    print("Time to walk Goofey !!")
    playsound(sound)
elif time == 10 and minute == 30:
    print("Time to eat your breakfast give Goofey his !!")
    playsound(sound)
elif time == 11 and minute == 10:
    print("Time to attend classes (again) !!")
    playsound(sound)
elif time == 14:
    print("Time to eat lunch !!")
    playsound(sound)
elif time == 14 and minute == 30:
    print("Time to Study !!")
    playsound(sound)
elif time == 17 and minute == 30:
    print("Time to take a break !!")
    playsound(sound)
elif time == 18:
    print("Time to take Goofey for his morning walk !!")
    playsound(sound)
elif time == 18 and minute == 30:
    print("Time to go and play/cycle outside !!")
    playsound(sound)
elif time == 20:
    print("Time to return back now !!")
    playsound(sound)
elif time == 20 and minute == 30:
    print("Time to eat your dinner !!")
    playsound(sound)
elif time == 21:
    print("Time to give Goofey his dinner !!")
    playsound(sound)
elif time == 22 and minute == 10:
    print("Time to sleep !! Good Night !!")
    playsound(sound)