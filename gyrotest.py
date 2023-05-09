# LEGO type:standard slot:9 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()

br.MoveTank(.2, 'seconds', -100, -100)

br.AccelGyroDriveForward(64)

#release oil three times
for i in range(3):
    br.LeftMedMotorRunForSeconds(.6, -45)
    br.LeftMedMotorRunForSeconds(.6, 45)

#set up to grab truck
br.GyroTurn(45)
br.MoveTank(-37,'cm',70,70)

br.GyroTurn(-45)

#grab truck/wall

br.MoveTank(11, 'cm', 40,40)

#Wiggle Wiggle
br.MoveTank(2, 'cm', -100,100)
br.MoveTank(-2, 'cm', -100,100)
br.MoveTank(2, 'cm', -100,100)
br.MoveTank(-2, 'cm', -100,100)

br.MoveTank(-2, 'cm', 10,10)
br.MoveTank(-48, 'cm', 50,50)
