################### EJERCICIOS DE FUNCIONES #####################

################### EJERCICIO 1 #####################

# 1.Crea una función llamada "calcular_impuestos" que reciba dos argumentos: "ingresos" (int) y "tasa_impuestos" (float) y retorne los impuestos a pagar (float)
#   (por ejemplo: calcular_impuestos(50000, 0.25))
# 2.Dentro de la función, calcula el impuesto debido multiplicando los ingresos por la tasa de impuestos y guarda el resultado en una variable "impuesto_debido".
# 3.Retorna el valor de "impuesto_debido".
# 4.Crea una variable "ingresos" con el valor de tus ingresos anuales (por ejemplo: 75000)
# 5.Crea una variable "tasa_impuestos" con el porcentaje de impuestos que debes pagar (por ejemplo: 0.3)
# 6.Crea una variable "impuesto_a_pagar" que sea igual a la función "calcular_impuestos" con los argumentos "ingresos" y "tasa_impuestos".
# 7.Imprime "Impuesto a pagar: " y el valor de "impuesto_a_pagar".



def calcular_impuestos(ingresos: int, tasa_impuestos: float)-> float:
    impuesto_debido =ingresos*tasa_impuestos
    return impuesto_debido

ingresos=75000
tasa_impuestos=0.3
impuesto_a_pagar= calcular_impuestos(ingresos,tasa_impuestos)

print(f'El impuesto a pagar será de {impuesto_a_pagar} y el valor de los impuestos es {tasa_impuestos}')


################### EJERCICIO 2 #####################

# 1.Crea una función llamada "calcular_promedio" que reciba una lista de números como argumento llamada "numeros" y retorne el promedio (float).
# 2.Dentro de la función, calcula el promedio de los números en la lista y guarda el resultado en una variable "promedio".
# 3.Retorna el valor de "promedio".
# 4.Crea una lista de números con las calificaciones obtenidas en un curso (por ejemplo: [9, 8, 10, 7, 8, 9, 6, 8, 10, 9])
# 5.Llama a la función "calcular_promedio" con la lista de calificaciones como argumento y guarda el resultado en una variable "promedio_curso"
# 6.Imprime "El promedio del curso es: " y el valor de "promedio_curso"


def calcular_promedio(numeros:list)->float:
    numeros_acumulados=0
    for numero in numeros:
        numeros_acumulados=numeros_acumulados+numero
        promedio=(numeros_acumulados/len(numeros))
    return(promedio)
    

calificaciones=[9, 8, 10, 7, 8, 9, 6, 8, 10, 9]
promedio_curso=calcular_promedio(calificaciones)
print(f'El promedio de las notas de tu curso es {promedio_curso} ')



################### EJERCICIO 3 #####################

# 1.Crea una función llamada "calcular_costo_envio" que reciba dos argumentos: "origen" (str) y "destino" (str) y retorne el precio (int) 
#   (por ejemplo: calcular_costo_envio("Nueva York", "Los Ángeles"))
# 2.Dentro de la función, crea un diccionario con los costos de envio entre diferentes ciudades 
#   (por ejemplo: {"Nueva York": {"Los Ángeles": 20, "Chicago": 10, "Miami": 15}, "Los Ángeles": {"Nueva York": 25, "Chicago": 17, "Miami": 20}})
# 3.Usa los argumentos "origen" y "destino" para obtener el costo de envio entre esas dos ciudades del diccionario y guarda el resultado en una variable "costo"
# 4.Retorna el valor de "costo"
# 5.Crea una variable "origen" con el lugar de origen del envio (por ejemplo: "Nueva York")
# 6.Crea una variable "destino" con el lugar de destino del envio (por ejemplo: "Los Ángeles")
# 7.Llama a la función "calcular_costo_envio" con las variables "origen" y "destino" como argumentos y guarda el resultado en una variable "costo_envio"
# 8.Imprime "El costo de envio desde " + origen + " hasta " + destino + " es de: " + costo_envio


def calcular_costo_envio(origen:str, destino:str)-> int:
    informacion_costo={"Nueva York": {"Los Ángeles": 20, "Chicago": 10, "Miami":15}, "Los Ángeles": {"Nueva York": 25, "Chicago": 17, "Miami": 20}}
    informacion_destino=informacion_costo.get(origen,{})
    costo_destino=informacion_destino.get(destino,f'Lo siento no hay ruta posible')
    return costo_destino

origen='Auckland'
destino='los angeles'

costo_envio=calcular_costo_envio(origen,destino)
print(f'el costo de envio desde {origen } a {destino} es de: {costo_envio}')



def calcular_envio2(origen, destino)->float:
    informacion_costo={'nueva york':{'los angeles':50}, 'los angeles':{'nueva york':40}}
    informacion_destino=informacion_costo.get(origen,{})
    costo_destino=informacion_destino.get(destino, f'Lo siento tu ruta no esta disponible por el momento')
    return costo_destino

origen='nueva york'
destino='los angeles'

costo_envio=calcular_envio2(origen,destino)
print(f'El costo de tu envio es de {costo_envio}')



################### EJERCICIO 4 #####################

# 1.Crea una función llamada "convertir_moneda" que convierta dolares a otra moneda. 
#   La función recibe como argumento "cantidad_dolares" (int) y otro argumento opcional "moneda_destino" donde moneda_destino tiene como valor por defecto "euros", 
#   retorna un valor tipo float.
# 2. Dentro de la funcion crear un diccionario llamado "tasas_cambio" con estos valores: 'euros': 0.91, 'yenes': 106.23, 'libras': 0.77.
# 3. Crea una variable llamada "cantidad_destino" que guarde el valor de "cantidad_dolares" convertida a la moneda destino. Retorna "cantidad_destino"
# 4. Crea una variable llamada "dolares" con una cantidad; por ejemplo 1000.
# 5. Llama a la función "convertir_moneda" con "dolares" y "yenes" como parámetros y guarda el resultado en una variable llamada "yenes".
# 6. Imprime el valor de la variable "yenes".


def convertir_moneda(cantidad_dolares, moneda_destino='euros')->float:
    tasas_cambio = {'euros': 0.91, 'yenes': 106.23, 'libras': 0.77,'dolares': 1.0}
    cantidad_destino = cantidad_dolares * tasas_cambio[moneda_destino]
    return cantidad_destino

dolares = 1000
yenes = convertir_moneda(dolares,'yenes')
print(yenes)


################### EJERCICIO 5 #####################

# 1.Crea una función llamada "aplicar_descuento" para comprar un producto en distintas divisas y con posibles descuentos,
#   que reciba como argumentos "producto" (str), "moneda" (str) como argumento opcional y argumentos **kwargs con productos como key y value siendo un diccionario con el precio 
#   del producto y el descuento a aplicar. 
#   (Ejemplo de uso de la función -> aplicar_descuento('zapatos','euros',zapatos={"precio": 12.99, "descuento": 0.1},
    # collar={"precio": 9.99, "descuento": 0.2},
    # pulsera={"precio": 19.99, "descuento": 0.15},
    # gafas={"precio": 29.99, "descuento": 0.25})
# 2.La función debe calcular el precio final en base a los argumentos recibidos. Si se especifica un descuento, debe aplicarlo al precio. 
# 3.Si se especifica una moneda diferente a la predeterminada, debe convertir el precio al valor en la moneda especificada, 
#   con la función realizada en el Ejercicio 6 llamada "convertir_moneda".
# 5.Usa la función "aplicar_descuento" para calcular el precio final de varios productos con diferentes argumentos opcionales.
# 6.Asegúrate de manejar el caso en el que no se pase ningún parámetro key-value.

def aplicar_descuento(producto:str, moneda='dolares', **descuentos_kwargs) -> float:
    if descuentos_kwargs and producto in descuentos_kwargs.keys():
        precio = descuentos_kwargs[producto]['precio']
        descuento = descuentos_kwargs[producto]['descuento']
        precio_con_cambio = convertir_moneda(precio,moneda)
        precio_con_descuento = precio - (precio_con_cambio * descuento)
        return precio_con_descuento
    return -1 #indica que estos parametos opcionales no se han pasado
    

precio_final = aplicar_descuento('zapatos','euros',zapatos={"precio": 12.99, "descuento": 0.1},
    collar={"precio": 9.99, "descuento": 0.2},
    pulsera={"precio": 19.99, "descuento": 0.15},
    gafas={"precio": 29.99, "descuento": 0.25})

print(f'El precio final es de {precio_final}')


################### EJERCICIO 6 #####################

# Definir una función con nombre numero_max() que tome como argumento 
# dos números inroducidos por el usuario y devuelva el mayor de ellos, 


numero_uno = float(input('Escribe el primer número por favor'))
numero_dos = float(input('Escribe el segundo numero por favor'))

def numero_max(numero_uno,numero_dos)->float:
    if numero_uno > numero_dos:
        return numero_uno
    else:
        return numero_dos
    
resultado=numero_max(numero_uno,numero_dos)
print(f'El numero máximo introducido por usted es{resultado}')


################### EJERCICIO 7 #####################

# Definir una función max_tres(), que tome tres números 
# como argumentos y devuelva el mayor de ellos.


primer_numero=float(input('Escriba el primer número'))
segundo_numero=float(input('Escriba el segundo número'))
tercer_numero=float(input('Escriba el tercer número'))

def max_tres(num1,num2,num3)->float:
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
numero_maximo=max_tres(primer_numero,segundo_numero,tercer_numero)
print(f'El número con el valor máximo escrito por tí es {numero_maximo}')


################### EJERCICIO 8 #####################


# Escribir una funcion que tome un carácter y devuelva 
# True si es una vocal, de lo contrario devuelve Flase

caracter=(input('Escriba una letra '))


def vocal(caracter):
    lista_vocales=['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False

resultado_letra= vocal(caracter)
print(f'Tu letra escrita es una vocal? {resultado_letra}') 


################### EJERCICIO 9 #####################

# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los numeros de una lista. 
# Por ejemplo: sum ([1,2,3,4,5]) debería devolver 10 y multiplicar ({1,2,3,4}) deberia devolver 24

# Solicitar al usuario ingresar la lista=
entrada_usuario = input("Ingresa una lista de números separados por espacios: ")

# Convertir la entrada del usuario a una lista de números
lista_numeros = [float(numero) for numero in entrada_usuario.split()]


def sumar(lista):
    suma=0
    for numero in lista:
        suma+=numero
    return suma 



def multiplicar(lista):
    resultado=1
    for numero in lista:
        resultado*= numero
    return resultado    



resultado_suma = sumar(lista_numeros)
resultado_multiplicacion = multiplicar(lista_numeros)

print(f'La suma de la lista es: {resultado_suma}')
print(f'La multiplicación de la lista es: {resultado_multiplicacion}')


#Función para saber si un numero es impar o no





