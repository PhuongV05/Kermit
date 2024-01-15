from guizero import App, PushButton, Window, ButtonGroup, TextBox, Text
from config import motors_config_list
import csv
import time
import threading
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from config import motors_config_list
import time
import os
from pick import pick
import sys

chosen_motor = None
    
stop_threads = 0

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus, address = 0x42)
pca.frequency = 50

L0 = 5
shoulder_angle = 90

def calibration_process(max_pulse, min_pulse, rotate, chosen_motor):
    active_joint = servo.Servo(pca.channels[motors_config_list[chosen_motor-1]["channel"]])
    active_joint.set_pulse_width_range(min_pulse, max_pulse)
    active_joint.angle = rotate
    time.sleep(0.03)


def open_calibration():
    global chosen_motor
    chosen_motor = motor_button.value
    motor_window.show()

def calibration_screen():
    calibration_window.show()

app = App("MAIN", height=320, width=480)

calibration_button = PushButton(app, text="Calibration", command = calibration_screen, align="bottom", height="5", width="fill")

calibration_window = Window(app, title="Calibration Screen", height=320, width=480, visible=False)
motor_button = ButtonGroup(calibration_window, options = [["FRL", "1"], ["FRF", "2"], ["FLL", "3"], ["FLF", "4"], ["RRL", "5"], ["RRF", "6"], ["RLL", "7"], ["RLF", "8"]], command=open_calibration)
motor_window = Window(calibration_window, height=320, width=480, visible=False)
max_pulse_text = Text(motor_window, text="Enter maximum pulse width: ")
max_pulse = TextBox(motor_window, text = "")
min_pulse_text = Text(motor_window, text="Enter minimum pulse width: ")
min_pulse = TextBox(motor_window, text = "")
rotate_text = Text(motor_window, text="Enter angle of rotation: ")
rotate = TextBox(motor_window, text = "")
update_values = PushButton(motor_window, text="Update Data", command = lambda: calibration_process(int(max_pulse.value), int(min_pulse.value), int(rotate.value), int(chosen_motor)))

app.display()
