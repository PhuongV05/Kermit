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
FRL = math.pi/2
FLL = math.pi/4
RRL = math.pi/4
RLL = math.pi/2
i = 0
pause = True
moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
while True:
    p.stepSimulation()
    focus_position, _ = p.getBasePositionAndOrientation(targid)
    p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
    if (i == 450):
        i = 0
    else: 
        pass
    if (i<45):
        RRL = RRL + step_length
        moving(FRL, 0,FLL, 0,RRL, math.pi/4,RLL, 0)
    elif (45<=i<90):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0) 
    elif (90<=i<135):
        FRL = FRL - step_length
        moving(FRL, math.pi/4,FLL, 0,RRL, 0,RLL,0)
    elif (135<=i<180):
        moving(FRL, 0,FLL,0,RRL, 0,RLL, 0) 
    elif (180<=i<225):
        FRL = FRL + step_length
        FLL = FLL + step_length
        RRL = RRL - step_length
        RLL = RLL - step_length
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0) 
    elif (225<=i<270):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0) 
    elif (270<=i<315):
        RLL = RLL + step_length
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, math.pi/4) 
    elif (315<=i<360):
        moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0) 
    elif (360<=i<405):
        FLL = FLL - step_length
        moving(FRL, 0, FLL, math.pi/4, RRL, 0,RLL, 0) 
    elif (405<=i<450):
        moving(FRL, 0, FLL, 0, RRL, 0, RLL, 0)
    i += 1
    time.sleep(0.001)
