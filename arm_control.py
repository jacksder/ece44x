#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor #, Adafruit_DCMotor, Adafruit_StepperMotor

import Adafruit_LSM303
import time
import atexit




#Classes and Functions
class Motor_control:
    def __init__(self):
        self.mtr_hat = Adafruit_MotorHAT()
        #initialize motor connections
        self.mtr_azimuth = mtr_hat.getStepper(200, 1)  # 200 steps/rev, stepper port #1
        self.mtr_pitch = mtr_hat.getStepper(200, 2)  # 200 steps/rev, stepper port #2
        mtr_azimuth.setSpeed(60)
        mtr_pitch.setSpeed(60)
        

    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors(self):
        self.mtr_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mtr_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mtr_hat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mtr_hat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    #Function to move Arm stepper motors
    def move(self, steps_azimuth, steps_pitch):
        if (steps_azimuth > steps_pitch):
            for i in range(0, steps_pitch):
                mtr_azimuth.onestep(Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
                mtr_pitch.onestep(Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)

            for x in range(0, steps_azimuth - steps_pitch):
                mtr_azimuth.onestep(Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
        else:
            for i in range(0, steps_azimuth):
                mtr_azimuth.onestep(Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
                mtr_pitch.onestep(Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)

            for x in range(0, steps_pitch - steps_azimuth):
                mtr_pitch.onestep(Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)

    
#Function to get current arm vector
def arm_vect(lsm303):
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))



    #TODO calculate azimuth and pitch from acclmtr/compass data


    return azimuth, pitch

#Function to get new vector
def new_vect():
    #TODO method to get vector from stack of other python prog



#Initialize system
lsm303 = Adafruit_LSM303.LSM303()
m_cntrl = Motor_control()
atexit.register(m_cntrl.turnOffMotors) #safely shutdown motors on program close


#Control loop
while (True):
    # Wait half a second and repeat.
    time.sleep(0.5)






