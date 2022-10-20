import numpy as np;

a=np.random.randint(1,20,15);
a=a.reshape(3,5);
print(a)
a.shape;
a[np.where(a==np.max(a))]=0;
print(a)