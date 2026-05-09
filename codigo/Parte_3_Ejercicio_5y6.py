
import random
import math
import time


def digitos_correctos(pi_aproximado):
    pi_real = f"{math.pi:.15f}"
    pi_aprox = f"{pi_aproximado:.15f}"

    # Sacamos el punto decimal para comparar todos los dígitos
    pi_real = pi_real.replace(".", "")
    pi_aprox = pi_aprox.replace(".", "")

    correctos = 0

    for real, aprox in zip(pi_real, pi_aprox):
        if real == aprox:
            correctos += 1
        else:
            break

    return correctos

def calcular_x_aleatoriamente(cantMonedas):
    x = 0
    for i in range(cantMonedas):
        es_cara = random.randint(0, 1);
        x += es_cara / (2**(i+1))
    return x

def devolver_XY(numero):
    X = calcular_x_aleatoriamente(numero);
    Y = calcular_x_aleatoriamente(numero);
    return X, Y

def calcular_n_tuplas(n,numero):
    tuplas=[];
    for i in range(n):
        tuplas.append(devolver_XY(numero));
    return tuplas;

def frecuencia_relativa(n,numero):
    favorables = 0
    for _ in range(n):
        x, y = devolver_XY(numero)

        if x**2 + y**2 <= 1:
            favorables += 1
    return favorables / n
    
print(f"Valor real de pi: {math.pi:.10f}\n")
cantidades_monedas = [20, 30, 40, 50, 60]
valores_n = [10**3, 10**4, 10**5, 10**6]
for numero in cantidades_monedas:
    print(numero,"monedas:")
    for n in valores_n:
        inicio = time.time()
        piAprox= frecuencia_relativa(n,numero)*4
        print("Valor n:", n)
        print(piAprox)
        digitos = digitos_correctos(piAprox)
        fin = time.time()
        tiempo = fin-inicio
        print(f"dígitos correctos = {digitos} \n "
              f"tiempo = {tiempo:.4f}s")



