# LEGO type:standard slot:0 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to


br = base_robot.BaseRobot()

# Put all of the individual missions in there first. Order doesn't matter

def mission1():
    br.hub.light_matrix.show_image("ANGRY")

def mission2():
    br.hub.light_matrix.show_image("CHESSBOARD")

def mission3():
    br.driveMotors.move(.5, "seconds", 0, -10)
    br.hub.motion_sensor.reset_yaw_angle()

    br.AccelGyroDriveFwd(55)
    br.TurnRightAndDriveOnHeading(85, 50)



# Run the missions in order here

mission1()

br.hub.right_button.wait_until_pressed()
br.hub.right_button.wait_until_released()

mission2()

br.hub.right_button.wait_until_pressed()
br.hub.right_button.wait_until_released()

mission3()

#raise SystemExit
sys.exit(1)

