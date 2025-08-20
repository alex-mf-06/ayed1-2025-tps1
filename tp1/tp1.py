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
#m = registrar_positivos(3)
#print(f"{buscar_mayor(m[0], m[1], m[2])}")

# ejercicio 2 TP1 : 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
    Args:
        anio (int): El año a evaluar.
    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
def validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Valida si una fecha es correcta.
    Args:
        dia (int): El día a validar.
        mes (int): El mes a validar.
        anio (int): El año a validar.
    Returns:
        bool: True si la fecha es válida, False en caso contrario.
    """
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Lista de dias por mes
    if anio < 1: # Verifica si el año es valido
        return False
    if es_bisiesto(anio): # Si el año es bisiesto, febrero
        meses[1] = 29
    if mes > 0 and mes < 13: # Verifica si el mes es valido
        if dia > 0 and dia <= meses[mes - 1]: # Verifica si el dia es valido
            return True
    return False
print(validar_fecha(29, 2, 2020)) # True
print(validar_fecha(29, 2, 2021)) # False
print(validar_fecha(31, 4, 2020)) # False

def total_pago_viajes():
    precio = 963 # Precio del peaje
    while True:
        cantidad_viajes = int(input("Ingrese la cantidad de viajes realizados en este mes: ")) # Solicita la cantidad de viajes
        if cantidad_viajes <= 0: # Verifica si la cantidad es negativa
            print("La cantidad de viajes no puede ser negativa o cero. Intente nuevamente.")
        elif cantidad_viajes <= 20:  
            descuento = 0 

        elif cantidad_viajes <= 30: # Si la cantidad de viajes es mayor a 20 
            descuento = 0.2

        elif cantidad_viajes <= 40: # Si la cantidad de viajes es mayor a 30
            descuento = 0.3

        else: # Si la cantidad de viajes es mayor a 40
            descuento = 0.4

        total = cantidad_viajes * precio * (1 - descuento)
        if descuento == 0:
            print(f"El total a pagar por {cantidad_viajes} viajes es: ${total:.2f} (sin descuento)")
            
        else:
            print(f"El total a pagar por {cantidad_viajes} viajes es: ${total:.2f} (con un descuento del {descuento * 100:.0f}%)")
        break
total_pago_viajes() # Llama a la funcion para calcular el total a pagar por los viajes