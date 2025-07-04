import math

def calcul_1():
    result = 0
    for i in range(1, 1000):
        a = i * 2
        b = i * 3
        c = a + b
        d = math.sqrt(c)
        e = math.pow(c, 3)
        result += d - e
        for j in range(1, 500):
            result += (a + b) / j
            if j % 2 == 0:
                result -= math.log(j)
            else:
                result *= math.sin(j)
    print(f"Résultat calcul 1: {result}")

calcul_1()
