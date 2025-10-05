from typing import List
import random as rn
from EJ3 import pedir_entero
guion = lambda x: "-" * x

def crear_matriz_() -> List[List]:
    """Crea una matriz con la cantidad de listas que el usuario desee y devuelve una matriz vacia.
    precondiciones: La cantidad de listas debe ser un numero entero mayor a 0.
    postcondiciones: Devuelve una matriz vacia con la cantidad de listas que el usuario haya ingresado.
    """    

    n = pedir_entero()
    return [[]for i in range(n)]
    
def cargar_bicicletas(matriz:List[List[int]]) -> List[List[int]]:
    """
    Carga la matriz con la cantidad de bicicletas que se fabricaron en cada dia de la semana.
    precondiciones: La matriz debe ser una matriz vacia con la cantidad de listas que el usuario haya ingresado.
    postcondiciones: Devuelve la matriz con la cantidad de bicicletas que se fabricaron en cada dia de la semana.
    """
    try: 
        dias = 6 
        matriz = [[rn.randint(0,150) for i in range(dias)] for fila in matriz] 
        return matriz
    except TypeError:
        raise TypeError("Error: La entrada no es una lista válida.")
def validar_matriz(fabricas) -> bool:
    """
    Valida que la matriz tenga al menos una fila y que todas las filas tengan la misma cantidad de columnas.
    precondiciones: La entrada debe ser una lista de listas con numeros.
    postcondiciones: Devuelve True si la matriz es valida, False en caso contrario.
    """
    try:
        # Comprobar que la matriz no esté vacía
        if not fabricas:
            raise ValueError("Error: la matriz no debe estar vacía.")
        
        # Verificar estructura y contenido
        columnas = len(fabricas[0])
        for fabrica in fabricas:
            if len(fabrica) != columnas:
                raise ValueError("Error: todas las filas deben tener la misma cantidad de columnas.")
            for bici in fabrica:
                _ = float(bici)  # Verificar que cada elemento sea numérico
        return True  # Si todo está bien
    except TypeError:
        raise TypeError("Error: la entrada debe ser una lista de listas con números.")
    except ValueError as e:
        raise ValueError(e)
    
def mostrar_fabricas(fabricas) -> None:
    """
    Muestra la cantidad de bicicletas fabricadas por cada fabrica en cada dia de la semana.
    precondiciones: La entrada debe ser una lista de listas con numeros.
    postcondiciones: No devuelve nada, solo muestra la matriz en un formato legible.
    """
    validar_matriz(fabricas)
    
    
    semana = ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB"]
    # Imprimir encabezado
    print(f"{'FAB':<5}", end="") # etiqueta de la columna
    for dia in semana: # encabezados de los dias
        print(f"{dia:>5}", end="") # ancho fijo para alinear
    print() # salto de linea

    # Imprimir datos de cada fábrica
    for i, fabrica in enumerate(fabricas,start=1): # indice de la fabrica
        print(f"F{i:<4}", end="")   # etiqueta de la fila
        for bici in fabrica: # datos de la fabrica
            print(f"{bici:>5}", end="")  # ancho fijo para alinear
        print()   
def mostrar_informe_fabri(fabricas) -> None :
    """
    muestra el total de bicicletas fabricadas por cada fabrica en la semana.
    precondiciones: La entrada debe ser una lista de listas con numeros.
    postcondiciones: No devuelve nada, solo muestra el total de bicicletas fabricadas por cada fabrica en la semana.
    """
    validar_matriz(fabricas)
    print("Informe de fabricas : ")
    for i , fabrica in enumerate(fabricas, start=1):
        print(f"F{i} total de la semana : {sum(fabrica)} bicicletas")
        print(guion(50))
def detaL_infordia_fabri_prod(fabricas) -> None:
    """
    Muestra el dia y la fabrica que mas bicicletas fabrico en la semana.
    precondiciones: La entrada debe ser una lista de listas con numeros.
    postcondiciones: Devuelve una tupla con la fabrica, el dia y la cantidad de bicicletas que mas fabrico en la semana.
    """
    validar_matriz(fabricas)
    semana = ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB"]
    max_val = -1
    max_fab = -1
    max_dia = -1
    for i , fabrica in enumerate(fabricas):
        for dia , mayor in enumerate(fabrica):
            if mayor > max_val :
                max_val = mayor
                max_fab = i
                max_dia = dia 
    print(f"la fabrica que mas produjo fue la F{max_fab +1} el dia {semana[max_dia ]} con {max_val} bicicletas . ")
def dia_mas_productivo(fabricas) -> None:
    """
    Muestra el dia que mas bicicletas se fabricaron en total en todas las fabricas.
    precondiciones: La entrada debe ser una lista de listas con numeros.    
    postcondiciones: No devuelve nada, solo muestra el dia que mas bicicletas se fabricaron en total en todas las fabricas.
    """

    validar_matriz(fabricas)
    semana = ["LUN", "MAR", "MIE", "JUE", "VIE", "SAB"]
    
    sem_prod = [sum(fabrica[i] for fabrica in fabricas)for i , _  in enumerate(fabricas[0]) ]   # Suma las bicicletas de todas las fabricas por dia
    Dia_may = sem_prod.index(max(sem_prod))
    for i , sem in enumerate(sem_prod):
        print(f"El dia {semana[i]} se fabricaron {sem} bicicletas . ")
        print(guion(50))

    print(f"El dia que mas produccion hubo contando todas las fabricas es el {semana[Dia_may]} con {max(sem_prod)} bicicletas .  ")

def min_prod(fabricas) -> List[int]:
    """
    Devuelve una lista con la cantidad minima de bicicletas fabricadas por cada fabrica en la semana.
    precondiciones: La entrada debe ser una lista de listas con numeros.
    postcondiciones: Devuelve una lista con la cantidad minima de bicicletas fabricadas por cada fabrica en la semana.
    """
    validar_matriz(fabricas)
    return [min(fila) for fila in fabricas] 


def menu() -> None:
    """Muestra el menu de opciones."""

    opciones =["- Crear matriz de fabricas",
               "- Cargar bicicletas fabricadas", 
               "- Mostrar fabricas",
               "- Mostrar informe de fabricas",
               "- Mostrar detalle del dia y fabrica que mas produjo",
               "- Mostrar dia mas productivo",
               "- Mostrar cantidad minima de bicicletas fabricadas por cada fabrica en la semana",
               "- Salir"]
    print("Menu de opciones : ")
    for i ,opcion in enumerate(opciones,start=1):
        print(guion(50))
        print(f"{i} {opcion}")
    print(guion(50))
def main () -> None:
    """Funcion principal del programa."""
    matriz = []
    while True : 
        menu()
        opcion = pedir_entero()
        if opcion == 1 :
            matriz = crear_matriz_()
            print("Matriz creada con exito .")
        elif opcion == 2 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear la matriz primero .")
                continue
            matriz = cargar_bicicletas(matriz)
            print("Matriz cargada con exito .")
        elif opcion == 3  :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            mostrar_fabricas(matriz)
        elif opcion == 4 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            mostrar_informe_fabri(matriz)
        elif opcion == 5 :
            if not matriz  or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            detaL_infordia_fabri_prod(matriz)
        elif opcion == 6 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            dia_mas_productivo(matriz)
        elif opcion == 7 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            semana_min_produccion = min_prod(matriz)
            for i , min_prod_fabri in enumerate(semana_min_produccion,start=1):
                print(f"La cantidad minima de bicicletas fabricadas por la fabrica F{i} en la semana es : {min_prod_fabri}")   
            
        elif opcion == 8 :
            print("Saliendo del programa ...")
            break
        else :
            print("Opcion invalida , intente nuevamente .")
            continue
if __name__ == "__main__":
    main()
