numeros=list(range(0,11))

numeros_copia=[]
for numero in numeros:    #numero es una variable auxiliar, temporal que solo existira dentro del bucle, que guarde cada elemento de esa lista
    
    numeros_copia.append(numero+1)
print(numeros_copia)     



lista_palabras=['r2d2.coder', 'instragram','tiktok']

for palabra in lista_palabras:
    print(palabra)


suma=50

while suma>0:
    suma=suma-1
    print(suma)
    if suma==20:    
        break



#sintaxis pass

numeros3=list(range(0,100))
for numero3 in numeros:
    pass                   #esto es para que el editor de codigo no de error, y en la parte de pass colocar algo mas adelante



suma4= 50

print('ejercicio numeros pares')
while suma4>0:
    suma4=suma4-1
    if suma4 % 2 !=0:
        continue
    else:
        print(suma4)