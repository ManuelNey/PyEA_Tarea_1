import time
from Parte_2_Ejercicio_2 import simular_muestra
from Parte_2_Ejercicio_3 import frecuencia_relativa

def comparar_eficiencia():
    valores_n = [10**3, 10**4, 10**5]
    monedas = [10, 50]

    print("=== EJERCICIO 5 ===")

    for m in monedas:
        print(f"\nMonedas: {m}")

        for n in valores_n:
            inicio = time.time()

            muestra = simular_muestra(n, m)
            freq = frecuencia_relativa(muestra)

            fin = time.time()

            print(f"n={n} | freq={freq:.5f} | tiempo={fin - inicio:.4f}s")

    print("\nConclusión:")
    print("Aumentar n mejora más la aproximación que aumentar la cantidad de monedas.")
    print("Aumentar monedas aumenta el costo computacional sin tanta mejora.")


if __name__ == "__main__":
    comparar_eficiencia()