def subcadena_con_rebandas(cadena: str, ) -> str:
    """ 
    La funcion se encarga de extraer el ultimo elemento de la cadena que seria el la subcadena .
    precondiciones : la cadena debe ser un str 
    postcondiciones : retorna la subcadena que seria el ultimo elemento de la cadena .

    """
    try :
        cadena = str(cadena)
        cadena = cadena.split()
        
        return cadena[-1]
        

    except TypeError: 
        raise TypeError("la cadena debe ser un str")
    
def subcadena_sin_rebandas(cadena: str) -> str:
    """ 

    La funcion debe dar la subcadena que seria la ultima palabra de la cadena. 
    precondiciones: el parametro recibido debe ser un string 
    postcondiciones: retorna la subcadena que seria la ultima palabra de la cadena.

    """
    try:
        cadena= str(cadena)
        cadena = cadena.split()
        ultimo_elemento = len(cadena) - 1
        for cad in cadena:
            if cad == cadena[ultimo_elemento]:
                return cad
        
    except TypeError:
        raise TypeError("la cadena debe ser un str")





frase = "El número de teléfono es 43567890" 
print(f"Con rebanadas :{subcadena_con_rebandas(frase)}\n")
print(f"Sin rebanadas :{subcadena_sin_rebandas(frase)}\n")
assert subcadena_con_rebandas(frase) == "43567890"
assert subcadena_sin_rebandas(frase) == "43567890"

    