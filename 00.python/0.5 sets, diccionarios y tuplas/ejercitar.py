amigos_invitados={'Juan', 'Pedro', 'Ana', 'Marta', 'Carlos'}
amigos_confirmados={'Juan', 'Pedro', 'Ana'}

amigos_confirmados.add('Luis')

amigos_sin_confirmar = amigos_invitados.difference(amigos_confirmados)
print(amigos_sin_confirmar)