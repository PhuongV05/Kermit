import numpy
import pybullet as p
import pybullet_data
import time

#set environment
p.connect(p.GUI) # gives visualisation
p.resetSimulation()
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.81)
p.setRealTimeSimulation(0)

p.loadURDF("plane.urdf" , [0, 0, 0], [0, 0, 0, 1])
targid = p.loadURDF("quadruped/spider.urdf", [0, 0, 1], [0, 0, 0, 1], useFixedBase = False)
obj_of_focus = targid
FR_leg_angle = p.addUserDebugParameter("FR_leg_angle", 0, 3.14, 0)
FR_feet_angle = p.addUserDebugParameter("FR_feet_angle", 0, 3.14, 0)
FL_leg_angle = p.addUserDebugParameter("FL_leg_angle", 0, 3.14, 0)
FL_feet_angle = p.addUserDebugParameter("FL_feet_angle", 0, 3.14, 0)
RR_leg_angle = p.addUserDebugParameter("RR_leg_angle", 0, 3.14, 0)
RR_feet_angle = p.addUserDebugParameter("RR_feet_angle", 0, 3.14, 0)
RL_leg_angle = p.addUserDebugParameter("RR_leg_angle", 0, 3.14, 0)
RL_feet_angle = p.addUserDebugParameter("RR_feet_angle", 0, 3.14, 0)

numjoints = p.getNumJoints(targid)
print("Number of joints: ", numjoints)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 0,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 1,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 2,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 3,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 4,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)

p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 5,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)
p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 6,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)
p.setJointMotorControl2(
    bodyIndex = targid,
    jointIndex = 7,
    controlMode = p.POSITION_CONTROL,
    targetPosition = 0,
    force = 100
)

while True:
    FR_leg = p.readUserDebugParameter(FR_leg_angle)
    FR_feet = p.readUserDebugParameter(FR_feet_angle)
    FL_leg = p.readUserDebugParameter(FL_leg_angle)
    FL_feet = p.readUserDebugParameter(FL_feet_angle)
    RR_leg = p.readUserDebugParameter(RR_leg_angle)
    RR_feet = p.readUserDebugParameter(RR_feet_angle)
    RL_leg = p.readUserDebugParameter(RL_leg_angle)
    RL_feet = p.readUserDebugParameter(RL_feet_angle)
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 0,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FR_leg,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 1,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FR_feet,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 2,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FL_leg,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 3,
        controlMode = p.POSITION_CONTROL,
        targetPosition = FL_feet,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 4,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RR_leg,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 5,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RR_feet,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 6,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RL_leg,
        force = 100
    )
    p.setJointMotorControl2(
        bodyIndex = targid,
        jointIndex = 7,
        controlMode = p.POSITION_CONTROL,
        targetPosition = RL_feet,
        force = 100
    )

    jointInfo = p.getJointInfo(targid, 1)
    print(round(p.getJointState(targid, jointInfo[0])[0],3))

    p.stepSimulation()