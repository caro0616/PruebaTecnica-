def NumeroFaltante(Lista, N):
    SumaTotal = 0
    for i in range(1, N + 1):
        SumaTotal += i

    SumaLista = 0
    for Numero in Lista:
        SumaLista += Numero

    return SumaTotal - SumaLista

print(NumeroFaltante([1, 2, 4, 5], 5))  
print(NumeroFaltante([1], 2))  
print(NumeroFaltante([1, 2, 3, 5, 6, 7, 8, 9, 10], 10))  
print(NumeroFaltante([5, 1, 4, 2], 5)) 