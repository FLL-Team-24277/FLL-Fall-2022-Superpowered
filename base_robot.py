import math
import sys

from spike import (App, Button, ColorSensor, DistanceSensor, ForceSensor,
                   LightMatrix, MotionSensor, Motor, MotorPair, PrimeHub,
                   Speaker, StatusLight)
from spike.control import Timer, wait_for_seconds, wait_until
from spike.operator import (equal_to, greater_than, greater_than_or_equal_to,
                            less_than, less_than_or_equal_to, not_equal_to)


class BaseRobot():
    """
    A collection of methods and Spike Prime objects for FLL Team 24277. \
    The BaseRobot class has two drive motors as a MotorPair, two medium \
    motors for moving attachments, and all of the base methods available \
    for Spike Prime sensors and motors. It also includes some custom \
    methods for moving the robot. Enjoy!

    Example:

    >>> import base_robot
    >>> import sys
    >>> br = base_robot.BaseRobot()
    >>> br.AccelGyroDriveForward(40)
    >>> br.GyroTurn(90)
    """
    def __init__(self):
        self.hub = PrimeHub()
        self._version = "2.2 11/22/2022"
        self._leftDriveMotorPort = 'E'
        self._rightDriveMotorPort = 'A'
        self._leftAttachmentMotorPort = 'B'
        self._rightAttachmentMotorPort = 'D'
        self._colorSensorPort = 'F'
        self.driveMotors = MotorPair(self._leftDriveMotorPort, \
            self._rightDriveMotorPort)
        self.debugMode = False
        self.colorSensor = ColorSensor(self._colorSensorPort)
        self.rightMedMotor = Motor(self._rightAttachmentMotorPort)
        self.leftMedMotor = Motor(self._leftAttachmentMotorPort)
        self._tireDiameter = 5.6 #CM
        self._tireCircum = self._tireDiameter * math.pi #CM
        self.hub.motion_sensor.reset_yaw_angle()

    

    def GyroTurn(self, angle):
        """
        Turns the robot to the specified `angle`. 
        Positive numbers turn to the right, negative numbers turn the \
        robot to the left. Note that when the robot makes the turn, it \
        will always overshoot by about seven degrees. In other words if \
        you need a +90 degree turn, you will probably end up commanding \
        something around +83 degrees. You may also want to put a \
        wait_for_seconds(0.2) or something like that after a gyro turn. \
        Just to make sure the robot has stopped moving before continuing \
        with more instructions.
        Parameter
        -------------
        angle: Where the robot should stop turning at. \
            Positive values turn the robot to the right, negative values \
            turn to the left.
        type: float
        values: Any. Best to keep the numbers less than 180, just so the \
            robot doesn't turn more than necessary.
        default: No default value
        """

        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        #Reset Yaw Angle
        MotionSensor().reset_yaw_angle()
        #Tests for angle and debug mode
        if self.debugMode and (angle > 179 or angle < -180):
            sys.exit("GyroTurn() Error: Angle must be between -180 \
                and 180")
        #Sets turn speed
        gyroTurnSpeed = 10
        #Tests if the angle is positive.
        if(angle > 0):
            while(MotionSensor().get_yaw_angle() < angle):
                #If it it is positive it starts turning right.
                self.driveMotors.start_tank(gyroTurnSpeed, -gyroTurnSpeed)
        else:
            while(MotionSensor().get_yaw_angle() > angle):
                #If it it is not positive it starts turning left.
                self.driveMotors.start_tank(-gyroTurnSpeed, gyroTurnSpeed)
        #Stops when it is it has reached the desired angle
        self.driveMotors.stop()
    
    
    def GyroDriveOnHeading(self, distance, heading, maximumSpeed=50):
        """
        Drives the robot very straight on a `Heading` for a \
        `Distance`, using acceleration and the gyro. \
        Accelerates smoothly to prevent wheel slipping. \
        Gyro provides feedback and helps keep the robot pointing \
        on the  heading.
        Minimum distance that this will work for is about 16cm.
        If you need to go a very short distance, use move_tank.
        Parameters
        ----------
        Heading: On what heading should the robot drive (float)
        type: float
        values: any. Best if the `Heading` is close to the current \
            heading. Unpredictable robot movement may occur for large \
            heading differences.
        default: no default value
        Distance: How far the robot should go in cm (float)
        type: float
        values: any value above 25.0. You can enter smaller numbers, but \
            the robot will still go 25cm
        default: no default value
        MaximumSpeed: The speed that the robot will accelerate to and cruise
        type: float
        values: any value between 10 and 100. Anything lower than 11, and \
            the robot won't decelerate.
        default: 50
        See Also
        --------
        Also look at ``AccelGyroDriveFwd()``.
        Example
        -------
        >>> import base_robot
        >>> br = base_robot.BaseRobot()
        >>> br.GyroDriveOnHeading(50, 90) #drive on heading 90 for 50 cm
        """
        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()
        #Sets minimum speed
        minSpeed = 10
        proportionFactor = 1
        # Calculates the amount of rotations in the distance
        # and multiplies it by 360 to make it degrees
        totalDegreesNeeded = distance / self._tireCircum * 360
        MotionSensor().reset_yaw_angle()

        #Sets counted motor port and sets the degrees counted to 0
        testmotor = Motor(self._rightDriveMotorPort)
        testmotor.set_degrees_counted(0)

        #Accel to full speed
        for currentSpeed in range(0, maximumSpeed, 5):
            correction =  heading - self.hub.motion_sensor.get_yaw_angle()
            self.driveMotors.start(steering = correction * \
                proportionFactor, speed = currentSpeed)
            wait_for_seconds(0.1)
        
        #Cruise at full speed
        slowDownPoint = totalDegreesNeeded - 300
        while(testmotor.get_degrees_counted() < slowDownPoint):
            #Print the degrees counted
            #print(str(testmotor.get_degrees_counted()))
            correction = heading - self.hub.motion_sensor.get_yaw_angle()
            self.driveMotors.start(steering = correction * \
                proportionFactor, speed = maximumSpeed)
        
        #Slow down
        for currentSpeed in range(maximumSpeed, minSpeed, -5):
            correction = heading - self.hub.motion_sensor.get_yaw_angle()
            self.driveMotors.start(steering = correction * \
                proportionFactor, speed = currentSpeed)
            wait_for_seconds(0.1)
            
        #Stop
        self.driveMotors.stop()
        wait_for_seconds(0.5)
    
    def AccelGyroDriveForward(self, distance, maximumSpeed=50):
        """
        Drives the robot very straight for `distance`, using \
            acceleration and gyro.
        
        Accelerates to prevent wheel slipping. Gyro keeps the robot \
        pointing on the same heading.
        Minimum distance that this will work for is about 16cm. \
        If you need to go a very short distance, use ``move_tank``.
        Parameters
        ----------
        Distance: How far the robot should go in cm
        type: float
        values: Any value above 16.0. You can enter smaller numbers, but\
            the robot will still go 16cm
        default: No default value
        MaximumSpeed: The speed that the robot will accelerate to and cruise
        type: float
        values: any value between 10 and 100. Anything lower than 11, and \
            the robot won't decelerate.
        default: 50
        Example
        -------
        >>> import base_robot
        >>> br = base_robot.BaseRobot()
        >>> br.AccelGyroDriveForward(20)
        """
        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        # Runs GyroDriveOnHeading with the current gyro yaw angle
        # and the desired distance
        MotionSensor().reset_yaw_angle()
        self.GyroDriveOnHeading(distance, \
            self.hub.motion_sensor.get_yaw_angle(), maximumSpeed)

    def TurnRightAndDriveOnHeading(self, distance, heading, maximumSpeed=50):
        """
        Turns the robot to the right until the `heading` \
        is reached. Then drives on the `heading` until \
        the `distance` has been reached.
        Minimum distance that this will work for is about 16cm. \
        If you need to go a very short distance, use ``GyroTurn`` and \
        move_tank.
        Parameters
        ----------
        heading: On what heading should the robot drive
        type: float
        values: any. However, it must be a heading larger than the \
            current heading (that is, to the right). If a heading is \
            entered that is less than the current heading, the program \
            will exit. default: no default value
        distance: How far the robot should go in cm
        type: float
        values: any value above 16.0. You can enter smaller numbers, but\
            the robot will still go 16cm
        default: no default value
        MaximumSpeed: The speed that the robot will accelerate to and cruise
        type: float
        values: any value between 10 and 100. Anything lower than 11, and \
            the robot won't decelerate.
        default: 50
        Example
        -------
        >>> import base_robot
        >>> br = base_robot.BaseRobot()
        >>> br.TurnRightAndDriveOnHeading(90, 40) #drive heading 90 for\
        40 cm
        """
        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        #Tests for direction and debug mode
        if heading < self.hub.motion_sensor.get_yaw_angle() and \
            self.debugMode:
            sys.exit("TurnRightAndDriveOnHeading Error: Invalid Heading, \
                try using TurnLeftAndDriveOnHeading Method")
        
        MotionSensor.reset_yaw_angle()
        #Turns Right
        self.GyroTurn(heading - self.hub.motion_sensor.get_yaw_angle())
        #Drives on selected Heading
        self.GyroDriveOnHeading(distance, 0, maximumSpeed)

    def TurnLeftAndDriveOnHeading(self, distance, heading, maximumSpeed=50):
        """
        Turns the robot to the left until the `heading` \
        is reached. Then drives on the `heading` until \
        the `distance` has been reached.
        Minimum distance that this will work for is about 16cm. \
        If you need to go a very short distance, use ``GyroTurn`` and \
        move_tank.
        Parameters
        ----------
        heading: On what heading should the robot drive
        type: float
        values: any. However, it must be a heading larger than the current\
            heading (that is, to the left). If a heading is entered that \
            is less than the current heading, the program will exit. \
            default: no default value
        distance: How far the robot should go in cm
        type: float
        values: any value above 16.0. You can enter smaller numbers, but \
            the robot will still go 16cm
        default: no default value
        MaximumSpeed: The speed that the robot will accelerate to and cruise
        type: float
        values: any value between 10 and 100. Anything lower than 11, and \
            the robot won't decelerate.
        default: 50
        Example
        -------
        >>> import base_robot
        >>> br = base_robot.BaseRobot()
        >>> br.TurnLeftAndDriveOnHeading(90, 40) #drive heading 90 for \
        40 cm
        """
        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        #Tests for direction and debug mode
        if heading > self.hub.motion_sensor.get_yaw_angle() and \
            self.debugMode:
            sys.exit("TurnLeftAndDriveOnHeading Error: Invalid Heading, \
                try using TurnRightAndDriveOnHeading Method")
        
        MotionSensor.reset_yaw_angle()
        #Turns Left
        self.GyroTurn(self.hub.motion_sensor.get_yaw_angle() - heading)
        #Drives on selected Heading
        self.GyroDriveOnHeading(distance, 0, maximumSpeed)
    
    def WaitForButtonPress(self):
        """
        Waits until the left button is pressed.
        """
        self.hub.left_button.wait_until_pressed()
        #Checks for abort after incase you want to rerun part of a mission
        if(self.hub.right_button.is_pressed()):
            return()

    def LeftMedMotorRunForDegrees(self, degrees, speed=None):
        """
        Runs the motor for a given number of degrees.
        
        Parameters
        -------------
        degrees : The number of degrees the motor should run.
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : any number
        
        Default : no default value

        -----------------

        speed : The motor's speed
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : -100% to 100%
        
        Default : 50
        
        Errors
        ----------
        TypeError : degrees or speed is not an integer.
        
        RuntimeError : The motor has been disconnected from the Port.
        """

        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        self.leftMedMotor.run_for_degrees(degrees)

    def RightMedMotorRunForDegrees(self, degrees, speed=50):
        """
        Runs the motor for a given number of degrees.
        
        Parameters
        -------------
        degrees : The number of degrees the motor should run.
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : any number
        
        Default : no default value

        -----------------

        speed : The motor's speed
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : -100% to 100%
        
        Default : 50
        
        Errors
        ----------
        TypeError : degrees or speed is not an integer.
        
        RuntimeError : The motor has been disconnected from the Port.
        """

        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        self.rightMedMotor.run_for_degrees(degrees, speed)

    def LeftMedMotorRunForSeconds(self, seconds):
        """
        Runs the motor for a given number of degrees.
        
        Parameters
        -------------
        seconds : The number of seconds the motor should run.
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : any number
        
        Default : no default value

        Errors
        ----------
        TypeError : degrees or speed is not an integer.
        
        RuntimeError : The motor has been disconnected from the Port.
        """

        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        self.leftMedMotor.run_for_seconds(seconds)

    def RightMedMotorRunForSeconds(self, seconds):
        """
        Runs the motor for a given number of degrees.
        
        Parameters
        -------------
        seconds : The number of seconds the motor should run.
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : any number
        
        Default : no default value

        Errors
        ----------
        TypeError : degrees or speed is not an integer.
        
        RuntimeError : The motor has been disconnected from the Port.
        """

        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        self.rightMedMotor.run_for_seconds(seconds)

    def MoveTank(self, amount, unit='cm', left_speed=50, right_speed=50):
        """
        Moves the Driving Base using differential (tank) steering.
        
        The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.
        
        When unit is 'cm' or 'in', the amount of the unit parameter is the horizontal distance that the Driving Base will travel before stopping. The relationship between motor rotations and distance traveled can be adjusted by calling set_motor_rotation().
        
        When 'unit' is 'rotations' or 'degrees', the amount parameter value specifies how much the motor axle will turn before stopping.
        
        When unit is 'seconds', the amount parameter value specifies the amount of time the motors will run before stopping.
        
        If left_speed or right_speed is outside of the allowed range, the value will be set to -100 or 100 depending whether the value is positive or negative.
        
        If one of the speed is negative (left_speed or right_speed), then the motor with that negative speed will run backward instead of forward. If the value of the amount parameter is negative, both motors will rotate backward instead of forward. If both the speed values (left_speed or right_speed) are negative and the value of the amount parameter is negative, then the both motors will rotate forward.
        
        The program will not continue until amount is reached.
        
        Parameters
        -----------------
        amount : The quantity to move in relation to the specified unit of measurement.
        
        Type : float (decimal number)
        
        Values : any value
        
        Default : no default value

        -----------------

        unit : The units of measurement of the amount parameter
        
        Type : string (text)
        
        Values : 'cm','in','rotations','degrees','seconds'
        
        Default : cm

        -----------------

        left_speed : The speed of the left motor
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : -100 to 100
        
        Default : the speed set by set_default_speed()

        -----------------

        right_speed : The speed of the right motor
        
        Type : integer (positive or negative whole number, including 0)
        
        Values : -100 to 100
        
        Default : the speed set by set_default_speed()
        
        
        Errors
        --------------
        TypeError : amount, left_speed or right_speed is not a number or unit is not a string.
        
        ValueError : unit is not one of the allowed values.
        
        RuntimeError : One or both of the Ports do not have a motor connected or the motors could not be paired.
        """
        
        #Checks for abort
        if(self.hub.right_button.is_pressed()):
            return()

        self.driveMotors.move_tank(amount, unit, left_speed, right_speed)

    def GetVersion(self, number):
        return self._version
