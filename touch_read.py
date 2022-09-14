# Name: touch_read.py
# This file is for MPIO10 Extension Module, run on MP510 Single Board Computer
# If there is any issue such as "No device found"
# Please make sure the MPIO-10 driver is fully installed
# To run this python code, you need install pyhon3 package
# GTK graphic interface is recommand operating on Linux system such as Debian
# for more infomation about GTK3, please visit:https://www.gtk.org/
#
# Author: Johnson Chen <johnson35762@gmail.com>
# Date: 2022/09/09
# ISSUE:
#
# Visit out forum for more information: https://forum.mapleboard.org/

# Import necessary libraries
import time
import os
# use gpio0 as input touch sensor
os.system('echo in  > /sys/class/gpio/gpio1/direction')

# Define gpio1 status file
gpio1 = open("/sys/class/gpio/gpio1/value", "r")

# Define prev_touch as old touch sensor status
prev_touch = 0

# Infinity loop
while True:
    # Set the file handle to position 0
    gpio1.seek(0)
    # Read the gpio state
    # When button press, system will read '1/n' in /sys/class/gpio/gpio1/value
    if gpio1.read()=='1\n':
        touch = 1
    else:
        touch = 0
    # Prevent bouncing
    if touch == 1 and prev_touch == 0:
        # Print Good on MP510 front pannel LED display
        os.system('echo Good > /tmp/led')
        
    elif touch == 0 and prev_touch == 1:
        # Print default information on LED display
        os.system('echo \"&&\" > /tmp/led')
    # Update prev_touch
    prev_touch = touch
    # Print touch sensor state
    print("Touch sensor:",touch)
    # Delay 0,1 sec
    time.sleep(0.1)
