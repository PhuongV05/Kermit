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
lr_angle = p.addUserDebugParameter("lr_angle", -math.pi/6, math.pi/6, 0)


numjoints = p.getNumJoints(targid)
print("Number of joints: ", numjoints)

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

def angle_lean_right_side(lean_angle):
    theta = math.pi/4 - lean_angle
    return theta

def angle_lean_left_side(lean_angle):
    theta = math.pi/4 + lean_angle
    return theta

moving(math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4)

while True:
    lr_lean_angle = p.readUserDebugParameter(lr_angle)
    moving(math.pi/4, angle_lean_right_side(lr_lean_angle), math.pi/4, angle_lean_left_side(lr_lean_angle), math.pi/4, angle_lean_right_side(lr_lean_angle), math.pi/4, angle_lean_left_side(lr_lean_angle))
    p.stepSimulation()