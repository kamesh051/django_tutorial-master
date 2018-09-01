import numpy as np
import time
import os

size = int(input("enter size:"))

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

#python list
start = time.time()
sum1 = [(x+y) for x,y in zip(l1,l2)]
print("python list took",(time.time()-start)*1000)

#array
start = time.time()
sum1 = a1+a2
print("python array took",(time.time()-start)*1000)
