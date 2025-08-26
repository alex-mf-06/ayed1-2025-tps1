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
#print(validar_fecha(29, 2, 2020)) # True
#print(validar_fecha(29, 2, 2021)) # False
#print(validar_fecha(31, 4, 2020)) # False

def total_pago_viajes(cantidad:int) -> int:
    """
    Calcula el costo total de una cantidad de viajes aplicando descuentos por tramos.

    Contrato:
    - Precondiciones:
        * cantidad (int) debe ser mayor a 0.
    - Postcondiciones:
        * Devuelve el costo total como un entero.
        * Si cantidad <= 20 → sin descuento.
        * Si 20 < cantidad <= 30 → 20% descuento en los viajes adicionales.
        * Si 30 < cantidad <= 40 → 30% descuento en los viajes adicionales.
        * Si cantidad > 40 → 40% descuento en los viajes adicionales.
        * Si cantidad <= 0 → devuelve -1.
    """
     
    contador = 1
    precio = 1000
    total = 0
    if cantidad <= 0 :
        return -1
    for i in range(cantidad):
        if contador <= cantidad and contador <= 20 :
            contador += 1
            total += precio
        elif contador <= cantidad and contador <= 30 :
            contador += 1
            total +=  precio - precio * 0.2
        elif contador <= cantidad and contador <= 40 :
            contador += 1
            total += precio - precio * 0.3
        elif contador <= cantidad and contador > 40 :
            contador += 1
            total += precio - precio * 0.4
    return total
print(total_pago_viajes(22)) # Llama a la funcion para calcular el total a pagar por los viajes


def calcular_cambio(precio:int, pago: int)-> list :
    """
    Calcula el cambio total de una compra en billetes de distintas denominaciones.
    contrato:
    - Precondiciones:
        * precio (int) debe ser mayor a 0.
        * pago (int) debe ser mayor o igual a precio.
    - Postcondiciones:
        * Devuelve una lista con la cantidad de billetes de cada denominación.
        * Si pago < precio → devuelve [-1].
    """
    billetes = [5000, 1000, 500, 200, 100, 50, 10] # Lista de billetes disponibles
    if pago < precio:
        return [-1] # Si el pago es menor que el precio, retorna [-1]
    cambio = pago - precio # Calcula el cambio a devolver
    total_billetes = [] # Lista para almacenar la cantidad de billetes de cada denominacion
    for billete in billetes: # Itera sobre cada billete disponible
        total_billetes.append(cambio // billete) # Calcula la cantidad de billetes de esa denominacion
        cambio %= billete # Actualiza el cambio restante
    return total_billetes # Retorna la lista de billetes

billetes = [5000, 1000, 500, 200, 100, 50, 10]
precio = 12730
pago = 20000
if pago < precio:
    print("El pago es menor que el precio.")
else:
    salida = calcular_cambio(precio, pago) # Llama a la funcion para calcular el cambio
    print(f"Cambio a devolver: ${pago - precio}")
    for i,s in enumerate(salida):
        if s:
            print(f"{s} billetes de ${billetes[i]}") # Imprime la cantidad de billetes de cada denominacion

def es_oblongo(a:int)->bool:
    """
    Verifica si un número es oblongo.

    contrato: 
    - Precondiciones:
        * a (int) debe ser mayor o igual a 1.
    - Postcondiciones:
        * Devuelve True si a es un número oblongo, False en caso contrario.
        * Un número es oblongo si puede expresarse como el producto de dos enteros consecutivos.
        * Si a < 1 → devuelve False.
    """

    if a < 1:
        return False
    num = 1
    while num * (num + 1) <= a:
        if num * (num + 1) == a:
            return True
        num += 1
    return False
assert es_oblongo(6) == True
assert es_oblongo(8) == False
assert es_oblongo(12) == True
def es_triangular(num:int)->bool:
    """
    Verifica si un número es triangular.
    contrato:
    - Precondiciones:
        * num (int) debe ser mayor o igual a 1.
    - Postcondiciones:
        * Devuelve True si num es un número triangular, False en caso contrario.    
        * Un número es triangular si puede expresarse como la suma de los primeros n enteros positivos.
        * Si num < 1 → devuelve False.
    """
    if num < 1:
        return False
    n = 0
    triangular = 1
    while triangular < num:
        n += 1
        triangular = n * (n + 1) // 2
    return triangular == num
assert es_triangular(36) == True
assert es_triangular(8) == False
assert es_triangular(10) == True

#ejeercicio 6 TP1 :
def concatenar_numeros(a:int, b:int)->int:

    dig = 0
    aux = b
    while aux > 0:
        dig += 1
        aux //= 10
    a = a * (10 ** dig) 
    return a + b
assert concatenar_numeros(12, 34) == 1234




def dia_siguiente(dia:int, mes:int, anio:int)->tuple:
    if dia < 1 or mes < 1 or anio < 1:
        return (-1, -1, -1)
    dias_en_mes = [31, 28 + (1 if es_bisiesto(anio) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia > dias_en_mes[mes - 1]: # Verifica si el dia es valido para el mes y año dado
        return (-1, -1, -1)
    dia += 1
    if dia > dias_en_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return (dia, mes, anio)
assert dia_siguiente(28, 2, 2020) == (29, 2, 2020) # Año bisiesto
assert dia_siguiente(28, 2, 2021) == (1, 3, 2021)  # Año no bisiesto
assert dia_siguiente(31, 12, 2021) == (1, 1, 2022) # Fin de año
def dia_de_la_semana(dia:int, mes:int, anio:int)->int:
    """
    Calcula el día de la semana para una fecha dada usando la fórmula de Zeller.
    contrato:
    - Precondiciones:
        * dia (int) debe ser un día válido del mes.
        * mes (int) debe ser un mes válido (1-12).
        * anio (int) debe ser un año válido (mayor que 0).
        - Postcondiciones:
        * Devuelve un entero que representa el día de la semana (0=Domingo, 1=Lunes, ..., 6=Sábado).
        * Si la fecha es inválida → devuelve -1."""
    if mes < 3:
        mes += 12
        anio -= 1
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem
assert dia_de_la_semana(1, 1, 2022) == 6 # Sábado
#Ultimo ejercicio TP1 :
def guion(n=50) -> None:
    print('-' * n)

def generar_naranjas(cantidad:int) -> None:
    """Genera una cantidad de naranjas con pesos aleatorios y realiza un análisis de la cosecha.
       Contrato:
       - Precondiciones:
           * cantidad (int) debe ser mayor que 0.

       - Postcondiciones:
           * No devuelve ningún valor, pero imprime un análisis de la cosecha.
           * Se generan naranjas con pesos aleatorios entre 150 y 350 gramos.

    """
    nrj_jugo = []
    nrj_apto = []
    for _ in range(cantidad):
        naranja = rn.randint(150,350)
        if naranja > 300 or naranja < 200 :
            nrj_jugo.append(naranja)
        else:
            nrj_apto.append(naranja)
    
    print(f"La cosecha de naranjas es de: {cantidad} naranjas")
    guion()
    print(f"Naranjas para jugo: {len(nrj_jugo)}")
    guion()
    print(f"Naranjas aptas para consumo: {len(nrj_apto)}")
    
    # Formar cajones completos de 100 naranjas aptas
    cajones_aptas = len(nrj_apto) // 100
    sobrante_aptas = len(nrj_apto) % 100
    print(f"Cajones completos aptas: {cajones_aptas}")
    guion()
    print(f"Naranjas sobrantes aptas para próxima entrega: {sobrante_aptas}")
    
    # Peso total de las naranjas aptas que llenan cajones
    peso_total_apto = sum(nrj_apto[:cajones_aptas*100])
    peso_en_kg = peso_total_apto / 1000
    promedio_kg_cajon = peso_total_apto / cajones_aptas / 1000 if cajones_aptas > 0 else 0
    print(f"Peso total de cajones aptas: {peso_total_apto} gramos ({peso_en_kg:.2f} kg)")
    guion()
    print(f"Promedio por cajón: {promedio_kg_cajon:.2f} kg")
    
    # Distribución en camiones
    peso_camion = 500
    peso_minimo = 0.8 * peso_camion  # 80%
    camiones_necesarios = 0
    peso_restante = peso_en_kg
    
    while peso_restante > 0:
        if peso_restante >= peso_minimo:
            camiones_necesarios += 1
            if peso_restante >= peso_camion:
                peso_restante -= peso_camion
            else:
                peso_restante = 0
        else:
            print(f"Los cajones que quedan para la próxima entrega: {peso_restante:.2f} kg")
            break
    guion()
    print(f"Camiones necesarios: {camiones_necesarios}")

# Ejecutar
generar_naranjas(1_000_000)
