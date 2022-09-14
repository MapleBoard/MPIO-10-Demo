# Name: air_pressure_read.py
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
from fcntl import ioctl
import time
import os

BM180_I2C_ADDRESS = 0x77

#===== bmp180 i2c open and read calibration data ====
# Open i2c device name i2c-1, set read write in binary mode, no buffering
# The number of i2c-xx maybe different if your system have other i2c devices
# use $ i2cdetect -l to list i2c devices (i2c-tools package needed)
bmpi2c = open("/dev/i2c-1",  "r+b", buffering=0)

# Set I2c slave address 0x77
# BMP180 datasheet pp.20: https://cdn-shop.adafruit.com/datasheets/BST-BMP180-DS000-09.pdf
I2C_SLAVE_ADDR = BM180_I2C_ADDRESS

# ioctl function number: force set i2c slave address
I2C_SLAVE_FORCE = 0x0706

rt = ioctl(bmpi2c, I2C_SLAVE_FORCE, I2C_SLAVE_ADDR)

#read 22 bytes starting from register 0xAA
rt = bmpi2c.write(b'\xaa')
bmpReadData = bmpi2c.read(22)

print(bmpReadData)

while True:
    # BMP180 i2c
    rt = bmpi2c.write(b'\xf4\x2e') # write 0x2E to reg. 0xF4, start sampling UT
    # Wait 45 ms
    time.sleep(.0045)
    rt = bmpi2c.write(b'\xf6') # read 2 bytes starting from reg. 0xF6
    bmpReadData = bmpi2c.read(2)
    # Read temperature RAW data
    UT = bmpReadData[0]*256 + bmpReadData[1]  # TODO: need calibration here

    rt = bmpi2c.write(b'\xf4\xf4') # write 0x34+(3<<6) to reg. 0xF4, start sampling UP
    time.sleep(.0255)
    rt = bmpi2c.write(b'\xf6') # read 3 bytes starting from reg. 0xF6
    bmpReadData = bmpi2c.read(3)
    # Read pressure RAW data
    UP = bmpReadData[0]*65536 + bmpReadData[1]*256 + bmpReadData[2]
    UP = (UP>>5) - 329000  # TODO: need real calibration here

    print("Temperature = ", UT, " Pressure =", UP)
    time.sleep(0.5)
