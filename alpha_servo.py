import time
import RPi.GPIO as GPIO


#Define the Pin of the Servo
Servo_pin = 12

#Setting up the pin 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Servo_pin,GPIO.OUT)


#Setting the GPIO as PWM output
Duty = GPIO.PWM(Servo_pin,50)


def end_effector(sw):
    Duty.start(0)
    if sw<1:
        sw=1
    elif sw>6:
        sw=6     
    Duty.ChangeDutyCycle(sw)
    time.sleep(0.1)
    return sw




