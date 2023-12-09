from mascota import Mascota

mascota1=Mascota('Nemo',10,0,2)

print(mascota1)
print(mascota1.get_nombre())
mascota1.ganar_torneo('Regional')
print(mascota1.get_nivel())

mascota1.alimentar_mascota('comida_buena')
