# LEGO type:standard slot:0 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to


br = base_robot.BaseRobot()
br.hub.motion_sensor.reset_yaw_angle()

br.AccelGyroDriveForward(27) # must be over 25
#br.driveMotors.move_tank(36, "cm", 50, 50)
#br.TurnRightAndDriveOnHeading(distance=30, heading=45)
#br.TurnRightAndDriveOnHeading(distance=20, heading=45)

# br.hub.light_matrix.show_image("ARROW_S")
# br.leftMedMotor.run_for_seconds(2, 100)
# br.leftMedMotor.run_for_seconds(2, -100)
# br.leftMedMotor.set_stop_action("coast")
# br.leftMedMotor.stop()

# br.hub.light_matrix.show_image("ARROW_N")
# br.rightMedMotor.run_for_degrees(speed=50, degrees=200)
# br.rightMedMotor.run_for_rotations(2.2, 60)
# br.rightMedMotor.set_stop_action("hold")
# br.rightMedMotor.stop()
# br.hub.motion_sensor.reset_yaw_angle()
# br.GyroTurn(-87) # turn to the right 90 degrees
# br.hub.motion_sensor.reset_yaw_angle()
# br.GyroTurn(87) # turn to the right 90 degrees

# br.GyroTurn(-45) # turn to the left 45 degrees

# #back up gently to make sure the robot is straight (like wall squaring)
# #then reset the gyro
# br.driveMotors.move(amount=1, unit="seconds", steering=0, speed=-15)
# br.hub.motion_sensor.reset_yaw_angle() # reset the gyro after squaring

# br.driveMotors.move_tank(40, 'cm', 70, 70)

# br.AccelGyroDriveForward(50)
# br.TurnRightAndDriveOnHeading(45, 110)
br.TurnLeftAndDriveOnHeading(distance=35, heading=45)

# br.driveMotors.move_tank(60, "cm", 10, 10)
wait_for_seconds(0.2)

curHead = br.hub.motion_sensor.get_yaw_angle()
print("Robot stopped. Current heading is " + str(curHead))


