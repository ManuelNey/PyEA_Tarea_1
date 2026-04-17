def calcular_x(resultados):
    x = 0
    for i in range(len(resultados)):
        x += resultados[i] / (2**(i+1))
    return x

print(calcular_x([1,1,1,1,1,1,1,1,1,1]))
print(calcular_x([0,0,0,0,0,0,0,0,0,0]))


def binario(num):
    fin=True
    lista=[]
    result=-1
    while (fin):
        if (result == 0 or result == 1):
            fin = False
            lista.append(result)
            while len(lista)<10:
                lista.append(0)
        else:
            result=num//2;
            resto=num-result*2
            num=int(result)
            lista.append(resto)
    return lista

def combinaciones():
    max=True
    total=[]
    iteracion=0
    while (max):
        sublista=binario(iteracion)
        total.append(sublista)
        iteracion+=1
        if(sublista.count(1)==10):
            max=False
    return(total)


resultados= set()
posibilidades=combinaciones();

for lista in posibilidades:
    resultado=calcular_x(lista)
    resultados.add(resultado)

#Resultado del 4:
print("Cantidad de formas distintas en las que se tiran 10 monedas: ",len(posibilidades))
print("Resultados posibles: ",resultados)
print("Cant resultados posibles: ",len(resultados))