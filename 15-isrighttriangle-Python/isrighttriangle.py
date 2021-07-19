# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
    a1=(x1-x2)
    a2=(y1-y2)
    X=(a1**2)+(a2**2)
    b1=(x2-x3)
    b2=(y2-y3)
    Y=(b1**2)+(b2**2)
    c1=(x1-x3)
    c2=(y1-y3)
    Z=(c1**2)+(c2**2)
    if((X>0 and Y>0 and Z>0)):
        if(X==(Y+Z) or Y==(X+Z) or Z==(X+Y)):
            return True
        else:
            return False  
    else:  
        return False
