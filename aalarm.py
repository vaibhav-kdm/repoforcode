import time
import datetime
import os

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")
        
        if current_time == alarm_time:
            print("\nWake up! Alarm ringing!")
            # Play sound (Windows example)
            try:
                import winsound
                winsound.Beep(1000, 1000)
            except:
                # For Mac/Linux
                os.system("afplay /System/Library/Sounds/Glass.aiff")
            break
        
        time.sleep(1)

# Set alarm time in HH:MM:SS format
alarm_time = input("Enter alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
