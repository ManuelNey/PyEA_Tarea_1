from Parte_2_Ejercicio_1 import simular_X


def simular_muestra(n, cantidad_monedas=10):
    muestra = []

    for _ in range(n):
        x = simular_X(cantidad_monedas)
        muestra.append(x)

    return muestra


if __name__ == "__main__":
    valores_n = [10**3, 10**4, 10**5, 10**6]

    for n in valores_n:
        muestra = simular_muestra(n, 10)
        print(f"n = {n} | tamaño de la muestra = {len(muestra)}")