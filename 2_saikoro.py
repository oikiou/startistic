import matplotlib.pyplot as plt
import collections

for n in range(6):
    s = [1,2,3,4,5,6]
    for i in range(n):
        a = [1,2,3,4,5,6]
        s = [i+j for i in a for j in s]
    avg = [i/(n+1) for i in s]
    d = collections.defaultdict(int)
    for i in avg:
        d[i]+=1
#plt.figure(n+1)
plt.bar([i for i in d.keys()],[i for i in d.values()],width=0.05)
plt.show()