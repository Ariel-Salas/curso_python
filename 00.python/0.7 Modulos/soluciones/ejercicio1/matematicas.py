def calcular_promedio(numeros:list)->float:
    numeros_acumulados=0
    for numero in numeros:
        numeros_acumulados=numeros_acumulados+numero
        promedio=numeros_acumulados/len(numeros)
    return(promedio)