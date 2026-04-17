import random

def calcular_x_aleatoriamente():
    x = 0
    for i in range(10):
        es_cara = random.randint(0, 1);
        x += es_cara / (2**(i+1))
    return x

print(calcular_x_aleatoriamente())