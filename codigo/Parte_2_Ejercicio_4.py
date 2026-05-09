import time
from Parte_2_Ejercicio_2 import simular_muestra
from Parte_2_Ejercicio_3 import frecuencia_relativa

def experimento_monedas():
    cantidades_monedas = [20, 30, 40, 50, 60]
    valores_n = [10**3, 10**4, 10**5, 10**6]
    valor_teorico = 4/7

    for m in cantidades_monedas:
        print(f"\nCantidad de monedas: {m}")

        for n in valores_n:
            inicio = time.time()

            muestra = simular_muestra(n, m)
            freq = frecuencia_relativa(muestra)

            fin = time.time()

            print(f"n = {n} | freq = {freq:.5f} | "
                  f"error = {abs(freq - valor_teorico):.5f} | "
                  f"tiempo = {fin - inicio:.4f}s")


if __name__ == "__main__":
    experimento_monedas()