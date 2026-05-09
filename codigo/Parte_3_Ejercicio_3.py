"""La frecuencia relativa es:
 casos en los que se cumple X**2 +Y**2 <=1
 ___________________________________________ (dividido)
 casos totales (es decir la cantidad de tuplas totales)
"""
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

def frecuencia_relativa(n):
    favorables=0;
    tuplas=calcular_n_tuplas(n);
    for tupla in tuplas:
        X=tupla[0];
        Y=tupla[1];
        calculo=X**2+Y**2;
        if calculo <=1:
            favorables += 1;
    return favorables/n;

print(frecuencia_relativa(10**4));
"""
Siempre da de resultado 0.7 algo o 0.8 algo , ya que pi/4 da aproximadamente 0.785

En la segunda parte tengo que el valor que me dió frecuencia_relativa
 multiplicarlo * 4, y ver si se parece a pi, esto tendría que tener sentido, ya que como
 se mencionó anteriormente los valores de frecuencia_relativa rondan entre 0.7 algo y
 0.8 algo, lo cual es pi/4.
Entonces, en teoría , si frecuencia_relativa se aproxima a pi/4, se va a cumplir
 frecuencia_relativa * 4 se aproximará a pi.

Decidimos probarlo 4 veces con valores 10^n distintos para ver si se cumple
"""
print(frecuencia_relativa(10**3)*4);
print(frecuencia_relativa(10**4)*4);
print(frecuencia_relativa(10**5)*4);
print(frecuencia_relativa(10**6)*4);