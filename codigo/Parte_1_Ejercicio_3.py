def calcular_x(resultados):
    x = 0
    for i in range(len(resultados)):
        x += resultados[i] / (2**(i+1))
    return x

print(calcular_x([1,1,1,1,1,1,1,1,1,1]))


print(calcular_x([0,0,0,0,0,0,0,0,0,0]))