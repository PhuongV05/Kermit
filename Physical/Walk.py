from config import motors_config_list
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time
import math
import pygame

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus, address = 0x42)
pca.frequency = 50

pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

def moving(FRL, FRF, FLL, FLF, RRL, RRF, RLL, RLF):
    front_right_leg = servo.Servo(pca.channels[motors_config_list[0]["channel"]])
    front_right_leg.set_pulse_width_range(motors_config_list[0]["min_pulse"], motors_config_list[0]["max_pulse"])

    front_right_feet = servo.Servo(pca.channels[motors_config_list[1]["channel"]])
    front_right_feet.set_pulse_width_range(motors_config_list[1]["min_pulse"],motors_config_list[1]["max_pulse"])

    front_left_leg = servo.Servo(pca.channels[motors_config_list[2]["channel"]])
    front_left_leg.set_pulse_width_range(motors_config_list[2]["min_pulse"],motors_config_list[2]["max_pulse"])

    front_left_feet = servo.Servo(pca.channels[motors_config_list[3]["channel"]])
    front_left_feet.set_pulse_width_range(motors_config_list[3]["min_pulse"],motors_config_list[3]["max_pulse"])

    rear_right_leg = servo.Servo(pca.channels[motors_config_list[4]["channel"]])
    rear_right_leg.set_pulse_width_range(motors_config_list[4]["min_pulse"],motors_config_list[4]["max_pulse"])

    rear_right_feet = servo.Servo(pca.channels[motors_config_list[5]["channel"]])  
    rear_right_feet.set_pulse_width_range(motors_config_list[5]["min_pulse"],motors_config_list[5]["max_pulse"])

    rear_left_leg = servo.Servo(pca.channels[motors_config_list[6]["channel"]])
    rear_left_leg.set_pulse_width_range(motors_config_list[6]["min_pulse"],motors_config_list[6]["max_pulse"])

    rear_left_feet = servo.Servo(pca.channels[motors_config_list[7]["channel"]])
    rear_left_feet.set_pulse_width_range(motors_config_list[7]["min_pulse"],motors_config_list[7]["max_pulse"])

    front_right_leg.angle = 180 - FRL
    front_right_feet.angle = 180 - FRF
    front_left_leg.angle = FLL
    front_left_feet.angle = FLF

    rear_right_leg.angle = RRL
    rear_right_feet.angle = RRF
    rear_left_leg.angle = 180 - RLL
    rear_left_feet.angle = 180 - RLF 

def angle_up_down(height):
    theta = 90 - math.degrees(math.asin(height/0.5))
    return theta

def up_down():
    done = False
    while not done:
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.
        if (joystick.get_button(0) == (1)): # A
            done = True
        axis = joystick.get_axis(1)
        height = 0.25 - (axis*0.25)
        moving(45, angle_up_down(height), 45, angle_up_down(height), 45, angle_up_down(height), 45, angle_up_down(height))
        time.sleep(0.01)

def walk():
    step_length = 5
    FRL = 90
    FLL = 45
    RRL = 45
    RLL = 90
    i = 0
    done = False
    while not done:
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.
        if (joystick.get_button(3) == (1)): # Y
            done = True
        """
        axis = joystick.get_axis(0)
        if axis > 0.5:
            turn_right()
        elif axis < -0.5:
            turn_left()
        """
        if (i == 45):
            i = 0
        else: 
            pass
        if (i<9):
            RRL = RRL + step_length
            moving(FRL, 0,FLL, 0,RRL, 45,RLL, 0)
        elif (9<=i<18):
            FRL = FRL - step_length
            moving(FRL, 45,FLL, 0,RRL, 0,RLL,0)
        elif (18<=i<27):
            FRL = FRL + step_length
            FLL = FLL + step_length
            RRL = RRL - step_length
            RLL = RLL - step_length
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        elif (27<=i<36):
            RLL = RLL + step_length
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 45)
        elif (36<=i<45):
            FLL = FLL - step_length
            moving(FRL, 0, FLL, 45, RRL, 0,RLL, 0)
        i += 1
        time.sleep(0.001)

while not done:
    moving(45, 45, 45, 45, 45, 45, 45, 45)
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        if (joystick.get_button(0) == (1)): # A
            walk()
        if (joystick.get_button(1) == (1)): # B
            up_down()

pygame.close()