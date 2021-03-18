import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev as sd
from scipy import random
%matplotlib inline

def appx(ax=0, bx=1, ay=0, by=2, N=1500, f=lambda x, y: x*x+y*y):
    samples = []
    for i in range(500):
        x = random.uniform(ax,bx,N)
        y = random.uniform(ay,by,N)
        s = 0
        integral = 0
        for i in range(N):
            s += f(x[i], y[i])
        
        integral = s/float(N)*(bx-ax)*(by-ay)
        samples.append(integral)
    return samples

samples = appx(N=1000)
print(sum(samples)/len(samples))
print(sd(samples))
plt.hist(samples, bins=30, ec='black')
plt.show()
