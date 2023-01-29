# LEGO type:standard slot:11 autostart

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

images = (
    (2, 7, 12), (0, 6, 12), (10, 11, 12), (20, 16, 12),
    (22, 17, 12), (24, 18, 12), (12, 13, 14), (4, 8, 12)
)
hub = PrimeHub()

def set_pixels(pixels):
    hub.light_matrix.off()
    for pixel in pixels:
        hub.light_matrix.set_pixel(pixel % 5, pixel // 5)

index = -1
hub.motion_sensor.reset_yaw_angle()
while True:
    yaw = hub.motion_sensor.get_yaw_angle() + 22.5
    if yaw < 0:
        yaw = yaw + 360
    new_index = int(yaw // 45)
    if new_index != index:
        index = new_index
        set_pixels(images[index])