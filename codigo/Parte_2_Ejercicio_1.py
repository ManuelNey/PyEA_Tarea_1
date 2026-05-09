import numpy as np

def simular_X(cantidad_monedas=10):
    monedas = np.random.randint(0, 2, cantidad_monedas)
    x = sum(monedas[i] / (2 ** (i + 1)) for i in range(cantidad_monedas))
    return x


if __name__ == "__main__":
    print(simular_X())