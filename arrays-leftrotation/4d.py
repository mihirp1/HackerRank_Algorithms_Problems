

#bin/bash/python
import numpy as np


arr = [1,2,3,4]

new = np.ndarray(arr,axis = 0,shape=2,2)

print(new)

for i in range(2):
    for j in range(2):
     print(new[i][j],i,j)
