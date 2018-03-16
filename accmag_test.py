# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time
import math

# Import the LSM303 module.
import Adafruit_LSM303

def compass(x,y,z):
	bear = 0
	pi = 3.14159265359
	
	alpha = math.atan(x)
	gamma = math.atan(y)
	print('roll: {0}  pitch: {1}'.format(math.degrees(gamma),math.degrees(alpha)))

	x_h = x*math.cos(alpha) + y*math.sin(gamma)*math.sin(alpha)
			- z*math.cos(gamma)*math.sin(alpha)
	y_h = y*math.cos(gamma) - z*math.sin(gamma)
	

	if (y>0):
		bear = 15 + 90 - (math.atan(x_h/y_h)*180/pi)
	elif (y<0):
		bear = 15 + 270 - (math.atan(x_h/y_h)*180/pi)
	elif (x < 0):
		bear = 180 + 15
	else:
		bear = 0 + 15
	print ('North and {0}'.format(bear))

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag


    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
    	accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
	compass(mag_x,mag_y,mag_z)
    # Wait half a second and repeat.
    time.sleep(2)
