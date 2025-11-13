
from typing import List, Tuple, Dict
import re

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
                    if anio >= 1900 and anio <= 2100:
                        if confirmar_dato("año", anio):
                            return anio
                    else:
                        print("El año debe ser entre 1900 a 2100.")
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
                           
                            return dia
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


def registrar_fecha_() -> Tuple[int, int, int]:
    
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
                return (anio, mes, dia)
        
            else:
                print("volviendo a ingresar la fecha... \n")


    except KeyboardInterrupt:
       print("\nOperación cancelada por el usuario.")
        
    except ValueError :
        print("No se puede convertir una palabra en un numero .")


def sumar_dias_a_Fecha(fecha: Tuple[int,int,int]) -> Tuple[int,int,int]:
    """
    Esta funcion se encarga de que el usuario ingrese la cantidad de dias 
    que se sumen en la fecha que se paso como parametro que es una tupla que representa el primer indice el año , el segundo el mes y el tercero el dia.
    precondiciones : 
     - La fecha que se recibe como parametro debe ser una tupla 
    postcondiciones : 
     - Retorna la tupla pero con las sumas de los dias ya echas . 

    """
    try :

        while True:
            dias = input("Ingrese la cantidad de días a sumar: ").strip()
            if dias.isdigit():
                dias = int(dias)
                break 
            else:
                print("El día debe ser un número entero.")
        anio, mes, dia = fecha
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        while True:
            meses[1] = 29 if es_bisiesto(anio) else 28
            dias_restantes_mes = meses[mes - 1] - dia
            if dias <= dias_restantes_mes:
                dia += dias
                break
            else:
                dias -= (dias_restantes_mes + 1)
                dia = 1
                mes += 1
                if mes > 12:
                    mes = 1
                    anio += 1
        return (anio, mes, dia)

    except TypeError:
        print("Ocurrio un error al convertir")
    except ValueError:
        print("Ocurrio un error al convertir")


def Validar_hora () -> int:
    """
    
    Esta funcion se encarga de que el usaurio ingrese una hora valida.
    no sale del bucle sin que sea una hora valida 
    precondiciones : no tiene 
    postcondiciones: Devuelve un entero que representa la hora.

    """
    
    while True:
            
            try :
                hora = input("Ingrese la hora del dia (0-23): ").strip()
                if hora.isdigit():
                    hora = int(hora)
                    if hora >= 0 and hora <= 23:
                        if confirmar_dato("hora", hora):
                            return hora
                        else : 
                            print("Cancelaste la confirmacion")
                    else:
                        print("La hora debe estar entre 0 y 23.")
                
                else:
                    print("La hora debe ser un número entero.")

            except TypeError:
                print("Ocurrio un error al convertir")
            except ValueError:
                print("Ocurrio un error al convertir")
            except KeyboardInterrupt:
                print("Solo vas a salir si ingresas una hora valida")
                continue
def validar_minutos() -> int:
    """
    
    Esta funcion se encarga de que el usuario ingrese minutos validos solo 
    va a poder salir si pone numero que entran entre 0 y 59.
    precondiciones : no tiene 
    postcondiciones : Devuelve un entero que representa los minutos.


    """
    while True:
        try :
            minutos = input("Ingrese los minutos : ").strip()

            if minutos.isdigit():
                minutos = int(minutos)
                if minutos >= 0 and minutos <= 59:
                    if confirmar_dato("minutos", minutos):
                        return minutos
                    else : 
                        print("Cancelaste la confirmacion")
                else:
                    print("Los minutos deben estar entre 0 y 59.")
            else:
                print("Los minutos deben ser un número entero.")


        except TypeError:
            print("Ocurrio un error al convertir")
        except ValueError:
            print("Ocurrio un error al convertir")
        except KeyboardInterrupt:
            print("Solo vas a salir si ingresas una hora valida")
            continue


    
def validar_horario() ->Tuple[int,int]:
    """
    Esta funcion se encarga de que el usuario ingrese tanto la hora como los minutos y despues de eso retorna una tupla que representa el horario . (hora,minutos) 
    precondiciones: no tiene 
    postcondicones : Devuelve una tupla que representa el horario.

    
    """
    try :
        hora = Validar_hora()
        minutos = validar_minutos()
        return (hora,minutos)

    except TypeError:
        print("Ocurrio un error al convertir")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def calcular_diferencia_entre_2_horarios (horario1:Tuple[int,int],horario2:Tuple[int,int]) ->None:
    """

    Esta funcion se encarga de validar las diferencias de tiempo entre los horarios .
    precondiciones: Los parametros deben ser Tuplas que contengan enteros que ademas tengan solo dos elemtentos cada tupla.
    postcondiciones: no devuelve nada solo muestra la difrencia de tiempo entre los dos horarios 
    
    """
    try:
        h1, m1 = horario1
        h2, m2 = horario2

        total_minutos1 = h1 * 60 + m1
        total_minutos2 = h2 * 60 + m2

        # Si horario2 es anterior a horario1, consideramos que pasó un día
        if total_minutos2 < total_minutos1:
            total_minutos2 += 24 * 60

        diferencia = total_minutos2 - total_minutos1
        horas_diferencia = diferencia // 60
        minutos_diferencia = diferencia % 60

        print(f"La diferencia de tiempo entre {horario1} y {horario2} es: {horas_diferencia} horas y {minutos_diferencia} minutos.")


    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def menu() -> None:
    """
    
    Esta funcion se encarga de mostrar el menu y ejecutar las opciones que tiene .
    
    """
    opciones = ("Sumar dias a una fecha","Calcular la diferencia entre dos horarios", "Salir")
    while True:
        for i , opcion in enumerate(opciones, start=1):
            print("="*30)
            print(f"{i}. {opcion}")
        opcion = input("Ingrese una opción: ").strip()
        if opcion == "1":
            fecha = registrar_fecha_()
            nueva_fecha =sumar_dias_a_Fecha(fecha)
            print(f"La nueva fecha luego de la suma es: {nueva_fecha[2]:02d}/{nueva_fecha[1]:02d}/{nueva_fecha[0]}")
        elif opcion == "2":
            horario1 = validar_horario()
            horario2 = validar_horario()
            calcular_diferencia_entre_2_horarios(horario1,horario2)
        elif opcion == "3":
            break
            

if __name__ == "__main__":
    menu()





