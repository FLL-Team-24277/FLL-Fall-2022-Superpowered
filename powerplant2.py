# LEGO type:standard slot:8 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()

br.MoveTank(70, 'cm', 55, 50)
br.RightMedMotorRunForDegrees(360, 40)
br.WaitForSeconds(1)
br.RightMedMotorRunForDegrees(-360,20)
br.WaitForSeconds(.5)
br.MoveTank(-70, 'cm', 100, 100)