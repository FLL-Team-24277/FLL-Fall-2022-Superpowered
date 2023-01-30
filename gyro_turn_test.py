# LEGO type:standard slot:15 autostart

import sys
import utime
from spike import (MotionSensor, MotorPair)
from spike.control import wait_for_seconds
import gc

logList = []
debugMode = True
_leftDriveMotorPort = 'E'
_rightDriveMotorPort = 'A'
driveMotors = MotorPair(_leftDriveMotorPort,
                                _rightDriveMotorPort)

def Log(topic, msg):
    # Example usage
    # Log("GyroTurn", "Starting a gyro turn")
    t = str(utime.ticks_ms())
    entry = t + " [" + topic + "] " + msg
    logList.append(entry)

    # garbage collect every 25th append
    if (len(logList) % 25 == 0):
        gc.collect()

def WriteLog():
    with open("log2.txt", "a") as f:
        for item in logList:
            # write each item on a new line
            # print("writing " + item)
            f.write("%s\n" % item)
    logList.clear()

def GyroTurn(angle):
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

    # open output file for logging
    if debugMode:
        Log("Gyroturn", "Turning to heading " + str(angle))

    # Reset Yaw Angle
    MotionSensor().reset_yaw_angle()
    # Tests for angle and debug mode
    if debugMode and (angle > 179 or angle < -180):
        sys.exit("GyroTurn() Error: Angle must be between -180 \
            and 180")
    # Sets turn speed
    gyroTurnSpeed = 10
    # Tests if the angle is positive.
    yawAngle = MotionSensor().get_yaw_angle()
    max_loops = 200
    loops = 0
    if (angle > 0):
        driveMotors.start_tank(gyroTurnSpeed, -gyroTurnSpeed)
        while (yawAngle < angle and loops < max_loops):
            # If it it is positive it starts turning right.
            yawAngle = MotionSensor().get_yaw_angle()
            if (debugMode == True):
                Log("Gyroturn", "(" + str(loops) + ") Current heading " + str(yawAngle))
            loops += 1
    else:
        driveMotors.start_tank(-gyroTurnSpeed, gyroTurnSpeed)
        while (yawAngle > angle and loops < max_loops):
            # If it it is positive it starts turning right.
            yawAngle = MotionSensor().get_yaw_angle()
            if (debugMode == True):
                Log("Gyroturn", "(" + str(loops) + ") Current heading " + str(yawAngle))
            loops += 1

    # did we max out on loops?
    if (loops == max_loops):
        Log("Gyroturn", "Aborted; reached max_loops")
    # Stops when it is it has reached the desired angle
    if (debugMode == True):
        Log("Gyroturn", "Calling stop(). Current heading " + str(MotionSensor().get_yaw_angle()))
    driveMotors.stop()
    if (debugMode == True):
        Log("Gyroturn", "stop() has been called. Current heading " + str(MotionSensor().get_yaw_angle()))
    wait_for_seconds(0.5)
    if (debugMode == True):
        Log("Gyroturn", "Final heading " + str(MotionSensor().get_yaw_angle()))

    WriteLog()

GyroTurn(-45)
wait_for_seconds(1)
GyroTurn(45)
