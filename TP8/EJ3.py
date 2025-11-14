from typing import List, Tuple
import re 

def dividir_correo(correo:str) -> Tuple[str,str,str,str]|None:
    """
    Recibe una dirección de email y devuelve sus partes separadas.

    PRECONDICIONES:
    - `correo` debe ser una cadena con formato usuario@dominio.extension.
      Ejemplo válido: "alguien@uade.edu.ar".

    POSTCONDICIONES:
    - Si el correo es válido, devuelve una tupla con:
        (usuario, dominio_completo, nombre_dominio, extension_principal)
      Ejemplo:
        "alguien@uade.edu.ar" -> ("alguien", "uade.edu.ar", "uade", "edu")

    - Si el correo tiene formato inválido, devuelve None.

    EFECTOS SECUNDARIOS:
    - Imprime un mensaje si ocurre un error inesperado.
    """
    try:
        patron_email = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.]+)$'
        es_valido = re.match(patron_email, correo)
        if not es_valido:
            return None


        user = es_valido.group(1)
        dominio = es_valido.group(2)
        partes_email = dominio.split('.')
        if len(partes_email) != 3:
            return None
        return (user,partes_email[0],partes_email[1],partes_email[2])
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None


if __name__ == "__main__":
    assert dividir_correo("alguien@uade.edu.ar") == ("alguien", "uade", "edu", "ar")
    assert dividir_correo("perritoinsano@.com") == None
    assert dividir_correo("perritomalvado@uade.edu.ar") == ("perritomalvado", "uade", "edu", "ar")



