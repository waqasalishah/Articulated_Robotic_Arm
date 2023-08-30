import math as m

# Define configuration parameters
L1 = 210
L2 = 170
L3 = 350

# Define the math functions
asin = m.asin
acos = m.acos
atan2 = m.atan2
atan = m.atan
sqrt = m.sqrt
cos = m.cos
sin = m.sin

def inverse(position):

    # Input coordinates of end point
    x = position[0]
    y = position[1]
    z = position[2]

    theta1 = atan2(y,x)
    c3 = ((x**2+y**2+z**2-(L1**2+L2**2+L3**2)-2*L1*(z-L1)))/(2*L2*L3)
    s3 = sqrt(1-c3)
    theta3 = atan2(s3,c3)
    
    c1 = sin(theta1)
    s1 = sin(theta1)
    
    theta2 = atan2((z-L1)*(c1-s1),(x-y)) - atan2(s3*L3,(c3*L3+L2))
 
    return [theta1*180/m.pi,theta2*180/m.pi,theta3*180/m.pi]
