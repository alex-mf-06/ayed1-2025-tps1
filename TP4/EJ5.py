def filtrar_palabras_por_ciclo(frase:str,longitud:int) -> str :
    """
    esta funcion se encarga de generar un string que sea mayor o igual a longitud es decir que si longitud es 5 y en la frase esta la palabra solo no debe estar al retornar 
    precondiciones : la longitud debe ser siempre un entero y ademas no debe ser menor a 0 y las frases debe ser una cadena de caracteres (string) 
    postcondiciones: la funcion debe retornar la frase que ingreso como parametro pero en la frase no deben estar palabras que sean menor a la lomgitud ingresada.

    """
    try : 
        frase = str(frase)
        longitud = int(longitud)
        if longitud < 0 :
            raise ValueError(" la longitud debe ser siempre un numero positivo ")
        
        lista_palabras = frase.split()
        frase_filtrada = ""
        for palabra in lista_palabras:
            if len(palabra) >= longitud:
                frase_filtrada += palabra + " "
        return frase_filtrada
    except ValueError  :
        raise ValueError("la longitud debe ser un numero entero no otra cosa lee el contrato ")
def filtrar_por_compresion(frase:str,longitud:int) -> str :
   
   
   """

    esta funcion se encarga de generar un string que sea mayor o igual a longitud es decir que si longitud es 5 y en la frase esta la palabra solo no debe estar al retornar 
    precondiciones : la longitud debe ser siempre un entero y ademas no debe ser menor a 0 y las frases debe ser una cadena de caracteres (string) 
    postcondiciones: la funcion debe retornar la frase que ingreso como parametro pero en la frase no deben estar palabras que sean menor a la lomgitud ingresada.

    
   """
   try : 
        frase = str(frase)
        longitud = int(longitud)
        if longitud < 0 :
            raise ValueError(" la longitud debe ser siempre un numero positivo ")
        
        frase_filtrada =[palabra for palabra in frase.split() if len(palabra) >= longitud]
        return " ".join(frase_filtrada)
   except ValueError  :
        raise ValueError("la longitud debe ser un numero entero no otra cosa lee el contrato ")    
   
def filtrar_por_filter(frase:str,longitud:int) -> str :
    """
    Se encarga de filtrar las palbras siempre y cuando la longitud de la misma sea mayor o igual a la longitud ingresada.
    precondiciones :
    la frase debe ser un string y la longitud debe ser un entero positivo.
    postcondiciones : 
    retorna la frase filtrada.

    """
    try : 
        frase = str(frase)
        longitud = int(longitud)
        if longitud < 0 :
            raise (" la longitud debe ser siempre un numero positivo")
        filtrado = list(filter(lambda x : len(x) >= longitud,frase.split()))
        return " ".join(filtrado)
    except ValueError:
        raise ValueError("la longitud debe ser un numero entero no otra cosa lee el contrato ")


frase = "La programación no solo consiste en escribir código que funcione, sino en crear soluciones claras, eficientes y fáciles de mantener, que otros puedan entender y mejorar con el tiempo"
longitud = 5

print(f"{filtrar_palabras_por_ciclo(frase,longitud)}\n")
print(f"{filtrar_por_compresion(frase,longitud)}\n")
print(f"{filtrar_por_filter(frase,longitud)}\n")

