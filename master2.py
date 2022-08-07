# LEGO type:standard slot:3 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()

# Put all of the individual missions in there first. Order doesn't matter

def mission1(): #green
    br.hub.light_matrix.show_image("HOUSE")
    wait_for_seconds(3)

def mission2(): #red
    br.hub.light_matrix.show_image("CHESSBOARD")
    wait_for_seconds(3)

def mission3(): #blue
    br.driveMotors.move(.5, "seconds", 0, -10)
    br.hub.motion_sensor.reset_yaw_angle()

    br.AccelGyroDriveForward(25)
    br.TurnRightAndDriveOnHeading(30, 45)



# Run the missions depending on what color is seen here
validColorList = ['azure','blue','cyan','green','orange','pink','red','violet','yellow','white']
while True:
    while True:
        curColor = br.colorSensor.get_color()
        if curColor in validColorList:
            br.hub.light_matrix.show_image("YES")
            br.hub.status_light.on(curColor)
        else:
            br.hub.light_matrix.show_image("CONFUSED")
            br.hub.status_light.off()
        
        if br.hub.left_button.is_pressed():
            break

        if br.hub.right_button.is_pressed():
            break
    
    if br.colorSensor.get_color() == "green":
        mission1()
    
    if br.colorSensor.get_color() == "red":
        mission2()

    if br.colorSensor.get_color() == "blue":
        mission3()

