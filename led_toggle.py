# Name: led_toggle.py
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
import gi
import os

# Define GTK version 3.0
gi.require_version("Gtk", "3.0")

# Import GTK graphical interface
from gi.repository import Gtk

# define led variable as False state
led = False

# Set gpio0 direction output, it can be gpio1-5
# Gpio6 and gpio7 can only define as input
os.system('echo out > /sys/class/gpio/gpio0/direction')

# Write 0 into gpio0/value to turn off led
os.system('echo 0 > /sys/class/gpio/gpio0/value')

# Define a GUI window object
class MyWindow(Gtk.Window):
    # Initialize graphical window
    def __init__(self):
        # Window title
        super().__init__(title="MPIO10 GTK demo")
        # Add button1 named "Toggle LED"
        self.button = Gtk.Button(label="Toggle LED")
        # Link the button to function
        self.button.connect("clicked", self.toggle_button_clicked)
        # Add button to self object
        self.add(self.button)
    # When button pressed
    def toggle_button_clicked(self, widget):
    
        # declare led is a gloable variable that define already
        global led
        
        # Invert led when button press
        led = not led
        # If led is true
        if led == True:
            print("LED ON")
            # Turn on led
            os.system('echo 1 > /sys/class/gpio/gpio0/value')
        else:
            print("LED OFF")
            # Turn off led
            os.system('echo 0 > /sys/class/gpio/gpio0/value')

# Define win as MyWindow object
win = MyWindow()

# When close the window, exit the program
win.connect("destroy", Gtk.main_quit)

# Show the window
win.show_all()

# Execute the main code
Gtk.main()
