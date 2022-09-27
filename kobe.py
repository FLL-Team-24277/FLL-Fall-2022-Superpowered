# LEGO type:standard slot:0 autostart


import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()

br.AccelGyroDriveForward(60)
br.GyroTurn(32)
br.hub.motion_sensor.reset_yaw_angle()
br.rightMedMotor.run_for_rotations(-0.1, -25)
br.driveMotors.move_tank(16)
br.rightMedMotor.run_for_rotations(0.1, -25)
br.rightMedMotor.run_for_rotations(-0.1, -25)
br.GyroTurn(-30)
br.driveMotors.move_tank(7)
br.GyroTurn(42)
br.AccelGyroDriveForward(16)
br.GyroTurn(42)
br.AccelGyroDriveForward(30)
br.rightMedMotor.run_for_rotations(0.3, -25)