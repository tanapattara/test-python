import math
#------------------------------------
# Function: distance
# Description: to calculate distance between 2 point
# Parameters:
#   - xa : float, The x coordinates of a point A
#   - ya : float, The y coordinates of a point A
#   - xb : float, The x coordinates of a point B
#   - xb : float, The y coordinates of a point B
# Return: float
#   - diatance between point A and B
#------------------------------------
def distance(xa, ya, xb, yb):
    p = [xa, ya]
    q = [xb, yb]

    result = math.dist(p, q)
    #------------------------------------
    # TODO! write your code here.
    #------------------------------------
    return result

#------------------------------------
# DO NOT CHANGE a function name
#------------------------------------