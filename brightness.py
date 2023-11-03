# importing the module
import screen_brightness_control as sbc

# get current brightness value
print(sbc.get_brightness())


#set the brightness of the primary display to 75%
sbc.set_brightness(100, display=0)

