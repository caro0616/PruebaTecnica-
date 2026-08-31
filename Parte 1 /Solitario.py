def ElementoSolitario(numeros):
    conteo = {}

    for numero in numeros:
        if numero in conteo:
            conteo[numero] += 1 
        else:
            conteo[numero] = 1 

    for numero, veces in conteo.items():
        if veces == 1:
            return numero

    return None  


print(ElementoSolitario([4, 1, 2, 1, 2]))  
print(ElementoSolitario([1, 1, 2]))               
print(ElementoSolitario([7]))                                        
print(ElementoSolitario([0, 1, 0]))                
print(ElementoSolitario([-1, 2, 2]))               
print(ElementoSolitario([8, 8, -3, -3, 100]))      