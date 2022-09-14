# Name: led_button_control.py
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

# Impoer necessary libraries
import gi
import os

# Define GTK version 3.0
gi.require_version("Gtk", "3.0")

# Import GTK graphical interface
from gi.repository import Gtk

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
        # Set button space 12 point
        self.box = Gtk.Box(spacing=12)
        # Add box object
        self.add(self.box)
        # Add button1 named "LED ON"
        self.button1 = Gtk.Button(label="LED ON")
        # Link the button to function
        self.button1.connect("clicked", self.on_button1_clicked)
        #
        self.box.pack_start(self.button1, True, True, 0)
        # Add button1 named "LED ON"
        self.button2 = Gtk.Button(label="LED OFF")
        # Link the button to function
        self.button2.connect("clicked", self.on_button2_clicked)
        #
        self.box.pack_start(self.button2, True, True, 0)
    # When button1 pressed
    def on_button1_clicked(self, widget):
        print("LED is ON")
        # Write 1 into gpio/gpio0/value
        os.system('echo 1 > /sys/class/gpio/gpio0/value')
    # When button2 pressed
    def on_button2_clicked(self, widget):
        print("LED is OFF")
        # Write 0 into gpio/gpio0/value
        os.system('echo 0 > /sys/class/gpio/gpio0/value')

# Define win as MyWindow object
win = MyWindow()

# When close the window, exit the program
win.connect("destroy", Gtk.main_quit)

# Show the window
win.show_all()

# Execute the main code
Gtk.main()
