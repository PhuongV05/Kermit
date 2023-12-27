import numpy
import pybullet as p
import pybullet_data
import time
import math

#set environment
p.connect(p.GUI) # gives visualisation
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.81)
p.setRealTimeSimulation(0)

p.loadURDF("plane.urdf" , [0, 0, 0], [0, 0, 0, 1])
targid = p.loadURDF("quadruped/spider.urdf", [0, 0, 1], [0, 0, 0, 1], useFixedBase = False)
obj_of_focus = targid

def moving(FRL, FRF, FLL, FLF, RRL, RRF, RLL, RLF):
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 0,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FRL,
        force = 100
        )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 1,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FRF,
        force = 100
        )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 2,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FLL,
        force = 100
    )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 3,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FLF,
        force = 100
    )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 4,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RRL,
        force = 100
    )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 5,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RRF,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 6,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RLL,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 7,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RLF,
        force = 100
    )

moving(math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4)

i = 0
FRL = 0
step_length = 1 * (math.pi/180)

while True:
    if (i == 240):
        i = 0
    if (i<60):
        FRL = FRL + step_length
        moving(FRL, math.pi, math.pi/4, 0, math.pi/4, math.pi*0.4, math.pi/4, math.pi*0.4) 
    elif(60 <= i < 120):
        moving(FRL, math.pi, math.pi/4, 0, math.pi/4, math.pi*0.4, math.pi/4, math.pi*0.4)
    elif(120 <= i < 180):
        FRL = FRL - step_length
        moving(FRL, math.pi, math.pi/4, 0, math.pi/4, math.pi*0.4, math.pi/4, math.pi*0.4)
    elif(180 <= i < 240):
        moving(FRL, math.pi, math.pi/4, 0, math.pi/4, math.pi*0.4, math.pi/4, math.pi*0.4) 
    i += 1
    time.sleep(0.005)
    p.stepSimulation()