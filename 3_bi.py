import random as rand
import matplotlib.pyplot as plt
import collections

p = 0.7
result = []
for n in range(5000):
    count_a = 0
    for i in range(250):
        a = rand.random()
        if a < p:
            count_a += 1
    result.append(count_a/(i+1))
d = collections.defaultdict(int)
for i in result:
    d[i]+=1
plt.figure(1)
plt.plot(result)
plt.figure(2)
plt.bar([i for i in d.keys()],[i for i in d.values()],width=0.001)
plt.show()