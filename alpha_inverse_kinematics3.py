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
# testing the point is within the workspace or not
    if -2*L2*L3 <= x**2+y**2+z**2 -2*L1*(z-L1)-(L1**2+L2**2+L3**2) <= 2*L2*L3:
        pass
        #print("True solution")
    else:
        #print("Out of space")
        return [0,0,0]
    
# Finding the angle thera 1
    theta1 = atan2(y,x)

# Finding the angle thera 3
    a = x/cos(theta1)
    b = z-L1

    cos3 = (a**2+b**2-L2**2-L3**2)/(2*L2*L3)
    sin3 = sqrt(abs(1-cos3**2))

    theta3a = atan(sin3/cos3)
    theta3a_d=round(180*theta3a/m.pi,2)
    
    theta3b = atan2(sin3,cos3)
    theta3b_d=round(180*theta3b/m.pi,2)
    
    theta3c = atan2(-sin3,cos3)
    theta3c_d=round(180*theta3c/m.pi,2)
    
    #print(theta3a_d,theta3b_d,theta3c_d)
    
# Finding the angle thera 2
    m2 = L3*cos(theta3b)+L2
    n2 = L3*sin(theta3b)
    
    if a!=0 or m2!=0:
        theta2 = atan2(b,a) - atan2(n2,m2)
    else:    
        theta2=0
        print("Detected")
        print(a,n2,cos(theta1),x)
    
 
    theta1_d=round(180*theta1/m.pi,2)
    theta2_d=round(180*theta2/m.pi,2)
    
    return [theta1_d,theta2_d,theta3b_d]
