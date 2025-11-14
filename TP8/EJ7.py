
from typing import Set 

def eliminar_conjunto() -> None:
    """
    
    Esta funcion se encarga de eliminar los valores que estan en el conjunto 
    precondiciones : no tiene 
    postcondiciones: se muestra cuando se elimina un elemento del conjunto.
    
    
    """
    set_conjuntos = set(range(10))
    while True:
        print(set_conjuntos)
        try:
            valor_str = input("Ingrese un numero que este entre los numeros del 0 al 9 : ").strip()

            if valor_str == "-1":
                break

            elif valor_str.isdigit():
                
                valor = int(valor_str)
                if valor >= 0 and valor <= 9:

                    if valor in set_conjuntos:
                        set_conjuntos.remove(valor)
                    
                
                
                else : 
                    print("El numero debe estar entre los elementos del conjunto")
            else:
                print("El numero debe ser un numero entero")
        
        except KeyboardInterrupt:
            print("Solo vas a salir si ingresas un numero valido")
            continue    

        except ValueError:
            print("Hubo un error al convertir el numero")

if __name__ == "__main__":
    eliminar_conjunto()







