from typing import List
def cargar_clientes() -> List[int] :
    """
    Carga una lista con los números de socios que ingresan al club. 
    precondición: El número de socio debe estar entre 10,000 y 99,999 o 0 para finalizar.
    postcondición: Devuelve una lista con los números de socios."""
    lista_clientes = []
    while True :
        try:

            cliente = int(input("Ingrese su numero de socio : "))
        except ValueError:
            print("Error: Ingrese un número entero válido.")
            continue

        if cliente == 0 :
            print("Saliendo....")
            break
        elif cliente >= 10_000 and cliente <= 99_999:
            lista_clientes.append(cliente)
        else:
            print("Numero de socio invalido...")
    return lista_clientes


def inf_de_usuarios(lista_socios:List[int]) -> None :
    """
    genera un informe de los socios que ingresaron al club y cuántas veces ingresaron.
    precondición: La lista no debe estar vacía y debe ser una lista de enteros.
    postcondición: Imprime un informe con el número de socio y la cantidad de ingresos
    """
    list_sin_rep = list(dict.fromkeys(lista_socios))
    cantidad_de_ingreso = [lista_socios.count(no_rep) for no_rep in list_sin_rep] 
    for socio,ingreso in zip(list_sin_rep,cantidad_de_ingreso):
        print(f" Socio : {socio} Entro : {ingreso} al club. ")


def sacar_cliente(lista_socios:List[int]) -> None :
    """
    Elimina todos los registros de un socio que se dio de baja.
    precondición: La lista no debe estar vacía y debe ser una lista de enteros.
    postcondición: Imprime la cantidad de registros eliminados y la lista actualizada de socios."""
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
    """
    Muestra un menú para que el usuario elija entre generar un informe de ingresos o eliminar un registro de socio.
    
    """
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
if __name__ == "__main__":             
    menu()    
        
            