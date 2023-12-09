import utilidades

def formatear_texto(texto: str, formato:str )-> str:
    if formato== 'minusculas':
        return utilidades.minusculas(texto)
    elif formato=='mayusculas':
        return utilidades.mayusculas(texto)
    return  f'El formato no existe'