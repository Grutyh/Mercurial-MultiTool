import random

def calcul_1():
    result = 0
    for i in range(1, 1000):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        d = a * b * c
        e = (a + b + c) / 3
        result += e - d
        for j in range(1, 500):
            temp = (a * b) / j
            result += temp
            if j % 5 == 0:
                result -= temp / 2
            else:
                result += temp * 0.5
    return result

calcul_1()
