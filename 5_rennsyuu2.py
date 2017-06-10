import random
import matplotlib.pyplot as plt
import collections

p = 0.4
s = 10
x = []
for n in range(10000):
    sum = 0
    for i in range(s):
        if random.random() < p:
            sum += 1
        else:
            sum -= 1
    x.append(sum)
print(x)
d = collections.defaultdict(int)
for i in x:
    d[i] += 1
plt.bar([i for i in d.keys()],[i for i in d.values()],width=0.5)
plt.show()