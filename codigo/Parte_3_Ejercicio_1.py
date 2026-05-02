import random

def calcular_x_aleatoriamente():
    x = 0
    for i in range(10):
        es_cara = random.randint(0, 1);
        x += es_cara / (2**(i+1))
    return x

def devolver_XY():
    X = calcular_x_aleatoriamente();
    Y = calcular_x_aleatoriamente();
    return X, Y

resultado= devolver_XY();
print(resultado)