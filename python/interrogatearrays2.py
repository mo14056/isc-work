

#question2


import numpy as np

arr = np.array([range(4), range(10, 14)]) #el array originale

print arr

print np.reshape(arr, (2, 2, 2)) #combertirlo en 3D, por eso el hueco

print np.reshape(arr, (4,2)) #cambiar la forma de la tabla, invertida

print np.transpose(arr) #tabla transpuesta

print np.ravel(arr) #everything on a line

print arr.astype(np.float64) #converted to floats






