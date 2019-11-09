import numpy as np
# 가중치
def WEIGHT(p1, p2):
    x = np.array(p1)
    w = np.array(p2)
    return np.sum(x * w)

# 편향
def BIAS(w, b):
    return w + b

# AND
def AND(param):
    if param <= 0:
        return 0
    else:
        return 1
def NAND(param):
    if param > 0:
        return 1
    else:
        return 0
def OR(param):
    if param <= 0:
        return 0
    else:
        return 1

x = [0,1]
w = [0.5, 0.5]
b = -0.7
or_b = -0.2
print(AND(BIAS(WEIGHT(x,w), b)))
print(OR(BIAS(WEIGHT(x,w),or_b)))


