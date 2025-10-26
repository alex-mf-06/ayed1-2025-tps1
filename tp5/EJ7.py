import random as rn 
def adivinar_numero()->None:
    """
    Juego donde el usuario debe adivinar 
    un número aleatorio entre 1 a 500.
    precondiciones: ninguna

    postcondiciones: ninguna
    """


    numero = rn.randint(1,500)
    intentos = 0
    print("¡Bienvenido al juego de adivinar el número!")
    while True:
        try:
            entrada = input("ingrese un número entre 1 y 500 : ")
            entrafa_int = int(entrada)
            intentos += 1
            if entrafa_int == numero:
                print(f"¡Felicidades! Has adivinado el número {numero} en {intentos} intentos.")
                break
            elif entrafa_int < numero:
                print("El número es mayor. Intenta de nuevo.")
            else:
                print("El número es menor. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except KeyboardInterrupt:
            print("\nJuego interrumpido por el usuario.")
            break

if __name__ == "__main__":
    adivinar_numero()