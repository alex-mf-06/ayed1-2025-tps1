def cargar_clientes() -> list[int] :
    lista_clientes = []
    while True :
        cliente = int(input("Ingrese su numero de socio : "))
        if cliente == 0 :
            print("Saliendo....")
            break
        elif cliente >= 10_000 and cliente <= 99_999:
            lista_clientes.append(cliente)
        else:
            print("Numero de socio invalido...")
    return lista_clientes
def inf_de_usuarios(lista_socios:list[int]) -> None :
    list_sin_rep = list(dict.fromkeys(lista_socios))
    cantidad_de_ingreso = [lista_socios.count(no_rep) for no_rep in list_sin_rep] 
    for socio,ingreso in zip(list_sin_rep,cantidad_de_ingreso):
        print(f" Socio : {socio} Entro : {ingreso} al club. ")
def sacar_cliente(lista_socios:list[int]) -> None :
    list_sin_rep = list(dict.fromkeys(lista_socios))
    while True:
        print("Afiliados registrados:", ", ".join(str(user) for user in list_sin_rep))
        usuario = int(input(" Ingrese el numero de socio que desea eliminar registro : "))
        if usuario not in list_sin_rep :    
             print("Socio no encontrado. Intente nuevamente.")
        else:
            print("---Registros antes de eliminar---")
            print(f"En el club entraron : {len(lista_socios)}")
            user_a_eliminar =  lista_socios.count(usuario)
            
            lista_socios[:] = [socio for socio in lista_socios if socio != usuario]
            
            print(f"\nSe eliminaron {user_a_eliminar} ingreso(s) del socio {usuario}.")
            print("Registros después de eliminar:")
            print(f"En el club entraron : {len(lista_socios)}")
            list_sin_rep = list(dict.fromkeys(lista_socios))
            break 
    
            
            
                
def menu() -> None :
    opciones = ["Salir","informe de los ingresos de los socios en el dia ","eliminacion del registro de un socio que se dio de baja  "] 
    socios = cargar_clientes()
    while True :
        for i,op in enumerate(opciones) :
            print(f" {i} - {op}")
        opc = input(" Ingrese una opcion que desea :  ")
        if opc == "0":
            print(" Saliendo... ")
            break
        elif opc == "1" :
            inf_de_usuarios(socios)
        elif opc == "2" :
            sacar_cliente(socios)
        else :
            print(f"Ingreso de numero de socio invalido...")
            
menu()    
        
            