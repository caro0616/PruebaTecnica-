def LimpiezaCeros(Numeros):
    SinCeros = []
    ContadorCeros = 0

    for Numero in Numeros:
        if Numero != 0:
            SinCeros.append(Numero)  
        else:
            ContadorCeros += 1  

    for i in range(ContadorCeros):
        SinCeros.append(0)

    return SinCeros


print(LimpiezaCeros([0, 1, 0, 3, 12]))  
print(LimpiezaCeros([0, -3, 12]))  
print(LimpiezaCeros([0, 0, 0, 0, 1]))  
print(LimpiezaCeros([0, 0.7, 0.8]))  