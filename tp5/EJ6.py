from typing import List
def cargar_datos()->List[int]:
    """
    Carga una lista con números enteros ingresados por el usuario.
    La carga finaliza cuando el usuario ingresa -1.
    """
    numeros = []
    print("--- Carga de la lista ---")
    print("Ingrese números enteros. Escriba -1 para finalizar.")
    
    while True:
        try:
            entrada = input("Ingrese un número: ")
            numero = int(entrada)
            
            if numero == -1:
                break
            numeros.append(numero)
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")
            
    print("\nLista cargada exitosamente:", numeros)
    return numeros

def buscar_elementos(lista_numeros: List[int]) -> None:
    """
    Permite al usuario buscar elementos en la lista usando el método index().
    precondiciones: lista_numeros debe ser una lista de enteros.
    postcondiciones: ninguna 
    """
    if not lista_numeros:
        print("La lista está vacía, no se puede buscar.")
        return

    print("\n--- Búsqueda de elementos ---")
    while True:
        try:
            entrada = input("Ingrese un número a buscar (o 's' para terminar): ")
            if entrada.lower() == 's':
                break
            
            numero_a_buscar = int(entrada)
            indice = lista_numeros.index(numero_a_buscar)
            print(f"El número {numero_a_buscar} se encuentra en el índice {indice}.")
        except ValueError:
            print("Error: El número no se encuentra en la lista o la entrada no es válida.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

def main():
    """Función principal del programa."""
    lista = cargar_datos()
    buscar_elementos(lista)
    print("\nPrograma terminado.")

if __name__ == "__main__":
    main()
