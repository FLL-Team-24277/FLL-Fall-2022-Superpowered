# LEGO type:standard slot:3 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

#####################################
## Master program for all missions ##
#####################################

br = base_robot.BaseRobot()
br.RightMedMotorRunForDegrees(150, 100)
br.WaitForSeconds(.75)
br.RightMedMotorRunForDegrees(-150, 50)
