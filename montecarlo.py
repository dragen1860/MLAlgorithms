
from __future__ import division
import numpy as np 
ns=nc=1

for i in range(1000000):
	randx=np.random.random()
	randy=np.random.random() 
	if pow(randx,2)+pow(randy,2)<1: 
		nc+=1
	ns+=1
	print 'pi:',4*nc/ns