import numpy as np

array = np.random.randint(1, 21, 15)
print(array)

#1
array2=np.reshape(array,(3,5))
print(array2)

#2
print(array2.shape)

#3
array2[np.where(array2==np.max(array2))]=0
maxelement=np.max(array2)
#printing maximum element
print(maxelement)

print(array2)