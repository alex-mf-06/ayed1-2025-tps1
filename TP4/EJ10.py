import re 
def cambiar_palabra_de_cadena(cadena:str) -> str :
    """
    Esta función permite al usuario ver una cadena de texto, especificar una palabra
    que desea cambiar y luego proporcionar la nueva palabra para el reemplazo.
    
    Precondiciones:
    - El parámetro 'cadena' debe ser un string.
    
    Postcondiciones:
    - La función retorna la cadena original con todas las ocurrencias de la
      palabra especificada por el usuario reemplazadas por la nueva palabra.
    - Lanza TypeError si el parámetro 'cadena' no es un string.
    """
    try:
       
        # Si 'cadena' no es un string, esto lanzará un TypeError.
        cadena + ""
    except TypeError:
        raise TypeError("la cadena debe ser un str")

    print(f"{cadena}\n")

    palabra_a_cambiar = input("Ingrese la palabra que desea cambiar: ")
    nueva_palabra = input(f"Ingrese la nueva palabra para reemplazar '{palabra_a_cambiar}': ")

    
    # si el usuario escribe "programacion", el patrón buscará "progr[aá]m[aá]ci[oó]n".
    patron_intermedio = (re.escape(palabra_a_cambiar)
                         .replace('a', '[aá]').replace('e', '[eé]')
                         .replace('i', '[ií]').replace('o', '[oó]')
                         .replace('u', '[uú]'))

    # \b asegura que se reemplace la palabra completa y no subcadenas.
    # re.IGNORECASE hace que la búsqueda no distinga entre mayúsculas y minúsculas.
    patron = r'\b' + patron_intermedio + r'\b'
    cadena_modificada = re.sub(patron, nueva_palabra, cadena, flags=re.IGNORECASE)
    
    return cadena_modificada

if __name__ == "__main__":
    frase_ejemplo = "La programación no solo consiste en escribir código que funcione, sino en crear soluciones claras, eficientes y fáciles de mantener, que otros puedan entender y mejorar con el tiempo"
    
    resultado = cambiar_palabra_de_cadena(frase_ejemplo)
    print(f"\nCadena modificada: {resultado}")

    
