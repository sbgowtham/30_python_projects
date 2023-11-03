import time

print(time.strftime("%H:%M"))
alarm_time = input("Enter the alarm time (HH:MM): ")
while time.strftime("%H:%M") != alarm_time:
    time.sleep(1)
print("Time to wake up!")