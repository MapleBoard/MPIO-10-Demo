from fcntl import ioctl
import os
import time

# ======== gpio ===========
# gpio0 --> touch sensor power
# gpio1 <-- touch sensor input
# Set gpio0 high, touch sensor power on, LED on
os.system('echo in  > /sys/class/gpio/gpio1/direction')
os.system('echo out > /sys/class/gpio/gpio0/direction')
os.system('echo 1  > /sys/class/gpio/gpio0/value')
gpio1 = open("/sys/class/gpio/gpio1/value", "r")

#===== bmp180 i2c open and read calibration data ====
bmpi2c = open("/dev/i2c-1",  "r+b", buffering=0)
I2C_SLAVE_ADDR = 0x77  # bmp180 i2c slave address 0x77
I2C_SLAVE_FORCE = 0x0706  # ioctl function number: force set i2c slave address
rt = ioctl(bmpi2c, I2C_SLAVE_FORCE, I2C_SLAVE_ADDR) 

rt = bmpi2c.write(b'\xaa')  #read 22 bytes starting from register 0xAA
bmpReadData = bmpi2c.read(22)

print(bmpReadData)

ztouch = 0

#===== Main Loop ======
while True:
	# touch sensor action
	gpio1.seek(0)  # rewind for read
	if gpio1.read() == '1\n':
		touch = 1
	else:
		touch = 0
	if touch == 1 and ztouch == 0:
		os.system('echo Good > /tmp/led') # say Good on LED display
	elif touch == 0 and ztouch == 1:
		os.system('echo \"&&\" > /tmp/led') # default LED display
	ztouch = touch

	# BMP180 i2c 
	rt = bmpi2c.write(b'\xf4\x2e') # write 0x2E to reg. 0xF4, start sampling UT
	time.sleep(.0045)
	rt = bmpi2c.write(b'\xf6') # read 2 bytes starting from reg. 0xF6
	bmpReadData = bmpi2c.read(2)

	UT = bmpReadData[0]*256 + bmpReadData[1]  # TODO: need calibration here

	rt = bmpi2c.write(b'\xf4\xf4') # write 0x34+(3<<6) to reg. 0xF4, start sampling UP
	time.sleep(.0255)
	rt = bmpi2c.write(b'\xf6') # read 3 bytes starting from reg. 0xF6
	bmpReadData = bmpi2c.read(3)

	UP = bmpReadData[0]*65536 + bmpReadData[1]*256 + bmpReadData[2]
	UP = (UP>>5) - 329000  # TODO: need real calibration here

	print("UT=", UT, " UP=", UP, " touch=", touch)
	time.sleep(0.1)


