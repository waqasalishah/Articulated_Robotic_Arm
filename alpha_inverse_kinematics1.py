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
    
    k1 = c3*L3 + L2
    k2 = s3*L3
    
    A = -2*k1*(L1-z)
    B = (2*k1*(L1-z))**2-4*(k1**2+k2**2)*(z**2+L1**2-k2**2-2*z*L1)
    
    theta2 = asin((A+sqrt(B))/(2*(k1**2+k2**2)))

 
    return [theta1*180/m.pi,theta2*180/m.pi,theta3*180/m.pi]
