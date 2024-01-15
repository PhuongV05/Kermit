# Kermit
8-DOF robot spider

Simulation folder contains code for simulation of various actions using PyBullet. Code is not complicated but also not clean. Somewhat legible in most cases:).

MainSim.py incorporates all motions into a single file and allows user to control the model using a Bluetooth Controller (in this case an Xbox 1 controller).

The model is Spider.urdf.

Robot Working!!!

Walking (Physical/Walk.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/9c5ee6b4-5c21-4a55-8fb6-0c1f3e3dd47c

Moving Up and Down(Physical/MoveUpDown.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/b5a7b6cd-5b74-4130-8471-ab54fb4fc09d

Proposed physical model of robot:

![Proposed Photo](https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/0519eed9-6b5a-4df2-ae5c-85f6b44cad3e)

Move each leg individually using sliders (Simulation/MoveLegs.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/9ea0aa39-d24a-455f-826d-ed903e8b6beb

Lean the robot from side to side using a slider (Simulation/MoveLean.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/2db3876d-97e5-404e-87d3-4731d5d930ea

Move robot up and down using a slider (Simulation/MoveUpDown.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/b22c8587-96be-4c68-99f2-235790c65b3e

Robot waves (Simulation/Action1.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/1d8a0b55-14e4-4dfa-89e6-9bfb4157cade

Robot walks rather chaotically using trot gait where two diagonal legs are raised at a time (Simulation/MoveWalk.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/2ceca2cc-3f5f-40e0-9f53-cf7298ff5e7b

A more controlled walk using a stable gait where one leg lifts at a time (Simulation/MoveWalk2.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/1937dd5d-60fc-4c13-a37b-94bdbd0a037a

Robot turns right using a stable gait (Simulation/TurnRight.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/ce784c8f-dd7d-40d3-86d9-2e2b1341b814

Robot turns left using a stable gait (Simulation/TurnLeft.py)

https://github.com/Ctrl-A-Ctrl-C/Kermit/assets/59261928/99b72242-fb86-42fe-825d-7a775628568f




