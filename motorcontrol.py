# LEGO type:standard slot:0 autostart

import math
import sys

from spike import (App, Button, ColorSensor, DistanceSensor, ForceSensor,
                   LightMatrix, MotionSensor, Motor, MotorPair, PrimeHub,
                   Speaker, StatusLight)
from spike.control import Timer, wait_for_seconds, wait_until
from spike.operator import (equal_to, greater_than, greater_than_or_equal_to,
                            less_than, less_than_or_equal_to, not_equal_to)
br = PrimeHub()
while True:
    if br.left_button.is_pressed:
        br.light_matrix.set_pixel(1,0,0)
        br.light_matrix.set_pixel(2,0,0)
    else:
        br.light_matrix.set_pixel(1,0,100)
        # br.light_matrix.set_pixel(2)
    #if br.right_button.is_pressed:
        # br.light_matrix.set_pixel(4,0,0)
        # br.light_matrix.set_pixel(5,0,0)
    #else:
        
        # br.light_matrix.set_pixel(1,0,100)
        # br.light_matrix.set_pixel(2,0,100)