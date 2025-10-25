def contar_cuantas_veces_aparece(cadena:str,subcadena:str) -> None : 
    """
    Esta función permite al usuario ver una cadena de texto, especificar una subcadena
    y luego contar cuántas veces aparece dicha subcadena en la cadena original.
    
    Precondiciones:
    - El parámetro 'cadena' debe ser un string.
    - El parámetro 'subcadena' debe ser un string.
    
    Postcondiciones:
    - La función retorna un mensaje indicando cuántas veces aparece la subcadena
      en la cadena original.
    - Lanza TypeError si alguno de los parámetros no es un string.
    """
    try:
        cadena + ""
        subcadena + ""
    except TypeError:
        raise TypeError("ambos parámetros deben ser str")
    
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    cont_encontrada = 0
    contador = 0
    largo_subcadena = len(subcadena)
    for i,v in enumerate(cadena):
        if  v == subcadena[contador]:
            contador += 1
            if contador == largo_subcadena:
                cont_encontrada += 1
                contador = 0

    print(f"La subcadena '{subcadena}' aparece {cont_encontrada} veces en la cadena dada.")
    return None
if __name__ == "__main__":
    cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."

    subcadena = "UADE"
    contar_cuantas_veces_aparece(cadena,subcadena)


