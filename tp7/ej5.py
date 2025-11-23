
def divide_devuelve_resto(a:int , b:int)->int:
    """
    
    Esta funcion se encarga de dividir dos numeros que el usuario ingrese el ususario debe ingresar dos numeros enteros y el segundo numero no puede ser 0
    precondiciones : ambos numeros deben ser enteros y el segundo numero no puede ser 0
    postcondiciones : devuelve un numero entero que es el resultado del resto de la division . devuelve -1 si el segundo numero es 0 o si alguno de los dos numeros no es entero

    """
    try : 
        a = abs(int(a))
        b = abs(int(b))
        if b == 0 :
            return -1
        elif a < b :
            return a
        elif a == b :
            return 0
        if b == 1:
            return 0
        else :
            return divide_devuelve_resto(a - b , b)
        
        
    except TypeError:
        return -1
    except ValueError:
        return -1
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return -1
    
if __name__ == "__main__":
    print(divide_devuelve_resto(33,7))





