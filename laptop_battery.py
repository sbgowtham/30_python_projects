import psutil

battery = psutil.sensors_battery()

print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)