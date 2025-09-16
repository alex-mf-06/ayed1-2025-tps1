import random as rn
def guion(n=50) -> None:
    print('-' * n)
def generar_naranjas(cantidad:int) -> None:
    """Genera una cantidad de naranjas con pesos aleatorios y realiza un análisis de la cosecha.
       Contrato:
       - Precondiciones:
           * cantidad (int) debe ser mayor que 0.

       - Postcondiciones:
           * No devuelve ningún valor, pero imprime un análisis de la cosecha.
           * Se generan naranjas con pesos aleatorios entre 150 y 350 gramos.

    """
    nrj_jugo = []
    nrj_apto = []
    for _ in range(cantidad):
        naranja = rn.randint(150,350)
        if naranja > 300 or naranja < 200 :
            nrj_jugo.append(naranja)
        else:
            nrj_apto.append(naranja)
    
    print(f"La cosecha de naranjas es de: {cantidad} naranjas")
    guion()
    print(f"Naranjas para jugo: {len(nrj_jugo)}")
    guion()
    print(f"Naranjas aptas para consumo: {len(nrj_apto)}")
    
    # Formar cajones completos de 100 naranjas aptas
    cajones_aptas = len(nrj_apto) // 100
    sobrante_aptas = len(nrj_apto) % 100
    print(f"Cajones completos aptas: {cajones_aptas}")
    guion()
    print(f"Naranjas sobrantes aptas para próxima entrega: {sobrante_aptas}")
    
    # Peso total de las naranjas aptas que llenan cajones
    peso_total_apto = sum(nrj_apto[:cajones_aptas*100])
    peso_en_kg = peso_total_apto / 1000
    promedio_kg_cajon = peso_total_apto / cajones_aptas / 1000 if cajones_aptas > 0 else 0
    print(f"Peso total de cajones aptas: {peso_total_apto} gramos ({peso_en_kg:.2f} kg)")
    guion()
    print(f"Promedio por cajón: {promedio_kg_cajon:.2f} kg")
    
    # Distribución en camiones
    peso_camion = 500
    peso_minimo = 0.8 * peso_camion  # 80%
    camiones_necesarios = 0
    peso_restante = peso_en_kg
    
    while peso_restante > 0:
        if peso_restante >= peso_minimo:
            camiones_necesarios += 1
            if peso_restante >= peso_camion:
                peso_restante -= peso_camion
            else:
                peso_restante = 0
        else:
            print(f"Los cajones que quedan para la próxima entrega: {peso_restante:.2f} kg")
            break
    guion()
    print(f"Camiones necesarios: {camiones_necesarios}")

# Ejecutar
generar_naranjas(1_000_000)