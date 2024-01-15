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

    front_right_leg.angle = FRL
    front_right_feet.angle = FRF
    front_left_leg.angle = FLL
    front_left_feet.angle = FLF

    rear_right_leg.angle = RRL
    rear_right_feet.angle = RRF
    rear_left_leg.angle = RLL
    rear_left_feet.angle = RLF 

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
        moving(180 - 45, 180 - angle_up_down(height), 45, angle_up_down(height), 45, angle_up_down(height), 180 - 45, 180 - angle_up_down(height))
        time.sleep(0.01)

moving(180 - 45, 180 - 45, 45, 45, 45, 45, 180 - 45, 180 - 45)

while not done:
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        if (joystick.get_button(0) == (1)): # A
            pass
        if (joystick.get_button(1) == (1)): # B
            up_down()

pygame.close()