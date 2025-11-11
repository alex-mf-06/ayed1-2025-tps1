import os 
import csv



ruta_formato1 = os.path.join("datos", "formato1empleados.txt")
ruta_formato2 = os.path.join("datos", "formato2empleados.txt")
ruta_formato1_csv = os.path.join("datos", "empleados_en_limpio1.csv")
ruta_formato2_csv = os.path.join("datos", "empleadoslimpio2.csv")

def formato_1() -> None:
    """
    Esta funcion se encarga de guardar los datos de los empleados segun el formato 1 .
    precondiciones: la ruta del archivo debe estar en la carpeta datos.
    postcondiciones: No retorna nada pero crea un archivo que va a guardar los datos en el formato 1 :   Los campos tienen longitud fija con un espacio de separación 
    entre ellos.
    """
    try:
        with open(ruta_formato1,"rt",encoding="utf-8") as fila_empleados:
            empleados = fila_empleados.readlines()
        registros = []
        for empleado in empleados:
            nombre = empleado[0:14].rstrip()
            fechaa= empleado[14:23].rstrip()
            domicilo = empleado[24:].rstrip()

            lista_limpia = [nombre,fechaa,domicilo]
            registros.append(lista_limpia)
        with open(ruta_formato1_csv,"wt",newline="",encoding="utf-8")as formato1:
            formato1 = csv.writer(formato1)
            for fila in registros:
                formato1.writerow(fila)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_formato1}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def formato_2() -> None : 
    """Esta funcion se va a encargar de que el foormato txt lo hace csv y ademas lo ordena 
    el contenido del txt debe ser asi : 10Pérez Juan082008021114Corrientes 348 .para despues con la funcion terimne asi Pérez Juan,20080211,Corrientes 348

    """
    try : 
        with open(ruta_formato2,"rt",encoding="utf-8") as fila_empleados:
            empleados = fila_empleados.readlines()
        registros = []
        for empleado in empleados:
            empleado = empleado.strip()
            campos = []
            indice = 0
            while True:
                largo = int(empleado[indice:indice+2]) #busca los digitos que serian la cantidad de caraacteres que hay en cada parte de nombres , fecha, direccion .
                indice += 2
                campo = empleado[indice:indice+largo] # guarda la parte que deberia menos los digitos que seria la cantidad de caracteres que llevaria la seccion de los tres que hay . 
                indice += largo # suma la canitda de largo de la seccion para que recorra y busque la siguiente seccion.
                campos.append(campo)
                if indice >= len(empleado):
                    break
            registros.append([campos[0],campos[1],campos[2]])
        with open(ruta_formato2_csv,"wt",newline="",encoding="utf-8")as formato2:
            formato2csv = csv.writer(formato2)
            formato2csv.writerows(registros)

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_formato2}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")






if __name__ == "__main__":
    formato_1()
    formato_2()

                    






            