'''
Code for forward kinematics of designed robot
Copyright Yihan LIU
Date 2023.05

Description: This is the code to transform rotational angles of joints 
             to the coordinates of end effector 

Input: Rotational angles of joints
Output: 3D coordinates of end point
'''
import math as m

# Define configuration parameters
L1 = 210
L2 = 170
L3 = 350
L4 = 0
L5 = 0

# Define the math functions
cos = m.cos
sin = m.sin

# Function for forward kinematics
def forward(rotation):
    # Input rotational angles of joints
    theta1 = m.radians(rotation[0])
    theta2 = m.radians(rotation[1])
    theta3 = m.radians(rotation[2])
    theta4 = m.radians(0)
    theta5 = m.radians(0)


    # Calculate the coordinates of end point
    x_end = L2*cos(theta1)*sin(theta2) \
        - L4*sin(theta5)*(sin(theta1)*sin(theta4)+cos(theta4) * (cos(theta1)*sin(theta2+theta3))) \
        + (L4*cos(theta5)+L3)*(cos(theta1)*cos(theta2+theta3))
    
    y_end = L2*sin(theta1)*sin(theta2) \
        - L4*sin(theta5)*(cos(theta1)*sin(theta4)+cos(theta4) * (sin(theta1)*sin(theta2+theta3))) \
        + (L4*cos(theta5)+L3)*(sin(theta1)*cos(theta2+theta3))

    z_end = L2*cos(theta2) - L3*sin(theta2+theta3) - L4*cos(theta5)*sin(theta2+theta3) \
        - L4*cos(theta4)*sin(theta5)*cos(theta2+theta3) + L1 
    
    location = [x_end, y_end, z_end]
    
    return location
