#####################
##   TV, WINDMILL  ##
##       Run 5     ##
## Cleveland, Toby ##
#####################
def mission5():

    # First put the truck in the ellipse
    # New COmment from zack
    br.WaitForSeconds(.5)
    br.MoveTank(78, "cm", 100, 100)
    br.MoveTank(-78, "cm", 100, 100)
    # tv mission
    br.WaitForButtonPress()
    br.MoveTank(46,"cm",50,50)
    br.MoveTank(-36,"cm",50,50)
    # After returning to launch area, place the robot in the
    # launch spot by hand, and then press the left button
    # to continue

    # Send to the car mission,

    br.WaitForButtonPress()
    br.AccelGyroDriveForward(30)
    br.GyroTurn(-35)
    br.AccelGyroDriveForward(72)
    br.MoveTank(1, "seconds", 5, -5)
    br.MoveTank(.5, "seconds", -5, 5)
    br.RightMedMotorRunForDegrees(480)
    br.RightMedMotorRunForDegrees(-480)
    br.MoveTank(.5, "seconds", -5, 5)
    
    # # back to home
    br.GyroTurn(-20)
    br.MoveTank(-100, "cm", 100, 100)
    

    # Windmill variables
    br.WaitForButtonPress()
    
    br.MoveTank(10,"cm", 50,50)
    br.RightMedMotorRunForDegrees(300)
    br.GyroTurn(-20)
    br.MoveTank(60,"cm",100,100)
    br.GyroTurn(60)
    delay= 0.5
    rammingspeed=50
    t = 1 #seconds
    dist = 4

    

    # operate the windmill three times
    for i in range(3):
        br.MoveTank(amount=t, unit= "seconds", \
            left_speed=rammingspeed, right_speed=rammingspeed)
        br.WaitForSeconds(delay)
        br.MoveTank(dist, unit= "cm", left_speed = \
            -rammingspeed, right_speed=-rammingspeed)
        br.WaitForSeconds(delay)
    
    br.MoveTank(-10)
    
    br.GyroTurn(100)
    
    br.MoveTank(78,"cm",100,100)
