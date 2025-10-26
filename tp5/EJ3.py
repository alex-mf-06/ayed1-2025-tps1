from typing import List

def informar_mes(mes:int)->str|List:
    """Dado un número de mes (1-12), devuelve el nombre del mes correspondiente.
    
    precondiciones: mes debe ser un entero entre 1 y 12.
    postcondiciones: devuelve una cadena con el nombre del mes correspondienteo o una lista vacia si el número es inválido.
    
    """
    try :
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        mes = mes -1
        if mes <0 or mes >11:
            return []
        else:
            return meses[mes]
    except TypeError:
        return []
    except IndexError:
        return []
    
if __name__ == "__main__":
    assert informar_mes(1) == "enero"
    assert informar_mes(5) == "mayo"
    assert informar_mes(12) == "diciembre"
    assert informar_mes(0) == []
    assert informar_mes(13) == []
    assert informar_mes(-3) == []
    assert informar_mes("tres") == []
    assert informar_mes([3.5]) == []