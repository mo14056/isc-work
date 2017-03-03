

#question 1

import numpy as np #we do this to have access to complicated calculations

a = np.array([range(4), range (10, 14)]) #create 2D array

b = np.array([2,-1,1,0])

print a*b 

# si


b1 = b * 100 #integers

b2 = b * 100.0 #floats

print b1, b2



print b1==b2 #si

print b1.dtype #interrogating why they display differently

print b2.dtype








