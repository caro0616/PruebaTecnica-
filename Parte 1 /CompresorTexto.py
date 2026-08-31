def CompresorTexto(Texto):
    Comprimido = ""
    ContadorActual = 1  

    for i in range(1, len(Texto)):
        if Texto[i] == Texto[i - 1]:
            ContadorActual += 1
        else:
            Comprimido += Texto[i - 1] + str(ContadorActual)
            ContadorActual = 1  

    Comprimido += Texto[-1] + str(ContadorActual)

    if len(Comprimido) < len(Texto):
        return Comprimido
    else:
        return Texto

print(CompresorTexto("aabcccccaaa"))  
print(CompresorTexto("aaaaaaaaaaa"))  
print(CompresorTexto("abcdefghi"))  