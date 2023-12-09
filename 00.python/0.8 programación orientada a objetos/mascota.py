# Sintaxis:

# class NombreClase():
#   Atributos
#   def __init__(self):
#       Inicializar atributos (constructor)
#   Setters and getters
#   Metodos de clase
#

# Implementación de la clase mascota para un videojuego de animales.
# TODO: - Añade el atributo salud_maxima y cambiar el método alimentar_mascota para comprobar cuando tu mascota ya tenga la salud máxima
#       no añada más puntos de salud. Además, si una comida que se le va a dar supera la salud máxima también se tiene que controlar.

class Mascota():

    ############################# ATRIBUTOS DE LA CLASE #####################################

    __nombre: str
    _puntos_salud: int
    __nivel: int
    __edad: int

    ############################# CONSTRUCTOR DE LA CLASE #####################################

    def __init__(self, nombre, puntos_salud, nivel, edad):
        self.__nombre = nombre
        self._puntos_salud = puntos_salud
        self.__nivel = nivel
        self.__edad = edad

    ##################d########### METODOS GETTERS AND SETTERS #####################################

    # Los metodos getters y setters sirven para ofrecer la funcionalidad de obtener el valor o cambiar el valor de los atributos que queremos darle 
    # la posibilidad al programador que utilice la clase.

    # Sintaxis getters: (Los atributos deben ser privados o protegidos, sino no tendría sentido hacer un get o set ya que podemos modificar y
    # consultar los atributos directamente, es más daría un bucle infinito.)
    
    # def get_atributo(self) -> tipo_atributo:
    #   return self.__nombre_atributo

    # Sintaxis setters:
    # def set_atributo(self, value) -> None:
    #   self.__nombre_atributo = value

    
    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, value):
        self.__nombre = value

    def get_puntos_salud(self) -> int:
        return self._puntos_salud

    def set_puntos_salud(self, puntos_salud):
        self._puntos_salud = puntos_salud

    def get_nivel(self) -> int:
        return self.__nivel

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def get_edad(self) -> int:
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

  ############################# METODOS DE CLASE #####################################

  # Método que sirve para aumentar la salud a tu mascota.

    def alimentar_mascota(self, comida: str) -> None:
        if comida == 'comida_normal':
            self._puntos_salud += 10
        elif comida == 'comida_buena':
            self._puntos_salud += 20
        elif comida == 'comida_genial':
            self._puntos_salud += 30

        print(
            f'Mmm... que rico! Ahora me siento más fuerte y tengo {self._puntos_salud} puntos de salud.')

    # Método que sirve para aumentar de nivel a tu mascota en función del torneo que haya ganado.
    def ganar_torneo(self, tipo_torneo: str) -> None:
        if tipo_torneo == 'Regional':
            self.__nivel += 1
        elif tipo_torneo == 'Nacional':
            self.__nivel += 2
        elif tipo_torneo == 'Internacional':
            self.__nivel += 3



mascota_1 = Mascota('Nemo',10,0,2)
mascota_1.ganar_torneo('Regional')