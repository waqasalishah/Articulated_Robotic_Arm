import RPi.GPIO as GPIO
import time

from alpha_servo import end_effector
from alpha_joint_motion import all_rotation 
from alpha_joint_motion import angle_buff
from alpha_joint_motion import joint_rotation


# Function to return to home position
def home():all_rotation([0, 0, 0])


# Start of the class
print("Starting and Initializing....")
time.sleep(1)


    
while True:
    i = int(input("Enter the rotation of J1: "))
    j = int(input("Enter the rotation of J2: "))
    k = int(input("Enter the rotation of J3: "))
    angles = [i,j,k]
    
    all_rotation(angles)
    
    print("Waiting at destination for 5 seconds....")
    time.sleep(5)
    
    i = int(input("Enter the end effector angle: 0 to 90 "))
    end_effector(i)
    time.sleep(1)
    
    print("Moving to home position....")
    home()
    
    