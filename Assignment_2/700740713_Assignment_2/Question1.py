import numpy as np


array = np.random.randint(1, 21, 15)
array

#1
array2 = array.reshape((3,5))
array2

#2
print(array2.shape)

#3
np.where(array2 == array2.max(axis = 1)[:,None], 0, array2)

print(array2)