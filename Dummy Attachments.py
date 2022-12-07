# LEGO type:standard slot:13 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()


#################
## Red n' BLck ##
##    Run 1    ##
## Fna Mr.Hugs ##
#################
#Debugged
def mission1():
    br.LeftMedMotorRunForSeconds(0.8, 15)
    br.RightMedMotorRunForSeconds(0.8, -15)
    br.MoveTank( 5, 'cm',50,50)
    br.LeftMedMotorRunForSeconds(0.8, -15)
    br.RightMedMotorRunForSeconds(0.8, 15)
    br.MoveTank( -5, 'cm',100,100)


#################
##Blue and Grey##
##    Run 2    ##
##    Billy    ##
#################
#Debugged
def mission2():
    br.RightMedMotorRunForSeconds(0.8, -30)
    br.MoveTank( 5, 'cm',50,50)
    br.LeftMedMotorRunForSeconds(0.8, -30)
    br.LeftMedMotorRunForSeconds(0.8, 30)
    br.RightMedMotorRunForSeconds(0.8, 30)


#################
##Yellow+ White##
##    Run 3    ##
##  Dr.Gears   ##
#################
#Debugged
def mission3():
    br.LeftMedMotorRunForSeconds(2.5, 30)
    br.MoveTank(5, 'cm', 10,10)
    br.GyroTurn(-50)
    br.GyroTurn(100)
    br.GyroTurn(-50)
    br.MoveTank(-5, 'cm', 10,10)
    br.LeftMedMotorRunForSeconds(2.5, -30)

validColorList = ['azure','blue','cyan','green','orange','pink','red',\
    'violet','yellow','white']
while True:
    while True:
        # Inner loop checks to see what color attachment is installed
        # and provide visual feedback
        # It then checks to see if a button is pressed. If it is,
        # break out of the loop and execute the mission associated
        # with that color
        curColor = br.colorSensor.get_color()
        if curColor in validColorList:
            br.hub.light_matrix.show_image("YES")
            br.hub.status_light.on(curColor)
        else:
            br.hub.light_matrix.show_image("CONFUSED")
            br.hub.status_light.off()
        
        if br.hub.left_button.is_pressed():
            break

    if br.colorSensor.get_color() == "red":
            mission1() # First run; Red n' BLck
            br.WaitForSeconds(.5)
        
    if br.colorSensor.get_color() == "blue":
        mission2() # Blue and Grey
        br.WaitForSeconds(.5)

    if br.colorSensor.get_color() == "yellow":
        mission3() # Oil Yellow+ White
        br.WaitForSeconds(.5)