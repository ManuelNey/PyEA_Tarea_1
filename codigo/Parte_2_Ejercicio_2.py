from Parte_2_Ejercicio_1 import simular_X

def simular_muestra(n, cantidad_monedas=10):
    return [simular_X(cantidad_monedas) for _ in range(n)]


if __name__ == "__main__":

    muestra = simular_muestra(10)
    #muestra = simular_muestra(10**3)
    #muestra2 = simular_muestra(10**4)
    #muestra3 = simular_muestra(10**5)
    #muestra4 = simular_muestra(10**6)
    print(muestra)