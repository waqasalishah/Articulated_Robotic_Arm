from gpiozero import AngularServo
import time

# Brown    GND
# Orange   Power
# Yellow   Signal


servo = AngularServo(6,min_angle=0, max_angle=180, min_pulse_width=0.0005,max_pulse_width=0.0025)



def end_effector(servoAngle):
    if servoAngle > 100 or servoAngle < 0:
        servo.angle = 100
    else:
        servo.angle = servoAngle
    return servoAngle




