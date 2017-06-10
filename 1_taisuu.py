import random as rand
import matplotlib.pyplot as plt

for j in range(10):
    count_a = 0
    p = 0.7
    result = []
    for i in range(20000):
        a = rand.random()
        if a < p:
            count_a += 1
        if i % 100 == 0:
            result.append(count_a/(i+1))
    plt.plot(result[1:])
plt.show()