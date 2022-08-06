# LEGO type:standard slot:0 autostart

import base_robot_bigwheel
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to


br = base_robot_bigwheel.BaseRobot()
br.debuggingEnabled = True

#back up gently to make sure the robot is square in the jig
#then reset the gyro
#br.driveMotors.move(.5, "seconds", 0, -10)
br.hub.motion_sensor.reset_yaw_angle()

#br.driveMotors.move_tank(40, 'cm', 70, 70)

br.AccelGyroDriveForward(60)
br.TurnRightAndDriveOnHeading(40, 115)

#br.driveMotors.move_tank(60, "cm", 10, 10)
wait_for_seconds(1)

curHead = br.hub.motion_sensor.get_yaw_angle()
print("Robot stopped. Current heading is " + str(curHead))


#raise SystemExit
sys.exit("All done. This is a normal exit.")

