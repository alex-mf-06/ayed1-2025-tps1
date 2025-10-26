def imprimir_1_a_100000() -> None:
    """Imprime los números del 1 al 100,000 en la consola.
    
    precondiciones: ninguna
    postcondiciones: ninguna
    """

    try: 
        i = 1
        while True: 
            print(i)
            i += 1
            if i > 100000:
                break
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        
    finally:
        confirmation = input("¿Desea continuar? (s/n): ")
        if confirmation.lower() == 's':
            imprimir_1_a_100000() #anteriormente hacia el while True pero si usaba el ctrl+c se paraba y no tapaba el error
        else:
            print("Proceso terminado.")
if __name__ == "__main__":
    imprimir_1_a_100000() 