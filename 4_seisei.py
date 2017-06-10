import random
import math
import matplotlib.pyplot as plt
import collections

myu = 10
delta = 5
x = []
for n in range(250):
    sum = 0
    for i in range(12):
        sum += random.random()
    a = round(math.sqrt(delta) * (sum - 6) + myu,1)
    x.append(a)
print(x)
d = collections.defaultdict(int)
for i in x:
    d[i]+=1
plt.bar([i for i in d.keys()],[i for i in d.values()],width=0.05)
plt.show()