# LEGO type:standard slot:2 autostart


import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()

# br.AccelGyroDriveForward(70)
# br.GyroTurn(32)
# br.AccelGyroDriveForward(16)
br.rightMedMotor.run_for_degrees(130, -25)
br.rightMedMotor.run_for_degrees(130,25)
br.GyroTurn(90)