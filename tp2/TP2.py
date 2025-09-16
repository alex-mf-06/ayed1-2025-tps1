import random
random.seed(42)  # Fijar la semilla para reproducibilidad
#ejercicio 1
def cargar_lista_aleatoria():
    """
    Carga una lista de números enteros aleatorios.

    """
    cantidad = random.randint(10, 99)  # Número aleatorio de dos dígitos
    lista = [random.randint(1000, 9999) for _ in range(cantidad)]
    return lista
def copiar_lista(lista):
    """
    Crea una copia de la lista proporcionada.

    """
    copia = []
    for i in lista:
        copia.append(i)
    return copia
def producto_lista(lista:list[int]) -> list[int]:
    """
    Calcula el producto de todos los elementos en la lista.

    """
    producto = 1
    for i in lista:
        producto *= i
    return producto
def eliminar_elemento(lista:list[int], elemento:int) -> list[int]:
    """
    Elimina todos los valores de un elemento que pone el usuario en la lista.

    """
    return [i for i in lista if i != elemento] # esto elimina el elemento que el usuario quiere quitar
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
guion = lambda x: "-" * x
lista = cargar_lista_aleatoria()
copia = copiar_lista(lista)
producto = producto_lista(copia)
lista_cambiada = eliminar_elemento(copia, 2824)
capicua = es_capicua(copia)
print(F"Lista original: {lista}")
print(F"Lista copiada: {copia}")
print(F"Producto de la lista copiada: {producto}")
print(F"Lista cambiada: {lista_cambiada}")
if len(capicua) > 0:
    print(F"Elementos comunes: {capicua}")
else:
    print("No hay elementos comunes.")

#ejercicio 2

def cargar_lista(cantidad:int)-> list[list[int]]:
    """
    Carga una lista de listas con números enteros aleatorios.

    """
    if cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    lista = [random.randint(1,100) for _ in range(cantidad)]
    return lista

def hay_repetidos(lista:list[int]) -> bool:
    """
    Verifica si hay elementos repetidos en la lista va a devolver True si hay repetidos y False si no.
    """
    for i in range(len(lista)):
        elem= lista[i]
        for elemento in lista[i+1:]:
            if elem == elemento:
                return True
    return False
def eliminar_repetidos(lista:list[int]) -> list[int]:
    """
    Elimina los elementos repetidos de la lista y devuelve una nueva lista sin duplicados.
    """
    lista_sin_repetidos = []
    for i in lista:
        if i not in lista_sin_repetidos:
            lista_sin_repetidos.append(i)
    return lista_sin_repetidos
def main():
    lista = int(input("Ingrese la cantidad de números a generar: "))
    print(guion(70))
    lista = cargar_lista(lista)
    print(F"Lista generada: {lista}")
    print(guion(70))
    print(F"¿Hay elementos repetidos? {hay_repetidos(lista)}")
    unicos = eliminar_repetidos(lista)
    print(guion(70))
    print(F"Lista sin repetidos: {unicos}")

if __name__ == "__main__":
    main()
#ejercicio 3 
def carg_lista():
    """
    cargar una lista con la cantidad  que se le solicita al usuario  
    """
    
    cantidad = int(input("Ingrese la cantidad de números a generar: "))
    lista = [i**2 for i in range(1,cantidad+1)]
    print(F"{lista}")
    print(f"Los ultimos 10 elementos son : {lista[-10:]}")
carg_lista()
#ejercicio 4
def eliminar_valor_lista(lista: list[int], lista_eliminar: list[int]) -> list[int]:
    for i in lista_eliminar: # Itera sobre los elementos a eliminar
        while i in lista:    # Se repite hasta eliminar todas las ocurrencias
            lista.remove(i)
    return lista # Lista final sin los valores eliminados
lista_a = [1,1,2,3,4,4,5,6,78,21]
lista_con_valores_a_eliminar = [1, 4, 9, 20, 21]
print(f"lista original : {lista_a}")
print(guion(70))
print(f"lista con valores a eliminar : {lista_con_valores_a_eliminar}")
print(guion(70))
print(f"lista final : {eliminar_valor_lista(lista_a, lista_con_valores_a_eliminar)}")
#ejercicio 5
def ordenar_(lista:list[int]) -> bool : 
    """
    la funcion va a retornar True si la lista esta ordenada de manera ascendente y False en caso contrario
    siempre y cuando la lista no este vacia y este ordenada. 
    contrato : la lista no debe estar vacia y debe estar ordenada
    precondiciones : la lista no debe estar vacia
    postcondiciones : la lista debe estar ordenada
    """
    return lista == sorted(lista)


print(ordenar_([1,2,3,4,5,6,7,8,9])) # True
print(ordenar_([9,8,7,6,5,4,3,2,1])) # False
assert ordenar_([1,2,3,4,5,6,7,8,9]) == True
assert ordenar_([9,8,7,6,5,4,3,2,1]) == False
assert ordenar_(["a","b","c"]) == True
assert ordenar_(["c","b","a"]) == False

#ejercicio 6 
def normalizar(lista: list[int]) -> list[float]:
    """
    Normaliza los valores de una lista de números enteros a una escala de 0 a 1.
    Contrato: La lista no debe estar vacía.

    """
    if not lista:
        raise ValueError("La lista no debe estar vacía.")
    return [x / sum(lista) for x in lista] # Normaliza los valores a una escala de 0 a 1
print(normalizar([1,2,2]))
assert normalizar([1,2,2]) == [0.2, 0.4, 0.4] # Normaliza a [0.2, 0.4, 0.4]
assert normalizar([9,9,9,13]) == [0.225, 0.225, 0.225, 0.325] #aproximado

#ejercicio 7 
def intercalando(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Intercala dos listas de números enteros y las vuelve en una nueva lista(se añade a la lista 1 -__-) con todos los elementos de las 2 anteriores listas.

    """
    for i,v in enumerate(lista2): # Itera sobre los elementos de la segunda lista
        indice = i * 2 + 1 # Calcula el índice de inserción
        lista1[indice:indice] = [v] # Inserta el elemento de la segunda lista en la posición calculada
    return lista1

print(intercalando([1,3,5],[2,4,6])) # [1,2,3,4,5,6]

assert intercalando([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
assert intercalando([10,20,30],[15,25,35]) == [10,15,20,25,30,35]
assert intercalando([1,2,3],[4,5,6]) != [1,4,2,5,3,2]

#ejercicio 8    
def impares(inicio:int, fin:int) -> list[int]:
    """
    Genera una lista de números impares en un rango dado entre inicio y fin.
    """
    return [i for i in range(inicio, fin + 1) if i % 2 != 0]

impares_lista = impares(100, 200)
print(impares_lista)  # Muestra la lista de números impares entre 100 y 
#ejercicio 9
def multiplo_7_no_de_5(inicio:int , fin:int)-> list[int]:
    """
    Genera una lista de números que son múltiplos de 7 pero no de 5 en un rango dado
    """
    return [i for i in range(inicio, fin + 1) if i % 7 == 0 and i % 5 != 0]
print(multiplo_7_no_de_5(1, 100))
#ejercicio 10
cantidad = 20
lista_random = [random.randint(1,100) for x in range(cantidad)]
impares = list(filter(lambda x : x % 2 != 0 , lista_random))
print(lista_random)
print(impares)
#ejercicio 11
def cargar_pacientes() -> list[list[int]]:
    """
    carga una lista de pacientes con su id de afiliado y que tipo de turno tienen (0 - urgencia , 1 - normal )
    """
    matriz = [[],[]]
    while True :
        
        pacientes = int(input("Ingrese su numero de afiliado : "))
        if pacientes >= 1000 and pacientes <= 9999:
            matriz[0].append(pacientes)
            while True :
                turno = int(input("Ingrese su tipo de turno ( 0. - Urgencia y 1. - turno normal ) : "))
                if turno >=0 and turno <= 1 :
                    matriz[1].append(turno)
                    break
                else :
                    print( "Turno invalido ingrese nuevamente")
                
        elif pacientes == -1 :
            return matriz
            break
        else :
            print("Numero de afiliado no encontrado. ")
def informe_(encabezado:list[str],matriz:list[list[int]]) -> None :
    """
    informa la cantidad de turnos normales y de urgencia que tuvo cada paciente si es que esta registrado
    en la lista de pacientes
    """
    cantidad_turno =  []
    
    lista_sin_repetidos = list(dict.fromkeys(matriz[0]))
    for no_rep in lista_sin_repetidos:
        turno_urgencia = 0
        turno_normal = 0  
        for afiliado,turn in zip (matriz[0],matriz[1]) :
            if no_rep == afiliado :
                if turn == 0:
                    turno_urgencia += 1
                else :
                    turno_normal += 1
    
        cantidad_turno.append((no_rep,turno_normal,turno_urgencia))
    informe = [dict(zip(encabezado,turno)) for turno in cantidad_turno]
    for inf in informe :
        print()
        print(inf)
def informe_ind(encabezado:list[str],matriz:list[list[int]]) -> None :
    """
    Informa los turnos de un paciente específico.
    """
    lista_sin_repetidos = list(dict.fromkeys(matriz[0]))
    info = [] 

    while True:
        for no_rep in lista_sin_repetidos :
            
            print()
            print(f"Numero de afiliado : {no_rep} ")
            
        codigo = int(input("Ingrese un numero de afiliado "))
        if codigo == -1 :
            print("Saliendo..")
            break
        else :
            turno_urgencia = 0
            turno_normal = 0
            encontrado = False
            
            for afiliado,turno in zip(matriz[0],matriz[1]):
                if codigo == afiliado :
                    encontrado = True
                    if turno == 0:
                        turno_urgencia += 1
                    else :
                        turno_normal += 1
            if encontrado :
                info.append((codigo,turno_normal,turno_urgencia))
                print(f"Resumen del afiliado {codigo}: Normal : {turno_normal}, Urgencia : {turno_urgencia}")
            else : 
                print("Código no encontrado.")
def main_ () -> None :
    """
    Función principal que gestiona el menú y las opciones del programa.
    """
    opciones = ["Salir","Informe de los pacientes atendidos y cuantas veces fue atendido de urgencia y por turno","ingresar numero de afiliado e informar sus turnos ",]
    encabezado = ["Numero de afiliado","Turno","Urgencia"]
    matriz = cargar_pacientes()
    guion = lambda n : "-" * n 
    while True:
        for i, v in  enumerate (opciones):
            print(guion(50))
            op = 0 
            print(f"{i} - {v}")
        op = input("Ingrese una de las opciones : ")
        if op == "0":
            print("Saliendo...")
            break
        elif op == "1":
            informe_(encabezado,matriz)
        elif op == "2":
            informe_ind(encabezado,matriz) 
            
main_()
#ejercicio 12
         