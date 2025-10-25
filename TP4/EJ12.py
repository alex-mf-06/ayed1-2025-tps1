def crear_baraja() -> list[str] :
    """
    Esta función crea una baraja de cartas española con 40 cartas.
    
    Precondiciones:
    - No hay precondiciones para esta función.
    
    Postcondiciones:
    - La función retorna una lista que representa una baraja de cartas española.
    """
    palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
    baraja = [f"{numero} de {palo}" for palo in palos for numero in numeros]
    return baraja

if __name__ == "__main__":
    baraja = crear_baraja()
    qaw = [carta  for carta in baraja]
    for carta in qaw:
        print(f"La carta es: {carta}")
