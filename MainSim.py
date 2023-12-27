import pygame
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

pygame.init()

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

def smooth(FRL, FRF, FLL, FLF, RRL, RRF, RLL, RLF, FRL_e, FRF_e, FLL_e, FLF_e, RRL_e, RRF_e, RLL_e, RLF_e):
    curpos = [FRL, FRF, FLL, FLF, RRL, RRF, RLL, RLF]
    endpos = [FRL_e, FRF_e, FLL_e, FLF_e, RRL_e, RRF_e, RLL_e, RLF_e]
    step_length = 7 * (math.pi/180)
    matched = False
    position = 0
    while not matched:
        matching = 0
        jointInfo = p.getJointInfo(targid, position)
        if round(p.getJointState(targid, jointInfo[0])[0],1) == round(endpos[position],1):
            pass
        elif round(p.getJointState(targid, jointInfo[0])[0],1) < round(endpos[position],1):
            curpos[position] += step_length
        elif round(p.getJointState(targid, jointInfo[0])[0],1) > round(endpos[position],1):
            curpos[position] -= step_length
        moving(curpos[0], curpos[1], curpos[2], curpos[3], curpos[4], curpos[5], curpos[6], curpos[7])
        p.stepSimulation()
        time.sleep(0.005)
        position += 1
        if position == 8:
            position = 0
        for i in range(8):
            jointInfo = p.getJointInfo(targid, i)
            if round(p.getJointState(targid, jointInfo[0])[0],1) == round(endpos[i],1):
                matching += 1
        print(matching)
        if matching == 8:
            matched = True

    moving(FRL_e, FRF_e, FLL_e, FLF_e, RRL_e, RRF_e, RLL_e, RLF_e)
    p.stepSimulation()


def wave():
    i = 0
    FRL = 0
    step_length = 1 * (math.pi/180)
    run = True

    smooth(math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, FRL, math.pi, math.pi/4, 0, math.pi/4 * 1.5, math.pi*0.4, math.pi/4 * 1.5, math.pi*0.4)

    while run == True:
        if (i == 240):
            run = False
        if (i<60):
            FRL = FRL + step_length
            moving(FRL, math.pi, math.pi/4, 0, math.pi/4 * 1.5, math.pi*0.4, math.pi/4 * 1.5, math.pi*0.4) 
        elif(60 <= i < 120):
            moving(FRL, math.pi, math.pi/4, 0, math.pi/4 * 1.5, math.pi*0.4, math.pi/4 * 1.5, math.pi*0.4)
        elif(120 <= i < 180):
            FRL = FRL - step_length
            moving(FRL, math.pi, math.pi/4, 0, math.pi/4 * 1.5, math.pi*0.4,math.pi/4 * 1.5, math.pi*0.4)
        elif(180 <= i < 240):
            moving(FRL, math.pi, math.pi/4, 0, math.pi/4 * 1.5, math.pi*0.4, math.pi/4 * 1.5, math.pi*0.4) 
        i += 1
        time.sleep(0.005)
        focus_position, _ = p.getBasePositionAndOrientation(targid)
        p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
        p.stepSimulation()

    smooth(FRL, math.pi, math.pi/4, 0, math.pi/4 * 1.5, math.pi*0.4, math.pi/4 * 1.5, math.pi*0.4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4)


def angle_lean_right_side(lean_angle):
    theta = math.pi/4 - lean_angle
    return theta

def angle_lean_left_side(lean_angle):
    theta = math.pi/4 + lean_angle
    return theta

def lean():
    done = False
    while not done:
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.
        if (joystick.get_button(1) == (1)): # B
            done = True
        axis = joystick.get_axis(0)
        lr_lean_angle = axis * math.pi/6
        moving(math.pi/4, angle_lean_right_side(lr_lean_angle), math.pi/4, angle_lean_left_side(lr_lean_angle), math.pi/4, angle_lean_right_side(lr_lean_angle), math.pi/4, angle_lean_left_side(lr_lean_angle))
        focus_position, _ = p.getBasePositionAndOrientation(targid)
        p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
        p.stepSimulation()
        time.sleep(0.005)

def angle_up_down(height):
    theta = math.pi/2 - math.asin(height/0.5)
    return theta

def height():
    done = False
    while not done:
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.
        if (joystick.get_button(2) == (1)): # B
            done = True
        axis = joystick.get_axis(1)
        height = 0.25 - (axis*0.25)
        moving(math.pi/4, angle_up_down(height), math.pi/4, angle_up_down(height), math.pi/4, angle_up_down(height), math.pi/4, angle_up_down(height))
        focus_position, _ = p.getBasePositionAndOrientation(targid)
        p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
        p.stepSimulation()
        time.sleep(0.005)

def walk():
    step_length = 1 * (math.pi/180)
    FRL = math.pi/2
    FLL = math.pi/4
    RRL = math.pi/4
    RLL = math.pi/2
    i = 0
    done = False
    while not done:
        focus_position, _ = p.getBasePositionAndOrientation(targid)
        p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.
        if (joystick.get_button(3) == (1)): # Y
            done = True
        p.stepSimulation()
        axis = joystick.get_axis(0)
        if axis > 0.5:
            turn_right()
        elif axis < -0.5:
            turn_left()
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
        time.sleep(0.005)

    smooth(FRL, 0,FLL, 0,RRL, 0,RLL, 0, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4)
    
def turn_right():
    step_length = 1 * (math.pi/180)
    FRL = math.pi/4
    FLL = math.pi/4
    RRL = math.pi/4
    RLL = math.pi/4
    i = 0
    moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    done = False
    while not done:
        p.stepSimulation()
        focus_position, _ = p.getBasePositionAndOrientation(targid)
        p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)      
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.       
        axis = joystick.get_axis(0)
        if axis < 0.5:
            done = True
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

def turn_left():
    step_length = 1 * (math.pi/180)
    FRL = math.pi/4
    FLL = math.pi/4
    RRL = math.pi/4
    RLL = math.pi/4
    i = 0
    done = False
    moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
    while not done:
        p.stepSimulation()
        focus_position, _ = p.getBasePositionAndOrientation(targid)
        p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
        for event in pygame.event.get(): # User did something.
            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.       
        axis = joystick.get_axis(0)
        if axis > -0.5:
            done = True  
        if (i == 450):
            i = 0
        if (i<45):
            FRL -= step_length
            moving(FRL, math.pi/4,FLL, 0,RRL, 0,RLL, 0)
        if (45<=i<90):
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        if (90<=i<135):
            RRL += step_length
            moving(FRL, 0,FLL, 0,RRL, math.pi/4,RLL, 0)
        if (135<=i<180):
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        if (180<=i<225):
            RLL -= step_length
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, math.pi/4)
        if (225<=i<270):
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        if (270<=i<315):
            FLL += step_length
            moving(FRL, 0,FLL, math.pi/4,RRL, 0,RLL, 0)
        if (315<=i<360):
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        if (360<=i<405):
            FRL += step_length
            RRL -= step_length
            RLL += step_length
            FLL -= step_length
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        if (405<=i<450):
            moving(FRL, 0,FLL, 0,RRL, 0,RLL, 0)
        i += 1
        time.sleep(0.005)

while not done:
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
        if (joystick.get_button(0) == (1)): # A
            wave()
        if (joystick.get_button(1) == (1)): # B
            lean()
        if (joystick.get_button(2) == (1)): # X
            height()
        if (joystick.get_button(3) == (1)): # Y
            FRL = math.pi/2
            FLL = math.pi/4
            RRL = math.pi/4
            RLL = math.pi/2
            smooth(math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4, math.pi/4,FRL, 0,FLL, 0,RRL, 0,RLL, 0)
            walk()
            
    focus_position, _ = p.getBasePositionAndOrientation(targid)
    p.resetDebugVisualizerCamera(cameraDistance = 3, cameraYaw = 0, cameraPitch = -40, cameraTargetPosition = focus_position)
                
    p.stepSimulation()
    
pygame.close()