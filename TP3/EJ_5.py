from typing import List
import EJ_4 as ej4
from EJ3 import pedir_entero
import random as rn
guion = lambda x: "-" * x

def menu() ->None:
    """Muestra el menu de opciones."""

    opciones =["- Crear filas para el cine y la cantidad de butacas",
               "- Mostrar las butacas ",
               "- Reservar butacas",
               "- Cargar butacas automatico",
               "- Mostrar butacas disponibles",
               "- Mostrar la mayor cantidad de butacas disponibles en cada fila",
               "- Salir"]
    print("Menu de opciones : ")
    for i ,opcion in enumerate(opciones,start=1):
        print(guion(50))
        print(f"{i} {opcion}")
    print(guion(50))

def cargar_butacas_por_fila(matriz : List[List]) -> List[List[int]]:
    """ 
    carga la matriz con las butacas por fila que ingrese el usuario
    precondicion : debe ser una  matriz con filas creadas pero que no tenga butacas cargadas
    postcondicion : devuelve la matriz con las butacas cargadas

    """
    n = pedir_entero()
    return [[1 for i in range(1,n+1)] for _ in matriz]

def mostrar_fil_buta_cine(matriz:List[List[int]]) -> None:
    """Muestra las butacas y filas del cine.
    precondiciones: La matriz debe estar creada y cargada con las butacas.
    postcondiciones: Muestra las butacas disponibles en el cine."""
    
    
    
    print(f"Asientos:", end=" ")
    for i , butaca in enumerate(matriz[0],start=1):
        print(f"{i:>3} ", end="")
    print("\n")
    for i , fila in enumerate(matriz,start=1):
        print(f"Fila {i}  : ", end="")
        for butaca in fila:
            print(f"{butaca:>3} ", end="")
        print("\n")
        
    print(guion(50))

def reservar(matriz:List[List[int]]) -> List[List[int]]:
    """Permite reservar butacas en el cine.
    precondiciones: La matriz debe estar creada y cargada con las butacas.
    postcondiciones: Devuelve la matriz actualizada con las butacas reservadas."""
    
    print(f"Elige la fila que desea  : (solo hay en el cine ){len(matriz)} filas ")
    while True :
        fila = pedir_entero()
        if fila > len(matriz):
            print("Error : fila invalida .")
            continue
        break

    print("Elige la butaca que desea reservar : ")
    print(f"(solo hay en la fila {fila} {len(matriz[0])} butacas )")
    while True : 
        butaca = pedir_entero()
        if butaca > len(matriz[0]):
            print("Error : butaca invalida .")
            continue
        break
    if matriz[fila-1][butaca-1] == 0 :
        print("Error : butaca ya reservada .")
        return False
    matriz[fila-1][butaca-1] = 0
    return True
def validar_matriz_vacia(matriz:List[List[int]]) -> bool:
    """Valida si la matriz esta vacia.
    precondiciones: La matriz debe estar creada.
    postcondiciones: Devuelve True si la matriz esta vacia, False en caso contrario."""
    try:
        for fila in matriz:
            for butaca in fila:
                if butaca == 1:
                    return False
        return True
    except TypeError:
        raise TypeError(" Error: la matriz no es válida o no es iterable.")
       
    

def cargar_sala(matriz:List[List[int]]) -> List[List[int]]:
    """Carga las butacas automaticamente en la matriz.
    precondiciones: La matriz debe estar creada tanto filas como columnas.
    postcondiciones: Devuelve la matriz con las butacas cargadas automaticamente. (0 = reservada , 1 = disponible)"""
    validar_matriz_vacia(matriz)
    while True :
     
     try:
        butacas = int(input("Ingrese la cantidad de butacas a reservar automaticamente : "))
     except ValueError:
        print("Error : debe ingresar un numero entero .")
        continue
     if butacas < 1 or butacas > len(matriz[0]): 
        print(f"Error : debe ingresar un numero entre 1 y {len(matriz[0])} .")
        continue
     break
    disponibles = [[rn.choice([0,1]) for _ in range(butacas)] for _ in matriz]
    return disponibles
def butacas_contiguas(matriz:List[List[int]]) -> tuple[int,int,int]:
    """retorna una tupla con la mayor cantidad de butacas contiguas disponibles.
    
    precondiciones: La matriz debe estar creada y cargada con las butacas.
    postcondiciones: Devuelve una tupla con la fila, columna y cantidad de butacas contiguas disponibles."""
    if ej4.validar_matriz(matriz):
       max_len = 0 # mayor cantidad de butacas contiguas
       fila_inicio = -1 # fila donde comienza la mayor cantidad de butacas contiguas
       col_inicio = -1 # columna donde comienza la mayor cantidad de butacas contiguas

       for i, fila in enumerate(matriz):
            
            cont = 0
            inicio = 0

            for j, butaca in enumerate(fila):
                if butaca == 1:
                    if cont == 0:
                        inicio = j
                    cont += 1
                    if cont > max_len:
                        max_len = cont
                        fila_inicio = i
                        col_inicio = inicio
                else:
                    cont = 0

       return fila_inicio + 1,col_inicio  + 1, max_len # devolver fila y columna en base 1
    
    else:
        raise ValueError("Error: la matriz no es válida.")
def butacas_libres(matriz:List[List[int]])  -> int:
    """Muestra la cantidad de butacas disponibles en el cine.
    precondiciones: La matriz debe estar creada y cargada con las butacas.
    postcondiciones: Devuelve un numero entero segun la cantidad de butacas disponibles en el cine."""
    if ej4.validar_matriz(matriz):
        return sum(fila.count(1) for fila in matriz)
    else:
        raise ValueError("Error: la matriz no es válida.")
def main( ) -> None:
     """Funcion principal del programa."""

     matriz = []
     while True : 

        menu()
        opcion = pedir_entero()
        if opcion == 1 :
            matriz = ej4.crear_matriz_()
            print("Matriz creada con exito .")
            matriz = cargar_butacas_por_fila(matriz)
            print("carga creada con exito .")

        elif opcion == 2 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear la matriz primero .")
                continue
            mostrar_fil_buta_cine(matriz)

        elif opcion == 3 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            disponible = reservar(matriz)
            print(disponible)
            if disponible :
                print("Butacas reservadas con exito .")
            else : 
                print("No se pudo reservar la butaca .")
            

        elif opcion == 4 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear la matriz primero .")
                continue
            matriz = cargar_sala(matriz)
            print("Butacas cargadas con exito .")

        elif opcion == 5 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            b_disponible=butacas_libres(matriz)
            print(f" Hay en total de butacas disponibles {b_disponible} en el cine .")

        elif opcion == 6 :
            if not matriz or len(matriz[0]) == 0 :
                print("Error : debe crear y cargar la matriz primero .")
                continue
            mayor =butacas_contiguas(matriz)
            print(f"La fila con mayor cantidad de butacas disponibles es la fila {mayor[0]} con {mayor[2]} butacas disponibles .")

        elif opcion == 7 :
            print("Saliendo del programa ...")
            break
if __name__ == "__main__":
    main()