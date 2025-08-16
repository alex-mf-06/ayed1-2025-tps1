def registrar_positivos(cantidad):
    
    """Registra una cantidad de numeros positivos ingresados por el usuario.
    Args:
        cantidad (int): La cantidad de numeros positivos a registrar.
    Returns:
        list: Una lista con los numeros positivos ingresados.
    """
    lista = []
    for i in range(cantidad): # Repite el proceso para la cantidad especificada
        num = -1 # Inicializa num con un valor negativo para entrar al bucle
        while num < 0 : # Mientras el numero sea negativo, solicita un nuevo numero
            num = int(input("Ingrese un numero positivo: "))
            if num < 0: # Si el numero es negativo, muestra un mensaje de error
                print("El numero debe ser positivo")
        lista.append(num) # Agrega el numero positivo a la lista
    return lista # retorna la lista de numeros positivos

def buscar_mayor(a:int,b:int, c:int) -> int:
    """Busca el mayor numero en una lista de numeros(int).
    Args:
        lista (list): La lista de numeros a evaluar.
    Returns:
        int: El mayor numero encontrado o -1 si los mayores son duplicados.
    """
    lista = [a, b, c] # Crea una lista con los numeros proporcionados
    mayor = 0 # Inicializa el mayor con 0
    repetido = False # Inicializa repetido como False
    for num in lista: 
        if num == mayor: # Si el numero es igual al mayor, se marca como repetido
            repetido = True
        elif num > mayor:
            mayor = num # Si el numero es mayor que el actual mayor, se actualiza
            repetido = False # Reinicia repetido a False si se encuentra un nuevo mayor
    if repetido == False:
        return mayor # Retorna el mayor si no hay duplicados
    else:
        return -1 # Si hay duplicados, retorna -1
# tp1.py
m = registrar_positivos(3)
print(f"{buscar_mayor(m[0], m[1], m[2])}")
