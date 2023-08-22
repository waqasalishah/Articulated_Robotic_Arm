'''

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

# Define the math functions
cos = m.cos
sin = m.sin

# Function for forward kinematics
def forward(rotation):
    # Input rotational angles of joints
    theta1 = m.radians(rotation[0])
    theta2 = m.radians(rotation[1])
    theta3 = m.radians(rotation[2])    

    # Calculate the coordinates of end point
    x_end = cos(theta1)*(L2*cos(theta2)+L3*cos(theta2+theta3))
    y_end = sin(theta1)*(L2*cos(theta2)+L3*cos(theta2+theta3))
    z_end = L1+L2*sin(theta2)+L3*sin(theta2+theta3)
   
    location = [x_end, y_end, z_end]
    
    return location

