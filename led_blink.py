# Name: led_blink.py
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
#
# This file interleave light up two LEDs
# Connect to GPIO0 and GPIO1
#


# Import necessary libraries
import os
import time

# Set gpio0 and gpio1 direction output, it can be gpio1-5
# Gpio6 and gpio7 can only define as input
os.system('echo out > /sys/class/gpio/gpio0/direction')
os.system('echo out > /sys/class/gpio/gpio1/direction')

# Write 0 into gpio0/value to turn off led, 1 into gpio1/value
os.system('echo 0 > /sys/class/gpio/gpio0/value')
os.system('echo 0 > /sys/class/gpio/gpio1/value')

while(True):
    os.system('echo 1 > /sys/class/gpio/gpio0/value')
    os.system('echo 0 > /sys/class/gpio/gpio1/value')
#    time.sleep(0.5)
    os.system('echo 0 > /sys/class/gpio/gpio0/value')
    os.system('echo 1 > /sys/class/gpio/gpio1/value')
#    time.sleep(0.5)

