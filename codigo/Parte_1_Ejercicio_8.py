
from Parte_1_Ejercicio_3 import calcular_x

def binario(num, cantMonedas):
    fin = True
    lista = []
    result = -1
    while fin:
        if (result == 0 or result == 1):
            fin = False
            lista.append(result)
            while len(lista) < cantMonedas:
                lista.append(0)
        else:
            result = num // 2
            resto = num - result * 2
            num = int(result)
            lista.append(resto)

    return lista

def combinaciones(cantMonedas):
    max = True
    total = []
    iteracion = 0
    while(max):
        sublista = binario(iteracion, cantMonedas)
        x = calcular_x(sublista)  
        total.append(x)
        iteracion += 1

        if (sublista.count(1) == cantMonedas):
            max = False

    return total
cantMonedas = [11,12,14,16,18,19]
for i in range(len(cantMonedas)):
    posibilidades = combinaciones(cantMonedas[i])
    
    probabilidad = 1 / (2 ** cantMonedas[i])
    
    esperanza = 0
    varianza = 0
    
    for num in posibilidades:
        esperanza += num * probabilidad

    for num in posibilidades:
        varianza += num ** 2 * probabilidad
    varianza = varianza - esperanza**2

    print("La Esperanza en el caso de que sean ", cantMonedas[i], " monedas es: ", esperanza)
    print("La Varianza en el caso de que sean ", cantMonedas[i], " monedas es : ", varianza)


