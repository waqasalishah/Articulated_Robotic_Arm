import time
import RPi.GPIO as GPIO

from alpha_servo import end_effector
from alpha_joint_motion import all_rotation 
from alpha_joint_motion import angle_buff
from alpha_joint_motion import joint_rotation

from alpha_inverse_kinematics import inverse
from alpha_forward_kinematics import forward



# Function to return to home position
def home():all_rotation([0, 0, 0])

# Start of the class
print("Starting and Initializing....")
time.sleep(1)
point = forward([0,0,0])
print(point)