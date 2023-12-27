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

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 0,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/2,
    force = 100
    )

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 1,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/4,
    force = 100
    )

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 2,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/4,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 3,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/4,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 4,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/2,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 5,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/4,
    force = 100
)
p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 6,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/4,
    force = 100
)
p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 7,
    controlMode = p.POSITION_CONTROL,
    targetPosition = math.pi/4,
    force = 100
)

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
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 7,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RLF,
        force = 10
    )


"""
def step_1():
    step_length = 1 * (math.pi/180)
    FRL = math.pi/2
    FLL = math.pi/4
    RRL = math.pi/2
    RLL = math.pi/4
    i = 0
    while i < 45:
        FRL = FRL - step_length
        FLL = FLL + step_length
        RRL = RRL - step_length
        RLL = RLL + step_length
        moving(FRL, math.pi/4,FLL, math.pi/4,RRL, math.pi/4,RLL, math.pi/4)
        i += 1
"""

step_length = 1 * (math.pi/180)
FRL = math.pi/2
FLL = math.pi/4
RRL = math.pi/2
RLL = math.pi/4
i = 0
step_1 = True
step_2 = False
while True:
    p.stepSimulation()
    focus_position, _ = p.getBasePositionAndOrientation(targid)
    p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
    if (i == 180):
        i = 0
        if step_1 == True:
            step_1 = False
            step_2 = True
        elif step_2 == True:
            step_2 = False
            step_1 = True
    if (i<45 and step_1 == True):
        FRL = FRL - step_length
        FLL = FLL + step_length
        RRL = RRL - step_length
        RLL = RLL + step_length
        print("Phase 1")
        moving(FRL, math.pi/2,FLL, math.pi/4,RRL, math.pi/4,RLL, math.pi/2)
    elif (45 <= i < 180 and step_1 == True):
        FRL = FRL
        FLL = FLL
        RRL = RRL
        RLL = RLL
        print("Phase 2")
        moving(FRL, math.pi/4,FLL, math.pi/4,RRL, math.pi/4,RLL, math.pi/4)
    elif (i<45 and step_1 == False):
        FRL = FRL + step_length
        FLL = FLL - step_length
        RRL = RRL + step_length
        RLL = RLL - step_length
        print("Phase 3")
        moving(FRL, math.pi/4,FLL, math.pi/2,RRL, math.pi/2,RLL, math.pi/4)
    elif (45 <= i < 180 and step_1 == False):
        FRL = FRL
        FLL = FLL
        RRL = RRL
        RLL = RLL
        print("Phase 4")
        moving(FRL, math.pi/4,FLL, math.pi/4,RRL, math.pi/4,RLL, math.pi/4)
    time.sleep(0.001)
    i += 1