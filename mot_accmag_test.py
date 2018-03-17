#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor #, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import math
import Adafruit_LSM303


def compass(mx,my,mz,ax,ay,az):
        bear = 0
        pi = 3.14159265359

        alpha = 0
        gamma = 0
        if (ax != 0):
            alpha = pi/2 - math.atan2(az,ax)
        #elif (ax < 0):
            #alpha = (pi/2 - math.atan2(az,ax))
        if (ay != 0):
            gamma = pi/2 - math.atan2(az,ay)
        #elif (ay < 0):
            #gamma = -(pi/2 + math.atan2(az,ay))

        print('pitch: {0}  roll: {1}'.format(math.degrees(alpha),math.degrees(gamma)))

        #y_h = my*math.cos(alpha) + mx*math.sin(gamma)*math.sin(alpha) - mz*math.cos(gamma)*math.sin(alpha)
        #x_h = mx*math.cos(gamma) - mz*math.sin(gamma)
        x_h = mx*math.cos(alpha) + my*math.sin(gamma)*math.sin(alpha) - mz*math.cos(gamma)*math.sin(alpha)
        y_h = my*math.cos(gamma) - mz*math.sin(gamma)
        print('x_h: {0}  y_h: {1}'.format(x_h,y_h))


        if (y_h>0):
                bear = 15 +90 - (math.atan(x_h/y_h)*180/pi)
        elif (y_h<0):
                bear = 15 + 270 - (math.atan(x_h/y_h)*180/pi)
                #bear = 270 - (math.atan2(x_h,y_h)*180/pi)
        elif (x_h < 0):
                bear = 180 + 15
        else:
                bear = 0 + 15
        print ('North and {0}'.format(bear))






lsm303 = Adafruit_LSM303.LSM303()

print("Select Motor port (1 or 2)")
mtr = input()
print("Select step delay interval (seconds)")
dly = input()

mtr_cntrl = Adafruit_MotorHAT()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mtr_cntrl.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mtr_cntrl.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mtr_cntrl.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mtr_cntrl.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, mtr)  # 200 steps/rev, motor port #1
myStepper.setSpeed(30)

print("Moving Motors")

while (True):
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag


    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
        accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    compass(mag_x,mag_y,mag_z,accel_x,accel_y,accel_z)


    myStepper.step(50, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)


