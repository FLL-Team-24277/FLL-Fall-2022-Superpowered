# LEGO type:standard slot:5 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

#####################################
## Master program for all missions ##
#####################################

br = base_robot.BaseRobot()

# Put all of the individual missions in there first. Order doesn't matter

#################
## POWER PLANT ##
##    Run 1    ##
##    Zack     ##
#################
def mission1(): #violet
    

    #reseting arms to ensure they are in the perfect position
    br.rightMedMotor.set_stop_action('coast')
    br.rightMedMotor.run_for_seconds(1.2, -50)
    br.rightMedMotor.stop()
    br.Wait_for_seconds(.5)
    br.RightMedMotorRunForDegrees(197, 50)

    # Arms are reset... now wait for 3, 2, 1, lego!
    br.WaitForButtonPress()
    #driving to mission
    br.MoveTank(66, 'cm', 50, 48)
    # doing mission
    br.RightMedMotorRunForDegrees(270,100)
    br.MoveTank(1.5,'cm', 45,45)
    br.RightMedMotorRunForSeconds(2,-55)
    br.Wait_for_seconds(.5)
    #going back to base
    br.MoveTank(70,"cm",-100,-100)




##################
## OIL REFINERY ##
##    Run 3     ##
##     Sam      ##
##################
def mission3(): #Red
    

    br.AccelGyroDriveForward(62)

    #release oil three times
    for i in range(3):
        br.LeftMedMotorRunForSeconds(.6, -45)
        br.LeftMedMotorRunForSeconds(.6, 45)

    #set up to grab truck
    br.GyroTurn(45)
    br.MoveTank(-37,'cm',70,70)
    
    br.GyroTurn(-45)
    #grab truck/wall
    
    br.MoveTank(-50, 'cm',50,50)
    
    br.MoveTank(41, 'cm',45,45)
    
    br.RightMedMotorRunForSeconds(1, -10)
    br.MoveTank(-50, 'cm',50,50)

    br.WaitForButtonPress()

    #east end drive

    
    br.MoveTank(180, 'cm', 100, 100)



#####################
##    SOLAR FARM   ##
##      Run 4      ##
##      Jonas      ##
#####################
def mission4():
    #Drive 70 centimeters
    br.AccelGyroDriveForward(70)
    br.GyroTurn(90)
    #Drive backwards 20 centimeters
    br.MoveTank(-20, 'cm', 50, 50)
    #Turn 6 degrees to the left
    br.GyroTurn(-6)
    #Extend Attachment
    br.LeftMedMotorRunForSeconds(2.7,100)
    #Drive 35 centimeters
    br.AccelGyroDriveForward(35)
    #Retract Attachment
    br.LeftMedMotorRunForSeconds(2.7,-100)
    #Drive back
    br.MoveTank(.7, 'rotations', -100, -50)
    br.MoveTank(5, 'rotations', -100, -100)



#####################
##   TV, WINDMILL  ##
##       Run 5     ##
## Cleveland, Toby ##
#####################
def mission5():

    # First put the truck in the ellipse
    
    br.Wait_for_seconds(.5)
    br.MoveTank(78, "cm", 100, 100)
    br.MoveTank(-78, "cm", 100, 100)

    # After returning to launch area, place the robot in the
    # launch spot by hand, and then press the left button
    # to continue
    br.WaitForButtonPress()
    br.MoveTank(46, "cm", 50,50)
    br.MoveTank(-31, "cm", 50,50)
    
    br.wait_for_seconds(.5)
    br.GyroTurn(-40)
    
    br.MoveTank(85, "cm", 50,50)
    br.RightMedMotorRunForDegrees(720,400) 
    
    br.RightMedMotorRunForDegrees(-720,400)
    br.MoveTank(-27, "cm", 50,50)
    
    br.RightMedMotorRunForDegrees(720,400)
    br.GyroTurn(80)

    # Windmill variables
    delay = 0.5
    rammingspeed=30
    t = 1 #seconds
    dist = 4

    br.MoveTank(23, "cm", 50, 50)
    

    # operate the windmill three times
    for i in range(3):
        br.MoveTank(amount=t, unit= "seconds", \
            left_speed=rammingspeed, right_speed=rammingspeed)
        br.wait_for_seconds(delay)
        br.MoveTank(dist, unit= "cm", left_speed = \
            -rammingspeed, right_speed=-rammingspeed)
        br.wait_for_seconds(delay)

    br.MoveTank(-10)
    
    br.GyroTurn(100)
    
    br.AccelGyroDriveForward(100)


#################
## TOY FACTORY ##
##    Run 6    ##
##     Bea     ##
#################
def mission2(): #Yellow
    
    br.AccelGyroDriveForward (distance=50)
    br.MoveTank(-10, 'cm', 50, 50)
    br.LeftMedMotorRunForSeconds(1.5)
    br.MoveTank(-35, 'cm', 50, 50)




##########################################
##########################################
###            MASTER PROGRAM          ###
##########################################
##########################################


# Run the missions depending on what color is seen here
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

        if br.hub.right_button.is_pressed():
            break
    
    # Outer loop. When we get here, it's because we pressed a button
    # and broke out of the inner loop. Now execute the mission for the
    # color of the attachment. When the mission is done executing,
    # loop back into the inner loop and do it all again
    if br.colorSensor.get_color() == "violet":
        mission1() # First run; Power Plant
        
        br.wait_for_seconds(.5)
    
    if br.colorSensor.get_color() == "yellow":
        mission2() # Toy Factory
        
        br.wait_for_seconds(.5)

    if br.colorSensor.get_color() == "red":
        mission3() # Oil Refinery
        
        br.wait_for_seconds(.5)

    if br.colorSensor.get_color() == "green":
        mission4() # Solar farm
        
        br.wait_for_seconds(.5)

    if br.colorSensor.get_color() == "blue":
        mission5() # Pick up north energy units
        
        br.wait_for_seconds(.5)
