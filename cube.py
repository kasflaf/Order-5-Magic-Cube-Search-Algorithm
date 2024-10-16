import random as r
import function as f
import time as t
# import numpy as np
import steepest as st
import obj as o
import sideways as sid


start = t.time()
arr = [0]*125
for i in range(0,125) :
    arr[i]=i+1
# cube = np.array(np.arange(1,126),dtype=np.int16)
print(type(arr[1]))
r.shuffle(arr)
f.printArray(arr)
print()
print()

# f.successor(cube,1,2)
# print()
# f.printArray(cube)
neighbor = st.steepest(arr)
print()
f.printArray(neighbor)
print()
end=t.time()
print()
print("time elapsed: "+ str(end-start))




