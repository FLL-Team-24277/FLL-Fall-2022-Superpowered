# LEGO type:standard slot:14 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to
br = base_robot.BaseRobot()

br.AccelGyroDriveForward(53)
br.GyroTurn(-26)
br.driveMotors.move_tank(25, 'cm', 50, 50)
wait_for_seconds(.5)
br.driveMotors.start_tank(-35, -35)
wait_for_seconds(.5)
br.driveMotors.start_tank(-80, -100)
wait_for_seconds(3)
br.driveMotors.stop()