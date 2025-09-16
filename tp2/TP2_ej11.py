import random as rn
def cargar_pacientes()  -> list[int] :
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