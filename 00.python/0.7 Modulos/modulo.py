############################# FUNCIÓN CON PARÁMETROS CON VALORES POR DEFECTO #####################################


def sacar_dinero(saldo_cuenta:int, dinero_retirar=20):
    return saldo_cuenta-dinero_retirar

saldo=5000
saldo_restante= sacar_dinero(saldo)
print(f'El saldo restante es de: {saldo_restante}')

############################# FUNCIÓN CON PARÁMETROS OPCIONALES #####################################

# En los parametros opcionales no hace falta definir que tipo de datos tienen porque internamente python los va a meter en tuplas. Los toppings que
# le pasemos en la función van a ser metidos en una tupla internamente.

def crear_pizza(tipo_pizza, *toppings_extra)-> str:
    tipos_pizza=['margarita','cuatro quesos', 'barbacoa']
    frase_respuesta=''

    if tipo_pizza in tipos_pizza and not toppings_extra:
        frase_respuesta = f'Tu pizza{tipo_pizza} se está procesando, vuelva en 10 min, No tiene toppings....' 
    elif tipo_pizza in tipos_pizza and toppings_extra:
        frase_respuesta = f'Tu pizza  {tipo_pizza} con toppings {str(toppings_extra) } se está procesando '
    else: 
        frase_respuesta=  f'Tu tipo de pizza {tipo_pizza} no esta en nuestro menú'
    
    return frase_respuesta

respuesta1= crear_pizza('margarita')
print(respuesta1)


# Salchicha y pimiento rojo son parámetros opcionales.
respuesta2 = crear_pizza('cuatro quesos', 'salchicha', 'pimiento rojo')
print(respuesta2)