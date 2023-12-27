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


numjoints = p.getNumJoints(targid)
print("Number of joints: ", numjoints)

def moving(FRL, FRF, FLL, FLF, RRL, RRF, RLL, RLF):
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 0,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FRL,
        force = 10
        )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 1,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FRF,
        force = 10
        )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 2,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FLL,
        force = 10
    )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 3,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FLF,
        force = 10
    )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 4,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RRL,
        force = 10
    )

    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 5,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RRF,
        force = 10
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 6,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RLL,
        force = 10
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 7,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RLF,
        force = 10
    )

step_length = 1 * (math.pi/180)
FRL = math.pi/4
FLL = math.pi/4
RRL = math.pi/4
RLL = math.pi/4
i = 0
moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
while True:
    p.stepSimulation()
    focus_position, _ = p.getBasePositionAndOrientation(targid)
    p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
    if (i == 450):
        i = 0
    if (i<45):
        FRL += step_length
        moving(FRL, math.pi/4,FLL, 0,RRL, 0,RLL, 0)
    if (45<=i<90):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    if (90<=i<135):
        RRL -= step_length
        moving(FRL, 0,FLL, 0,RRL, math.pi/4,RLL, 0)
    if (135<=i<180):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    if (180<=i<225):
        RLL += step_length
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, math.pi/4)
    if (225<=i<270):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    if (270<=i<315):
        FLL -= step_length
        moving(FRL, 0,FLL, math.pi/4,RRL, 0,RLL, 0)
    if (315<=i<360):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    if (360<=i<405):
        FRL -= step_length
        RRL += step_length
        RLL -= step_length
        FLL += step_length
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    if (405<=i<450):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    i += 1
    time.sleep(0.005)
    