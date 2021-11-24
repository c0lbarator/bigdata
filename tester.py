import math
import random
from reshenie import *
from sklearn.metrics import accuracy_score
a0 = 0
ash = 0
for i in range(4):
    tmp = random.randint(0, 5)
    ash += tmp
    if i == 0:
        a0 = tmp
ni = random.randint(0, 3)
b = [0, 0, 0, 0]
for i in range(4):
    if i >= ni:
        b[i] = 0
    else:
        b[i] = random.randint(0, 5)
m = [12, 24, 168, 672]
on_input = []
test = []
for t in range(1, 168):
    tmp = random.randint(0, 3)
    on_input.append(int(a0 + ash * math.cos((t / m[tmp] + b[tmp] / 24) * 2 * math.pi)))
for t in range(168, 336):
    tmp = random.randint(0, 3)
    test.append(int(a0 + ash * math.cos((t / m[tmp] + b[tmp] / 24) * 2 * math.pi)))
test = np.array(test)
print(test)
print(accuracy_score(test, evaluation(on_input)))