valor_booleano=True




#if valor_boleano:
#    print('el valor es verdadero')
    


if valor_booleano:
    print('valor es verdadero')
else:
    print('velor es falso')

edad=9;

if edad >=18 and edad<=81:
    print('puedes manejar')
else:
    print('no puedes') 


dinero=1000;

if dinero >=1000:
    print('eres rico!')
elif dinero >=500:
    print('eres de clase media')
elif dinero >=200:
    print('tamos mal')
else:
    print('eres pobre')
    


nombre="r2d2";

if nombre=="r2d2":
    print('es el nombre exactamente igual')
else:
    print('no es el nombre')



lista=['arturo','pepe','maria']
nombre2='pepe'
if nombre2 in lista:
    print('puedes acceder a la web ' + nombre2)
else:
    print('no puedes acceder ' + nombre2 )





if lista:
    print(lista[0])
else:
    print('Esta lista esta vacia ')



#condicionales inline:



liquidacion=2500

estatus_economico= 'clase muy alta' if liquidacion>=2000 else 'clase media' if liquidacion >500 else 'clase baja'






print(estatus_economico)