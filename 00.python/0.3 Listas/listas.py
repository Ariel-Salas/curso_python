

motocicleta_lista= ["honda","ducati1","indian"]

motocicleta_lista.append(True)

#print(motocicleta_lista)



#ordenar listas#

vocales_desordenadas=['u','a','i','o']
vocales_desordenadas.sort(reverse=True)
print(vocales_desordenadas)


#acceder a las listas

números=[2,3,1,5,4]

primer_elemento=números[4]
primeros_elementos=números[0:5]
print(primer_elemento)
print(primeros_elementos)

último_elemento_lista=números[-1]
print(último_elemento_lista)

últimos_elementos_lista=números[-2:]
print(últimos_elementos_lista)


#Posiciones impares de la lista
#primero conseguir todos los elementos#

todos_elementos=números[::1]
print(todos_elementos)


comidas=['pizza','hamburguesa','papas fritas']
comidas_copia=comidas.copy()



comidas.append('ensalada')


print(comidas)
print(comidas_copia)



longuitud_comidas=len(comidas)
print(longuitud_comidas)

comidas_cuenta=comidas.count('pizza')
print(comidas_cuenta)



#concatenar 2 listas#

comidas_no_sanas=['pizza','hamburguesas','papas fritas']
comidas_sanas=['ensaladas','manzana']

comidas=comidas_sanas+comidas_no_sanas
print(comidas)

#otra forma#

comidas_no_sanas.extend(comidas_sanas)
print(comidas_no_sanas)