import random as rn 
from typing import List

def pedir_entero( ) -> int:
    """Pide al usuario que ingrese un numero entero mayor a 0.
    precondiciones: El usuario debe ingresar un numero entero mayor a 0.
    postcondiciones: Devuelve el numero ingresado por el usuario si es valido."""
    while True :
        try :
            n = int(input("Ingrese un numero entero mayor a 0 :"))
            if n <1 :
                print("debe ser un numero mayor a 0 ")
                continue 
            return n
        except ValueError:
            print("Error, debe ingresar un numero entero lee el contrato")


def crear_matriz(Lista:List) -> List[List[int]]:
    """Crea una matriz con la cantidad de listas que el usuario desee y devuelve una matriz vacia.
    precondiciones: La cantidad de listas debe ser un numero entero mayor a 0.
    postcondiciones: Devuelve una matriz vacia con la cantidad de listas que el usuario haya ingresado.
    """

    n = pedir_entero()
    matriz = [[]for i in range(n)]
    repetidos = set()
    for i , _ in enumerate(matriz):
        j = 0 
        while True :
            numero = rn.randint(0,n**2)
            if j == n :
                break
            elif not numero in repetidos :
                matriz[i].append(numero)
                repetidos.add(numero)
                j += 1
    return matriz 

matriz = []
matriz = crear_matriz(matriz)
print(matriz)