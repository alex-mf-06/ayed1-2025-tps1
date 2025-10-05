from typing import List
import random as rn
def cargar_pacientes()  -> List[int] :
    """
    Carga una matriz con los números de afiliado y el tipo de turno (0 para urgencia, 1 para turno normal).
    precondición: El número de afiliado debe estar entre 1000 y 9999 o -1 para finalizar.
    postcondición: Devuelve una matriz con dos listas: la primera con los números de afiliado y la segunda con los tipos de turno."""
    matriz = [[],[]]
    while True :
        try :
            pacientes = int(input("Ingrese su numero de afiliado : "))
        except ValueError:
            print("Error: Ingrese un número entero válido.")
            continue
        if pacientes >= 1000 and pacientes <= 9999:
            matriz[0].append(pacientes)
            while True :
                try :
                    turno = int(input("Ingrese su tipo de turno ( 0. - Urgencia y 1. - turno normal ) : "))
                except ValueError:
                    print("Error: Ingrese un número entero válido.")
                    continue
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
def informe_(encabezado:List[str],matriz:List[List[int]]) -> None :
    """
    Genera un informe de los pacientes atendidos y cuántas veces fueron atendidos de urgencia y por turno normal.
    precondición: La matriz debe contener dos listas: la primera con los números de afiliado y la segunda con los tipos de turno.
    postcondición: Imprime un informe con el número de afiliado, la cantidad de turnos normales y la cantidad de urgencias."""
    cantidad_turno =  []
    try : 
        if encabezado == [] or matriz == [] :
            raise ValueError("La matriz o el encabezado no deben estar vacíos.")
    except TypeError:
        raise TypeError("Error: La entrada no es una matriz válida o directamente no es una matriz .")

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
def informe_ind(encabezado:List[str],matriz:List[List[int]]) -> None :
    """
    Genera un informe individual de un paciente atendido, mostrando cuántas veces fue atendido de urgencia y por turno normal.
    precondición: La matriz debe contener dos listas: la primera con los números de afiliado y la segunda con los tipos de turno.
    postcondición: Imprime un informe con el número de afiliado, la cantidad de turnos normales y la cantidad de urgencias
    """
    lista_sin_repetidos = list(dict.fromkeys(matriz[0]))
    info = [] 

    while True:
        for no_rep in lista_sin_repetidos :
            
            print()
            print(f"Numero de afiliado : {no_rep} ")
        try :
            codigo = int(input("Ingrese un numero de afiliado "))
        except ValueError:
            print("Error: Ingrese un número entero válido.")
            continue
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
    Muestra un menú para que el usuario elija entre generar un informe de los pacientes atendidos o un informe individual de un paciente.
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
if __name__ == "__main__":

    main_() 