import os 
import csv
import re
from typing import List, Tuple, Dict 


pisos = 10
habitaciones = 6
total_habitaciones = pisos * habitaciones



def confirmar_dato(etiqueta: str, valor: str) -> bool:
    """
    Solicita al usuario que confirme si un dato ingresado es correcto.
    Precondiciones:
        - etiqueta: str, la etiqueta del dato (por ejemplo, "DNI", "nombre").
        - valor: str, el valor del dato a confirmar.
    Postcondiciones:
        - Devuelve True si el usuario confirma que el dato es correcto ('s') y False si no lo confirma.
    """

    while True:
        try : 
            confirmacion = (
                input(
                    f"¿Confirma que el {etiqueta} '{valor}' es correcto? (s/n): ")
                .strip()
                .lower()
            )
            if confirmacion in ("s", "n"):
                return confirmacion == "s"
            print("Respuesta inválida. Por favor ingrese 's' o 'n'.")
        except KeyboardInterrupt: 
            continue


def confirmar_nombre() -> str:
    """solicita, valida y confirma un nombre de usuario.
    El nombre debe tener al menos 6 caracteres y  puede contener solo letras,
    acentos, 'ñ' y espacios."""
    regex_nombre = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{6,}$")

    while True:
        nombre = input(
            "Ingrese el nombre y apellido de la persona :  ").strip()
        

        if nombre.strip() and regex_nombre.match(nombre):
            if confirmar_dato("nombre", nombre):
                return nombre  # Si el usuario confirma el nombrey apellido va a salir del bucle principal

        else:
            print("Nombre inválido. No puede estar vacío.")
            continue


def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
    Args:
        anio (int): El año a evaluar.
    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    try:
        anio = int(anio)
    except ValueError:
        return False
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_anio() -> int: 
    """
    Esta funcion se encarga de que el usuario ingrese bien el año y no sale de aca hasta que confrme que el año que puso lo confirme que esta bien 


    """
    try :
        
        while True:
            try :
                anio = input("ingrese el año: ").strip()
                if anio.isdigit():
                    anio = int(anio)
                    if anio >= 2025:
                        if confirmar_dato("año", anio):
                            return anio
                    else:
                        print("El año debe ser mayor o igual a 2025.")
                else:
                    print("El año debe ser un número entero.")
            except KeyboardInterrupt:
                continue
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except ValueError :
        print("No se puede convertir")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
def validar_mes() -> int:
        """
        Esta funcion se encarga de validar el mes que ingrese el usaurio sea un 
        mes valido que no sea un numero negativo y no se pase de los 12 meses.
        precondiciones : no tiene parametros.
        postcondiciones : devuelve un entero representando el mes. 

        """
        
        while True:
            try: 
                
                mes = input("Ingrese el mes (1-12): ").strip()
                if mes.isdigit():
                    mes = int(mes)
                    if mes > 0 and mes <= 12:
                        if confirmar_dato("mes", mes):
                            mes = f"{mes:02d}"
                            return mes
                    else:
                        print("El mes debe estar entre 1 y 12.")
                else:
                    print("El mes debe ser un número entero.")
            except KeyboardInterrupt:
                continue
            except ValueError :
                print("No se puede convertir")

        



def confirmar_informacion(informacion: Dict) -> bool:
    """
    Esta funcion se encarga de que la persona vea la imformacion que paso
    como parametro para que la persona verifique si esta bien su ingormacion
    y retorna True si es positivo la informacion y False si no lo es.
    precondiciones : la funcion le deben dar como parametro un diccionario.
    postcondiciones: devuelve True si la persona confirma la informacion
    y False si no lo hace.

    """
    try:
        while True:
            for clave, valor in informacion.items():
                print("="*30)
                print(f"{clave}: {valor}")
            
            confirmacion = (
                    input(f"¿Confirma que la informacion es correcta? (s/n): ").strip().lower()
                )
            if confirmacion in ("s", "n"):
                return confirmacion == "s"
            else:
                print("Respuesta inválida. Por favor ingrese 's' o 'n'.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
        return False

def validar_dia(anio: int, mes: int) -> int:
    """
    Esta funcion se encarga de que el usuario ingrese una fecha valida segun el 
    el mes y el año .
    precondiciones: los parametros que se necesita deben ser enteros que representan 
    uno el año y el otro el mes . 
    postcondiciones : devuelve una fecha que representa uno de los validos segun el mes y el año .

    """
    try: 
        anio = int(anio)
        mes = int(mes)
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if es_bisiesto(anio):
            meses[1] = 29
        while True:
            try:
                dia = input(f"Ingrese el día (1-{meses[mes - 1]}): ").strip()

                if dia.isdigit():
                    dia = int(dia)
                    if dia >= 1 and dia <= meses[mes - 1]:
                        if confirmar_dato("día", dia):
                           
                            return f"{dia:02d}"
                    else:
                            print(f"El día debe estar entre 1 y {meses[mes - 1]}.")
                else:
                        print("El día debe ser un número entero.")
            except KeyboardInterrupt:
                print("\nOperación queriendo ser cancelada por el usuario.")
                continue
            except ValueError :
                    print("No se puede convertir")
    except ValueError:
        print("Error: La fecha debe contener números enteros.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def registrar_fecha() -> str:
    
    """
    Solicita interactivamente al usuario un año, mes y día, y los valida.
    Pide confirmación al usuario antes de devolver la fecha.

    Precondiciones:
      - Las funciones helper (validar_anio, validar_mes, validar_dia, 
        confirmar_informacion) deben estar definidas e importadas.
      - El programa debe estar ejecutándose en una terminal interactiva 
        que acepte 'input()'.

    Postcondiciones (en caso de éxito):
      - Devuelve una cadena (str) con la fecha confirmada por el usuario.
      - Devuelve una cadena (str) con la fecha confirmada por el usuario en formato 'dd/mm/yyyy'.

    Postcondiciones (en caso de fallo):
      - Lanza 'KeyboardInterrupt' si el usuario cancela (Ctrl+C).
    """
    
    
    try :
        while True:
            anio = validar_anio()
            mes = validar_mes()
            dia = validar_dia(anio, mes)
            fecha = {
                "Día": dia,
                "Mes": mes,
                "Año": anio,
            }
            if confirmar_informacion(fecha):
                return f"{dia}/{mes}/{anio}"
        
            else:
                print("volviendo a ingresar la fecha... \n")


    except KeyboardInterrupt:
       print("\nOperación cancelada por el usuario.")
        
    except ValueError :
        print("No se puede convertir una palabra en un numero .")


def validar_hospedaje(fecha_ingreso: str, fecha_egreso: str) -> bool:
    """
    Valida que las fechas de ingreso y egreso sean válidas y que la fecha de egreso 
    sea posterior a la de ingreso.
    No utiliza la librería datetime.
    
    Parámetros:
        fecha_ingreso (str): Fecha de ingreso en formato 'dd/mm/yyyy'.
        fecha_egreso (str): Fecha de egreso en formato 'dd/mm/yyyy'.

    Retorna:
        bool: True si las fechas son válidas y coherentes, False en caso contrario.
    """

    try: 
        d1, m1, a1 = map(int, fecha_ingreso.split('/'))
        d2, m2, a2 = map(int, fecha_egreso.split('/'))
        if( a1 < a2) or (a1 == a2 and m1 < m2 )or (a1 == a2 and m1 == m2 and d1 < d2): 
            return True # Va a retornar True solamente si el egreso es mayor al ingreso 
        else:
            return False
    except TypeError:
        print("Ocurrio un error al convertir")
    except ValueError:
        print("Ocurrio un error al convertir")


def validar_cant_hospedantes() -> int:
    """
    
    Esta funcion  se encarga de que el usuario ingrese  una cantidad real de personas que se 
    van  a hospedar. 
    precondiciones: no tiene parametros 
    postcondiciones : solo va a salir del bucle cuando ingrese de 1 persona hasta 8 como maximo .
    
    """
    while True:
        try : 
            hospedantes = input("Ingrese la cantidad de ocupantes (1-8): ").strip()
            if hospedantes.isdigit():
                hospedantes = int(hospedantes)
                if hospedantes >= 1 and hospedantes <= 8:
                    return hospedantes
                else:
                    print("La cantidad de ocupantes debe estar entre 1 y 8.")
            else:
                print("ingrese numeros representando los hospedantes ")
        except KeyboardInterrupt:
            print("\n Solo se sale de aca cuando ingreses un numero valido")
            continue
        except ValueError :
            print("No se puede convertir")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


def registar_clientes (ruta_clientes: str) -> None:
    """
    
    Esta funcion se encarga de registrar a los clientes con su dni , el nombre de
    la perosna fecha de ingreso , fecha de egreso y la cantidad de ocupantes, ademas de guardarlos en un archivo .csv
    precondiciones : el parametro debe ser una ruta de archivo existente .
    postcondiciones : los datos se van a guradar a un archivo csv y no retorna nada. 
    
    """
    try :
        Re_dni= re.compile(r"^\d{7,8}$")
        dnis= [] 
        registrados =[]
        while True:

            dni = input("Ingrese el DNI (7 u 8 dígitos)(ingrese -1 para salir): ").strip()
            if Re_dni.match(dni):
                if dni not in dnis:
                    if confirmar_dato("DNI", dni):

                        dnis.append(dni)
                        while True:
                            nombre = confirmar_nombre()
                            while True:
                                fecha_ingreso = registrar_fecha()
                                fecha_egreso = registrar_fecha()
                                if validar_hospedaje(fecha_ingreso, fecha_egreso):
                                    break
                                else:
                                    print("La fecha de egreso debe ser posterior a la de ingreso.")
                            hospedantes = validar_cant_hospedantes()
                            registro = {
                                "DNI": dni,
                                "Nombre": nombre,
                                "Fecha de ingreso": fecha_ingreso,
                                "Fecha de egreso": fecha_egreso,
                                "Cantidad de ocupantes": hospedantes,
                            }
                            if confirmar_informacion(registro):
                                registrados.append(registro)
                                break
                    else :
                        print("El usuario cancelo la operacion")    
                else :
                    print("El DNI ya fue registrado")
            
            elif dni == "-1":
                break
            else :
                print("Error en el DNI deben ser digitos numericos")
        
        if registrados:
            with open(ruta_clientes, "w", newline="", encoding="utf-8") as archivo_csv:
                campos = ["DNI", "Nombre", "Fecha de ingreso", "Fecha de egreso", "Cantidad de ocupantes"]
                escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
                escritor_csv.writeheader()
                escritor_csv.writerows(registrados)
                
            
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_clientes}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def cargar_datos(ruta_archivo: str) -> List[Dict[str, int]]:
    """
    Carga una lista de diccionarios desde un archivo CSV de forma segura.

    Precondiciones:
        - ruta_archivo (str): La ruta completa al archivo .csv.
        - El CSV DEBE tener encabezados en la primera fila.

    Postcondiciones:
        - Devuelve una lista de diccionarios (List[Dict]).
        - Si el archivo no existe o está vacío, devuelve [].
    """
    datos = []
    try:
        # 'newline=""' es crucial para leer CSVs correctamente
        with open(ruta_archivo, mode='r', encoding='utf-8', newline='') as file:
            # csv.DictReader automáticamente usa la primera fila como 
            # las "claves" (keys) de los diccionarios.
            reader = csv.DictReader(file)
            
            for row in reader:
                datos.append(row)
        
        return datos

    except FileNotFoundError:
        print(f"Advertencia: Archivo CSV no encontrado en '{ruta_archivo}'. Se devolverá [].")
        # A diferencia de JSON, no lo creamos, porque no sabemos 
        # qué encabezados (columnas) debería tener.
        return []
        
    except (csv.Error, UnicodeDecodeError):
        # csv.Error si el formato es incorrecto
        # UnicodeDecodeError si la codificación 'utf-8' falla
        print(f"Advertencia: El archivo '{ruta_archivo}' está corrupto o tiene formato inválido. Se devolverá [].")
        return []
        
    except Exception as e:
        # Captura cualquier otro error
        print(f"Ocurrió un error inesperado al leer el archivo '{ruta_archivo}': {e}")
        return []



def asignar_clientes_habitaciones(ruta_clientes:str,ruta_habitaciones:str,pisos:int,habitaciones:int,habitaciones_totales:int) -> List[List[int]]:
     """
     Asigna clientes a las habitaciones disponibles del hotel y devuelve una matriz de ocupación.

    PRECONDICIONES:
    - El archivo `ruta_clientes` existe y contiene columnas válidas: 
      "DNI", "Fecha de ingreso", "Fecha de egreso", "Cantidad de ocupantes".
    - Las variables `pisos`, `habitaciones` y `ruta_habitaciones` están definidas 
      con valores enteros positivos.
    - La función `cargar_datos()` retorna una lista de diccionarios de clientes válidos.

    POSTCONDICIONES (caso exitoso):
    - Cada cliente se asigna a una habitación libre (1 = ocupada, 0 = libre).
    - Se genera un archivo CSV con las asignaciones realizadas.
    - Si hay más clientes que habitaciones, solo se asignan los primeros disponibles.

    POSTCONDICIONES (caso de error):
    - Si no se encuentra el archivo o no hay clientes, se devuelve la matriz vacía
      con todas las habitaciones libres (0).
    - Si ocurre un error inesperado, se informa por consola y se retorna la matriz vacía.

    RETORNO:
    List[List[int]]: Matriz bidimensional que representa el estado de ocupación 
    (1 = ocupada, 0 = libre).
     """
     
     try:
         habitaciones_totales = [[0]* habitaciones for _ in range(pisos)]
         clientes = cargar_datos(ruta_clientes)
         if len(clientes) > total_habitaciones:
             print(f"Advertencia: Hay {len(clientes)} clientes y solo hay {total_habitaciones} habitaciones disponibles.\n Solo se guardar los primero 60 clientes.")
             clientes = clientes[:total_habitaciones]
         
         if not clientes:
             print("No hay clientes para asignar habitaciones.")
             return habitaciones_totales
         
         lista_csv = []
         contador_cliente = 0
         for  p , piso in enumerate(habitaciones_totales):
             for h , habitacion in enumerate(piso):
                 
                 if contador_cliente < len(clientes):
                    habitaciones_totales[p][h] = 1
                    cliente = clientes[contador_cliente]

                    clientes_habitacion = {
                        "DNI": cliente["DNI"],
                        "Fecha de ingreso": cliente["Fecha de ingreso"],
                        "Fecha de egreso": cliente["Fecha de egreso"],
                        "Cantidad de ocupantes": cliente["Cantidad de ocupantes"],
                        "Piso": p +1 ,
                        "Habitación": h + 1,
                    }
                    lista_csv.append(clientes_habitacion)
                    contador_cliente += 1
                 else:
                    break
         if lista_csv:
             print(f"Se asignaron {len(lista_csv)} habitaciones a {len(clientes)} clientes.")
             with open(ruta_habitaciones, "w", newline="", encoding="utf-8") as hospedajes:
                 campos = ["DNI", "Fecha de ingreso", "Fecha de egreso", "Cantidad de ocupantes", "Piso", "Habitación"]

                 escritor_csv = csv.DictWriter(hospedajes, fieldnames=campos)
                 escritor_csv.writeheader()
                 escritor_csv.writerows(lista_csv)

             print(f"Se guardaron las asignaciones en '{ruta_habitaciones}'")
         return habitaciones_totales 
     except FileNotFoundError:
         print(f"Error: El archivo '{ruta_clientes}' no se encontró.")
         return habitaciones_totales
     except Exception as e:
         print(f"Ocurrió un error inesperado: {e}")
         return habitaciones_totales
                 
                 

def mostrar_piso_mayor_ocupacion_habitaciones(habitaciones: List[List[int]]) -> None:
    """
    Muestra por consola el número del piso con mayor cantidad de habitaciones ocupadas.

    PRECONDICIONES:
    - `habitaciones` es una lista de listas de enteros (matriz) donde:
        1 = habitación ocupada, 0 = habitación libre.
    - La matriz contiene al menos un piso y una habitación por piso.

    POSTCONDICIONES:
    - Se imprime el número del piso con más habitaciones ocupadas.
    - En caso de empate, se muestra el primer piso con esa cantidad máxima.
    - Si todas las habitaciones están libres, se indica que no hay ocupación.

    RETORNO:
    None
    """
    try :
        ocupaciones = [sum(piso) for piso in habitaciones]
        if ocupaciones:
            mayores= []
            mayor = 0
            for piso, ocupacion in enumerate(ocupaciones):
                if ocupacion > mayor:
                    mayor = ocupacion
                    mayores = [piso + 1]
                elif ocupacion == mayor:
                    mayores.append(piso + 1)
            if len(mayores) == 1:
                print(f"El piso con mayor ocupación es el piso {mayores[0]}.")
            else:
                print(f"Los pisos con mayor ocupación son los pisos {', '.join(map(str, mayores))} con todas la habitacioes ocupadas.")
        else:
            print("No hay habitaciones ocupadas.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    

def  Mostrar_cant_habitaciones_vacías(habitaciones: List[List[int]])-> None:
    """
    Muestra la cantidad total de habitaciones vacías en el hotel.

    PRECONDICIONES:
    - `habitaciones` es una lista de listas de enteros.
    - Cada valor interno debe ser 0 (vacía) o 1 (ocupada).

    POSTCONDICIONES (caso exitoso):
    - Se imprime por consola la cantidad total de habitaciones vacías.
    - No modifica la estructura original de `habitaciones`.

    POSTCONDICIONES (caso de error):
    - Si la matriz está vacía o contiene datos inválidos, se muestra un mensaje de advertencia.

    RETORNO:
    - None. Solo imprime resultados.
    """
    try :
        if habitaciones:
            habitaciones_vacias = sum(habitacion == 0 for piso in habitaciones for habitacion in piso )
            print(f"Hay {habitaciones_vacias} habitaciones vacías en el hotel.")
        else:
            habitaciones_vacias = 0
            print("No hay habitaciones registradas en el sistema.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def mostrar_piso_mayor_personas(ruta_habitaciones:str ) -> None:
    """
    PRECONDICIONES:
        - El archivo CSV debe existir.
        - Las columnas deben tener encabezado y estar separadas por comas.
        - 'Cantidad de ocupantes' y 'Piso' deben ser valores numéricos válidos.

    POSTCONDICIONES:
        - Se mostrará por pantalla el piso con mayor cantidad total de ocupantes.
        - Si el archivo está vacío o contiene errores, se mostrará un mensaje descriptivo.
    """
    try : 
        pisos_hospedantes = []
        with open (ruta_habitaciones,"r",encoding="utf-8") as file :
            pisos= csv.DictReader(file)
            piso_ = []
            contador = 1
            for fila in pisos: 
                
                ocupantes = int(fila["Cantidad de ocupantes"])
                if contador <= 6:
                    piso_.append(ocupantes)
                    contador +=1

                else :
                    pisos_hospedantes.append(piso_)
                    piso_ = []
                    contador = 1
            pisos_hospedantes.append(piso_)
            suma_ocupantes = [sum(piso) for piso in pisos_hospedantes]
            mayor_ocupacion= max(suma_ocupantes)
            pisos_maximos = [i + 1 for i, total in enumerate(suma_ocupantes) if total == mayor_ocupacion]
            if len(pisos_maximos) == 1:
                print(f"El piso con más personas es el piso {pisos_maximos[0]} con {mayor_ocupacion} ocupantes en total.")
            else:
                pisos_str = ', '.join(str(p) for p in pisos_maximos)
                print(f"Hay varios pisos con la mayor cantidad de ocupantes ({mayor_ocupacion} personas): pisos {pisos_str}.")

    except FileExistsError:
        print(f"La ruta {ruta_habitaciones} donde se encontraba los datos de los hospedantes fueron elminadas o estan corruptas.")
    except ValueError:
        print("Error: algunos valores numéricos no son válidos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    

def convertir_fecha(fecha_str: str) -> tuple:
    """Convierte 'dd/mm/aaaa' a (año, mes, día) para facilitar comparaciones."""
    d, m, a = map(int, fecha_str.split('/'))
    return (a, m, d)

def mostrar_proxima_habitacion_desocupada(ruta_habitaciones:str) -> None:
    """
    
    Muestra cuál será la próxima habitación en desocuparse según la fecha actual ingresada.
    
    PRECONDICIONES:
        - El archivo CSV indicado por `ruta_habitaciones` debe existir.
        - Debe contener las columnas: 'Fecha de egreso', 'Piso', 'Habitación' y 'DNI'.
        - La fecha actual se ingresa por teclado en formato 'dd/mm/aaaa'.

    POSTCONDICIONES:
        - Se mostrará la(s) habitación(es) con la fecha de egreso más cercana a la actual.
        - Si no hay fechas posteriores a la actual, se mostrará un mensaje informativo.

    """

    try:
        fecha_actual_str = registrar_fecha()
        fecha_actual = convertir_fecha(fecha_actual_str)

        registros = cargar_datos(ruta_habitaciones)

        if not registros:
            print("No hay datos de habitaciones registrados.")
            return
        fechas_validas = []
        for fila in registros:
            try:
                fecha_egreso = convertir_fecha(fila["Fecha de egreso"])
                if fecha_egreso >= fecha_actual:
                    fechas_validas.append((
                        fecha_egreso,
                        fila["Piso"],
                        fila["Habitación"],
                        fila["DNI"]
                    ))
            except (KeyError, ValueError):
                continue  # Ignora filas inválidas

        if not fechas_validas:
            print("No hay habitaciones próximas a desocuparse.")
            return

        
        fecha_minima = min(f[0] for f in fechas_validas) 

       
        proximas = [f for f in fechas_validas if f[0] == fecha_minima]

     
        fecha_texto = f"{fecha_minima[2]:02d}/{fecha_minima[1]:02d}/{fecha_minima[0]}"
        print(f"\n Próxima fecha de desocupación: {fecha_texto}")
        for _, piso, habitacion, dni in proximas:
            print(f" - Piso {piso}, Habitación {habitacion} (Huésped DNI {dni})")

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta_habitaciones}'.")
    except ValueError:
        print("Error: formato de fecha inválido. Use dd/mm/aaaa.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def dias_entre_fechas(ingreso: str, egreso: str) -> int:
    """Devuelve la diferencia en días entre dos fechas, sin usar datetime."""
    d1, m1, a1 = map(int, ingreso.split('/'))
    d2, m2, a2 = map(int, egreso.split('/'))
    return (a2 - a1) * 360 + (m2 - m1) * 30 + (d2 - d1)


def mostrar_huespedes_ordenados_por_estadia(ruta_habitaciones: str) -> None:
    """
    Muestra todos los huéspedes registrados en el hotel, ordenados por cantidad de días de alojamiento.
    
    PRECONDICIONES:
        - El archivo CSV `ruta_habitaciones` debe existir y contener las columnas:
          'DNI', 'Fecha de ingreso', 'Fecha de egreso', 'Piso', 'Habitación'.
    POSTCONDICIONES:
        - Se imprimirá una lista de huéspedes ordenados por duración del hospedaje (mayor a menor).
    """
    try:
        registros = cargar_datos(ruta_habitaciones)

        if not registros:
            print("No hay huéspedes registrados en el hotel.")
            return

        listado = []
        for fila in registros:
            try:
                dias = dias_entre_fechas(fila["Fecha de ingreso"], fila["Fecha de egreso"])
                listado.append({
                    "DNI": fila["DNI"],
                    "Piso": fila["Piso"],
                    "Habitación": fila["Habitación"],
                    "Días": dias
                })
            except (KeyError, ValueError):
                continue

        # Ordenar por cantidad de días (mayor a menor)
        listado.sort(key=lambda x: x["Días"], reverse=True)

        print("\n Huéspedes ordenados por cantidad de días de alojamiento:")
        for h in listado:
            print(f"="*50 ,"\n")
            print(f" - DNI {h['DNI']}: {h['Días']} días (Piso {h['Piso']}, Habitación {h['Habitación']})")
           


    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta_habitaciones}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def menu_principal():
    opciones = {
        "1": "Registrar clientes",
        "2": "Asignar habitaciones",
        "3": "Mostrar piso con mayor ocupación de habitaciones",
        "4": "Mostrar cantidad de habitaciones vacías",
        "5": "Mostrar piso con mayor cantidad de personas",
        "6": "Mostrar próxima habitación en desocuparse",
        "7": "mostrar huespedes ordenados por estadia",
        "8": "Salir"
    }

    ruta_clientes = os.path.join("datos", "clientes.csv")
    ruta_habitaciones = os.path.join("datos", "habitaciones.csv")

    habitaciones_matriz = [[0] * habitaciones for _ in range(pisos)]

    while True:
        print("\n" + "=" * 50)
        for k, v in opciones.items():
            print(f"{k}. {v}")


        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registar_clientes(ruta_clientes)
        elif opcion == "2":
            habitaciones_matriz = asignar_clientes_habitaciones(
                ruta_clientes, ruta_habitaciones, pisos, habitaciones, total_habitaciones
            )
        elif opcion == "3":
            mostrar_piso_mayor_ocupacion_habitaciones(habitaciones_matriz)
        elif opcion == "4":
            Mostrar_cant_habitaciones_vacías(habitaciones_matriz)
        elif opcion == "5":
            mostrar_piso_mayor_personas(ruta_habitaciones)
        elif opcion == "6":
            mostrar_proxima_habitacion_desocupada(ruta_habitaciones)
        elif opcion == "7":
            mostrar_huespedes_ordenados_por_estadia(ruta_habitaciones)
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()