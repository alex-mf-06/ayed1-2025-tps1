from typing import List, Tuple




def de_fecha_a_cadena(fecha: Tuple[int, int, int]) ->str|None:
    """
    
    Esta funcion se encarga de que el usuario que anteriormente haya puesto una tupla con tres elemento que representan el dia el mes y el año 
    se convierta en un string.
    precondiciones :
    la persona de parametro debe darle una tupla de enteros que representen el año , el mes , y el dia 
    postcondicioes:devuelve un string que representa la fecha.
    
    """
    try:
        dia, mes, anio = fecha
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
        corte = 30
        meses_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes < 1 or mes > 12:
            print("El mes debe estar entre 1 y 12.")
            return None

        if dia < 1 or dia > meses_dias[mes - 1]:
            print(f"El día debe estar entre 1 y {meses_dias[mes - 1]}.")
            return None

        if anio >0 and anio <= 99:
            if anio <= corte:
                anio += 2000
            else:
                anio += 1900
        
        return f"{dia} de {meses[mes]} de {anio}"


    except TypeError:
        print("Ocurrio un error al convertir")
    except ValueError:
        print("Ocurrio un error al convertir los valores de la tupla a enteros fijese si son numeros enteros")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    
if __name__ == "__main__":
    fecha_cadena = de_fecha_a_cadena((12,12,12))
    print(fecha_cadena)
    assert fecha_cadena == "12 de diciembre de 2012"
    assert de_fecha_a_cadena((35,2,21)) == None
    assert de_fecha_a_cadena((12,15,21)) == None

    




