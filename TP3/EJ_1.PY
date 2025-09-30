
import random as rn 
from typing import List
es_impar = lambda x : x % 2 != 0
# punto 1.a
def crear_matriz(Lista:List) -> List[List]:
    """Crea una matriz con la cantidad de listas que el usuario desee y devuelve una matriz vacia.
    precondiciones: La cantidad de listas debe ser un numero entero mayor a 0.
    postcondiciones: Devuelve una matriz vacia con la cantidad de listas que el usuario haya ingresado.
    """ 

    while True :
        n = int(input("Ingrese la cantidad de listas que va a tener la matriz :"))
        if n <1 :
            print("debe ser un numero mayor a 0 ")
        return [[]for i in range(n)] 
#punto 1.b
def carga_datos_(matriz:List[List]) -> List[List[int]]:
  """
  Carga la matriz con numeros aleatorios entre 1 y 99.
  precondiciones: La matriz debe ser una matriz vacia

  postcondiciones: Devuelve la matriz cargada con numeros aleatorios entre 1 y 99.
  la cantidad de filas y columnas depende de la cantidad de listas que el usuario haya ingresado.
  """
  return [[rn.randint(1,9)for col in matriz]for fila in matriz]
#punto 2 
def ordenar_ascendente(matriz:List[List[int]]) -> List[List[int]] :
  """
  ordena cada lista de la matriz en orden ascendente.
  precondiciones: La matriz debe estar cargada con numeros enteros.
  
  postcondiciones: Devuelve la matriz con cada lista ordenada en orden ascendente.
  """
  for i in matriz :
    i.sort()
  return matriz
#punto 3.a
def validar(matriz:List[List[int]]) -> int:
    """
    Valida que el numero ingresado por el usuario sea un numero entero mayor a 0 y menor o igual a la cantidad de listas de la matriz.
    precondiciones: La matriz debe ser una matriz cargada con numeros enteros.
    postcondiciones: Devuelve el numero ingresado por el usuario si es valido.
    """
    while True : 
        fila = int(input(f"ingrese que fila quiere mover sabiendo que la matriz tiene {len(matriz)} filas : "))
        if fila > len(matriz) or fila <1:
          print(f"Error_Numero invalido solo  hay {len(matriz)} filas")
          continue
        return fila
    
#punto 3.b    
def mover_filas(matriz:List[List[int]]) -> List[List[int]]:
    """
    Mueve una fila de la matriz a otra posicion.
    precondiciones: La matriz debe ser una matriz cargada con numeros enteros.
    postcondiciones: Devuelve la matriz con la fila movida a la nueva posicion."""
    n1=validar(matriz)
    while True:
        n2 = validar(matriz)    
        if n1 == n2 :
            print("no podes mover al mismo lugar una fila de la mtatriz")
            continue
    
        matriz[n1-1],matriz[n2-1] = matriz[n2-1],matriz[n1-1]
        return matriz

#punto 4
def mover_columnas(matriz:List[List[int]]) -> List[List[int]]:
    """
    Mueve una columna de la matriz a otra posicion.
    precondiciones: La matriz debe ser una matriz cargada con numeros enteros.
    postcondiciones: Devuelve la matriz con la columna movida a la nueva posicion.
    """
    n1=validar(matriz)
    while True:
        n2 = validar(matriz)    
        if n1 == n2 :
            print("no podes mover al mismo lugar una columna de la mtatriz")
            continue
        for fila in matriz : # recorre cada fila de la matriz
            fila[n1-1],fila[n2-1] = fila[n2-1],fila[n1-1] # intercambia los elementos de la columna n1 y n2
        return matriz
    
#punto 5
def transponer(matriz:List[List[int]]) -> List[List[int]]:
    """
    Transpone la matriz.
    precondiciones: La matriz debe ser una matriz cuadrada cargada con numeros enteros.
    postcondiciones: Devuelve la matriz transpuesta.
    """
    for i ,fila in enumerate(matriz) :
        for j ,_ in enumerate(fila) :
            if j > i:
                matriz[i][j],matriz[j][i] = matriz[j][i] , matriz[i][j]
        
    return matriz  

#punto 6 
def cal_promedio(matriz:List[List[int]]) -> None:
    """
    Calcula el promedio de una fila de la matriz.

    precondiciones: La matriz debe ser una matriz cargada con numeros enteros.

    postcondiciones: Muestra el promedio de la fila ingresada por el usuario.
    """
    filas =len(matriz)
    while True :
        fila = int(input(f"ingrese el numero de fila que desea saber el promedio sabien que la matriz tiene {filas} filas :  "))
        if fila > filas or fila < 1 :
            print("ERROR fila ingresada invalida " )
            continue
    
        total = sum(matriz[fila - 1])
        promedio = total / len(matriz)
        print(f"El promedio de los numeros de la fila {fila} es {round(promedio,2)} ")
        break
#punto 7
def cal_prom_impar_por_column(matriz:List[List[int]]) -> None:
    """
    Calcula el porcentaje de numeros impares en una columna de la matriz.
    precondiciones: La matriz debe ser una matriz cargada con numeros enteros.
    postcondiciones: Muestra el porcentaje de numeros impares en la columna ingresada por el usuario.
    
    """
    columna = int(input(f"ingrese la columna (la matriz tiene {len(matriz)} : ")) # la cantidad de columnas es igual a la cantidad de filas porque es una matriz cuadrada
    impares = sum(1 for fila in matriz if es_impar(fila[columna-1])) # cuenta la cantidad de numeros impares en la columna
    #for fila in matriz :
        #if es_impar(fila[columna]):
            #impares += 1
    porcentaje = (impares /len(matriz)) * 100 # calcula el porcentaje de numeros impares en la columna
    print(f"el porcentaje de la columna {columna} es : {round(porcentaje,2)}%")

#punto 8
def es_simet_diag_principal(matriz:List[List[int]]) -> bool:
    """
    Verifica si la matriz es simetrica respecto a la diagonal principal.

    precondiciones: La matriz debe ser una matriz cuadrada cargada con numeros enteros.

    postcondiciones: Devuelve True si la matriz es simetrica respecto a la diagonal principal y False en caso contrario.
    """
    copia = [fila[:] for fila in matriz] # crea una copia de la matriz
    transpuesta = transponer(fila[:] for fila in matriz) # transpone la matriz
    return copia == transpuesta # compara la copia con la transpuesta
#punto 9
def es_simet_diag_secun(matriz:List[List[int]]) -> bool:
    """
    Verifica si la matriz es simetrica respecto a la diagonal secundaria.
    precondiciones: La matriz debe ser una matriz cuadrada cargada con numeros enteros.
    postcondiciones: Devuelve True si la matriz es simetrica respecto a la diagonal secundaria y False en caso contrario."""
    n = len(matriz) # la canitdad de listas que tiene la matriz 
    for i , fila in enumerate(matriz): # va a recorrer la canitdad de list de la matriz y ademas da el valor de una list
        for j , _ in enumerate(fila): # recorre la cant de elementos de la lista NxN 
            if i + j < n -1 : # pregunta si el suma de i + j que en la primer vuelta son 0 es menor que n -1 
                if matriz[i][j] != matriz[n-1-j][n-1-i]: # pregunta si el primer elemen de la 1er lista es distinto a el ultimo elem de la ultima lista ejemplo : [[4,3,2],[6,8,3],[2,3,4]]
                    return False # va a retornar false si se cumple la preguta de arriba 
    return True # despues de recorrer todo el for retorna true queriendo decir que 
#punto 10.a
def es_capicua(lista:list[int]) -> list[int]:


    """
    Verifica si la lista es capicúa (se lee igual de izquierda a derecha que de derecha a izquierda).

    """
    n = len(lista)
    copia = []
    for i in range(n//2):
        if lista[i] == lista[n-i-1]:
            copia.append(lista[i])
    return copia
#punto 10.b
def col_capic(matriz:List[List[int]]) -> List[int]:
    """
    Devuelve una lista con las columnas que son capicuas.
    precondiciones: La matriz debe ser una matriz cargada con numeros enteros.
    postcondiciones: Devuelve una lista con las columnas que son capicuas.
    """
    columnas_lista = [
    [fila[col] for _, fila in enumerate(matriz)]  
    for col, _ in enumerate(matriz)          
    ]
    return [columna for columna in columnas_lista if es_capicua(columna)]
def mostrar_matriz(matriz: List[List[int]]) -> None:
    """Muestra la matriz en pantalla."""
    for fila in matriz:
        print(fila)
    print()  # línea en blanco para mejor visualización    
def menu_compacto():
    matriz = []
    while True:
        print("\n=== MENÚ MATRICES ===")
        print("1.Crear  2.Cargar  3.Ordenar  4.Mover filas  5.Mover columnas")
        print("6.Transponer  7.Promedio fila  8.% impares columna")
        print("9.Simetría diag. principal 10.Simetría diag. secundaria")
        print("11.Columnas capicúas 12.Mostrar 0.Salir")
        opcion = input("Opción: ")

        if opcion == "0":
            break
        elif opcion == "1":
            matriz = crear_matriz([])
        elif opcion == "2" and matriz:
            matriz = carga_datos_(matriz)
        elif opcion == "3" and matriz:
            matriz = ordenar_ascendente(matriz)
        elif opcion == "4" and matriz:
            matriz = mover_filas(matriz)
        elif opcion == "5" and matriz:
            matriz = mover_columnas(matriz)
        elif opcion == "6" and matriz:
            matriz = transponer(matriz)
        elif opcion == "7" and matriz:
            cal_promedio(matriz)
        elif opcion == "8" and matriz:
            cal_prom_impar_por_column(matriz)
        elif opcion == "9" and matriz:
            print("Sí" if es_simet_diag_principal(matriz) else "No")
        elif opcion == "10" and matriz:
            print("Sí" if es_simet_diag_secun(matriz) else "No")
        elif opcion == "11" and matriz:
            print(col_capic(matriz))
        elif opcion == "12" and matriz:
            mostrar_matriz(matriz)
        else:
            print("Opción inválida o matriz no creada/cargada aún.")


menu_compacto()
