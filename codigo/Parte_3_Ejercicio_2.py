#Antes devolvía una tupla (X,Y); ahora devuelvo n tuplas,
#donde n toma los valores 10**3, 10**4, 10**5 y 10**6

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

def calcular_n_tuplas(n):
    tuplas=[];
    for i in range(n):
        tuplas.append(devolver_XY());
    return tuplas;

print("n=10**3",calcular_n_tuplas(10**3));
print("n=10**4",calcular_n_tuplas(10**4));
print("n=10**5",calcular_n_tuplas(10**5));
print("n=10**6",calcular_n_tuplas(10**6));
