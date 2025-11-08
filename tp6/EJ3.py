import os
from typing import List


def grabarRangoAlturas() -> None:
    """
    Esta funcion permite al usuario ingresar alturas de inscriptos para diferentes deportes y guarda los datos en un archivo de texto según ciertas condiciones.
    - Los deportes disponibles son: Atletismo, Natación, Gimnasia y Fútbol
    - La altura debe estar entre 1.5 metros y 2.5 metros para ser registrada.
    precondicion: El archivo inscriptos_deportes.txt debe estar en la carpeta datos o se creará uno nuevo.
    postcondicion: Se agregan las alturas válidas al archivo inscriptos_deportes.txt junto con el deporte correspondiente.
    """
    try:
        deportes = ("Atletismo", "Natacion", "Gimnasia", "Futbol")
        while True:
            print("Deportes disponibles :") 
            for deporte in deportes:
                print(f"- {deporte}")

            deporte = (
                input(
                    "Ingrese el deporte que desea agregar los datos de los inscriptos (ingrese 'salir' para salir): "
                )
                .strip()
                .title()
            )

            if deporte not in deportes and deporte.lower() != "salir":
                print("Deporte no válido. Intente nuevamente.\n")
                continue

            elif deporte.lower() == "salir":
                print("Saliendo del programa.")
                break
            elif deporte in deportes:
                deportes = tuple(
                    disponible for disponible in deportes if disponible != deporte
                )  # Actualizar la lista de deportes disponibles 
            
                ruta_Archivo = os.path.join("datos", "inscriptos_deportes.txt")
                with open(ruta_Archivo, "a", encoding="utf-8") as file:
                    file.write(f"{deporte}: \n")
                    while True:
                        try:
                            altura = float(
                                input(
                                    f"Ingrese la altura del inscripto en {deporte} en metros (ingrese un valor negativo para finalizar): "
                                ).strip()
                            )
                            if altura < 0:
                                print("Finalizando ingreso de alturas.\n")
                                break
                            elif altura >= 1.5 and altura <= 2.5:
                                file.write(f"{altura}\n")
                                print(
                                    f"Altura {altura} m para {deporte} registrada exitosamente.\n"
                                )
                            else:
                                print(
                                    "Altura inválida. Debe estar entre 1.5 m y 2.5 m. Intente nuevamente.\n"
                                )
                        except ValueError:
                            print(
                                "Entrada inválida. Por favor, ingrese un número válido para la altura.\n"
                            )
                        except KeyboardInterrupt:
                            print("\nOperación cancelada por el usuario.")
                            break

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def grabar_promedios_alturas() -> None:
    """
    Lee las alturas de los inscriptos desde el archivo inscriptos_deportes.txt, calcula el promedio de alturas para cada deporte y guarda los resultados en promedios_alturas.txt.
    precondicion: El archivo inscriptos_deportes.txt debe existir en la carpeta datos.
    postcondicion: Se crea o actualiza el archivo promedios_alturas.txt con los promedios de alturas por deporte.
    """
    try:
        ruta_alturas= os.path.join("datos", "Promedios_alturas.txt")
        ruta_Archivo = os.path.join("datos", "inscriptos_deportes.txt")
        with open(ruta_Archivo, "rt", encoding="utf-8") as f_alturas, \
         open(ruta_alturas, "wt", encoding="utf-8") as f_promedios:
            
            promedios = 0
            contador = 0
            deporte_actual = None
            for linea in f_alturas:
                linea = linea.strip()
                if not linea:
                    continue
                if ":" in linea:
                    if deporte_actual and contador > 0:
                        promedio = promedios / contador
                        f_promedios.write(f"{deporte_actual}: {promedio:.2f} metros .\n")

                    deporte_actual = linea
                    promedios = 0
                    contador = 0

                else:
                    try:
                        altura = float(linea)
                        promedios += altura
                        contador += 1
            

                    except ValueError: 
                        print(f"error se quiso convertirn en un numero un {linea}")
                        continue
            if deporte_actual and contador > 0:
                        promedio = promedios / contador
                        f_promedios.write(f"{deporte_actual}: {promedio:.2f} metros .\n")
   
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_Archivo}' no se encontró.")
    
    except TypeError:
        print(f"Error en la parte de recorrido")
    except ValueError:
        print(f"Error en la parte de de la suma de los promedios")

def mostrar_mayor_alturas_deportes() -> None:
    """
    
    Esta funcion se va a encargar de Usar una ruta de archivo que va a estar dentro de la funcion para mostrar la persona mas alta de cada deporte.
    Si es que el archivo que se use este crgado en caso contrario le va a mostrar un mensaje de que no hay datos cargados de los deportes.
    
    
    """
    try:
        ruta_alturas= os.path.join("datos", "inscriptos_deportes.txt")
        
        with open(ruta_alturas, "rt", encoding="utf-8") as alturas : 
            if not alturas:
                print("No hay datos cargados de los deportes.")
                return
            
            mayor= 0 
            deporte_actual = None
            
            
            for altura in alturas:
                altura = altura.strip()
                if not altura:
                    continue
                elif ":" in altura:
                    if mayor >0:
                        print(f"El mayor del deporte {deporte_actual} es {mayor} metros.")
                    deporte_actual = altura
                    mayor = 0
                else:
                    try:
                        altura = float(altura)
                        if altura > mayor:
                            mayor = altura
                    except ValueError:
                        print("Erorr en pasar una linea a float")
            if deporte_actual and mayor > 0 :
                print(f"El mayor del deporte {deporte_actual} es {mayor} metros.")

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_alturas}' no se encontró.")
    except TypeError:
        print(f"Error en la parte de recorrido")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def menu()->None:

    """
    
    Esta funcion se encarga de mostrar las opciones de las funciones que se hicieron 
    para hacer el menu . 
    precondiciones : no tiene parametros . 
    
    """
    ruta_promedios = os.path.join("datos", "promedios_alturas.txt")
    opciones = ("Cargar las inscripciones de los integrantes de los juegos "
    "deportivos panamericanos ","Mostrar el promedio de altura por deportes","Mostrar la persona más alta de cada deporte")    
    try:    
        while True:
            for i , v in enumerate(opciones, start=1):
                print(f"{i}. {v}\n")     
            opcion = input("Ingrese una opción: ")  

            if opcion == "1":
                grabarRangoAlturas()
            elif opcion == "2":
                grabar_promedios_alturas()
                with open(ruta_promedios, "rt", encoding="utf-8") as promedios:
                    print(promedios.read() ) 
            elif opcion == "3":
                mostrar_mayor_alturas_deportes()
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")



    
if __name__ == "__main__":
    
    menu()


        
            