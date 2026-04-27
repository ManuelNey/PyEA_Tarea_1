from Parte_2_Ejercicio_2 import simular_muestra

def frecuencia_relativa(muestra):
    contador = sum(1 for x in muestra if 2/7 <= x <= 6/7)
    return contador / len(muestra)


def experimento():
    valores_n = [10**3, 10**4, 10**5, 10**6]
    valor_teorico = 4/7
    for n in valores_n:
        muestra = simular_muestra(n, 10)
        freq = frecuencia_relativa(muestra)

        print(f"n = {n}")
        print(f"Frecuencia = {freq}")
        print(f"Error = {abs(freq - valor_teorico)}\n")


if __name__ == "__main__":
    experimento()