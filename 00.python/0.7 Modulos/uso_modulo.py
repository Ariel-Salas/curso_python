############################# IMPORTAR MODULOS COMPLETOS #####################################

# 1.Importar todas las funciones de un módulo con *.

from modulo import *
crear_pizza('margarita','pepperoni')

# 2.Importar todo el módulo.

import modulo

modulo.crear_pizza('margarita','pepperoni')

# 3.Importar todo el módulo con un alias.

import modulo as m

m.crear_pizza('margarita', 'pepperoni')


############################# IMPORTAR PARTES CONCRETAS DE UN MODULO #####################################

# 1.Importar varias funciones de un módulo.

from modulo import crear_pizza

crear_pizza('margarita','pepperoni')

# 2.Importar funciones con alias.

from modulo  import crear_pizza as cp, sacar_dinero as sd 

cp('margarita', 'pepperoni')

sd()