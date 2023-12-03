# Una diferencia importante entre las tuplas y las listas es que las tuplas son más rápidas que las listas en términos de eficiencia y rendimiento. 
# Esto se debe a que las tuplas son inmutables, lo que significa que el interprete de Python puede optimizar el uso de la memoria y el acceso a los elementos de la 
# tupla de manera más eficiente que en el caso de las listas.

# En general, se recomienda utilizar tuplas en casos donde se necesite una estructura de datos que no pueda ser 
# modificada, como por ejemplo cuando se quiera representar un conjunto de valores constantes. Por otro lado, se recomienda utilizar listas en casos donde se 
# necesite una estructura de datos que pueda ser modificada, como por ejemplo cuando se quiera almacenar una secuencia de elementos que puedan ser cambiados 
# en el transcurso del programa.

#Enlace de la web: https://stackoverflow.com/questions/14135542/how-is-tuple-implemented-in-cpython

#Las tuplas son ordenadas.
#Las tuplas son inmutables
#Las tuplas permiten valores duplicados.

################### 1.CREACIÓN DE TUPLAS #####################
tupla_vacia = ()
tupla_uno   = ('Arturo','Lorenzo','Hernandez')
tupla_dos   = ('r2d2', 'coder' )


################### 2.INSERTAR Y ACTUALIZAR #####################
#Las tuplas no cuentan con métodos de inserción y actualización puesto que son inmutables, una vez creadas no se pueden cambiar.


################### 3.BORRADOS #####################
 #Borra una tupla de memoria, no se pueden hacer borrados por elemento.

del tupla_vacia

################### 4.OPERACIONES DE TUPLAS #####################
tupla_tres= tupla_uno + tupla_dos   #Unión de tuplas
print(tupla_tres)     
index_arturo= tupla_uno.index('Arturo')
print(f'La posición es: {index_arturo}')  #Devuelve el indice de la primera aparición de ese elemento, en este caso, devuelve 0.
count_coder= tupla_uno.count('Hernandez') #Devuelve el número de aparaciones del elemento que se pasa por parámetro, en este caso, devuelve 1.
print(count_coder)                     

################### 5.OTROS METODOS #####################

                          # Devuelve la longitud de la tupla
                          # Minimo de una lista
                          # Maximo de una lista
                          # Suma los elementos de la lista
                          # Longitud de la lista

################### 6.ACCESO A LOS TUPLAS #####################

# Acceso de forma indexada
print(tupla_uno[0])

# Acceso con intervalos de elementos
print(tupla_uno[1:3])

# Acceso con bucle for
for elemento in tupla_tres:
    print(elemento)
