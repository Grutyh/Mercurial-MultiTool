import random

def calcul_1():
    result = 0
    for i in range(1000):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        temp = a * b
        result += temp
        if temp % 2 == 0:
            result -= temp / 2
        else:
            result += temp * 2
    print(f"Résultat calcul 1: {result}")
    
calcul_1()
