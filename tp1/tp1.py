import random as rn 

rn.seed(0)
def registrar_positivos(cantidad):
    
    """Registra una cantidad de numeros positivos ingresados por el usuario.
    Args:
        cantidad (int): La cantidad de numeros positivos a registrar.
    Returns:
        list: Una lista con los numeros positivos ingresados.
    """
    lista = []
    for _ in range(cantidad): # Itera la cantidad de veces especificada
        while True: # Bucle infinito hasta que se ingrese un numero positivo
            try:
                num = int(input("Ingrese un numero positivo: ")) # Solicita al usuario un numero
                if num < 0: # Verifica si el numero es negativo
                    print("El numero debe ser positivo") # Muestra un mensaje de error si es negativo
                    continue # Vuelve al inicio del bucle para solicitar otro numero
                lista.append(num) # Agrega el numero positivo a la lista
                break # Sale del bucle si se ingresa un numero positivo
            except ValueError:
                print("Error, debe ingresar un numero entero") # Maneja el error si la entrada no es un entero
                continue # Vuelve al inicio del bucle para solicitar otro numero
    return lista # retorna la lista de numeros positivos

def buscar_mayor(lista) -> int:
    """Busca el mayor numero en una lista de numeros(int).
    Args:
        lista (list): La lista de numeros a evaluar debe ser una lista con enteros.
    Returns:
        int: El mayor numero encontrado o -1 si los mayores son duplicados.
    """
    #lista = [a, b, c] # Crea una lista con los numeros proporcionados
    mayor = max(lista)
    return mayor if lista.count(mayor) == 1 else -1
# tp1.py
m = registrar_positivos(10)
print(m)
print(buscar_mayor(m))

