import random
import numpy as np
import sklearn
import math
from sklearn.linear_model import LinearRegression
def gendata(a0,ash, m, b, ts):
    tmp = random.randint(0, 3)
    return list(zip(ts, [int(a0 + ash*math.cos((t/m[tmp]+b[tmp]/24)*2*math.pi)) for t in ts]))
def evaluation(data):
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
    tr1 = LinearRegression()
    '''for i in range(1, 168):
        data.append(int(input()))'''
    ts = np.array(data)
    #print(type(ts))
    #print(ts)
    tr1.fit(gendata(a0, ash, m, b, list(range(1,168))), ts)
    preds = tr1.predict(gendata(a0, ash, m, b, list(range(168, 336))))
    print(preds)
    preds = np.round(preds)
    print(preds)
    '''for elem in preds:
        print(elem)'''
    return preds
