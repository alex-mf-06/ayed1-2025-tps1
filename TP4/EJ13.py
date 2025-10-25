
UNIDADES = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
DECENAS = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
ESPECIALES = {
    10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
    16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"
}
CENTENAS = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]


def _convertir_grupo_de_tres(n: int) -> str:
    """
    Función auxiliar para convertir un número de hasta 3 dígitos (0-999) a palabras.
    Es llamada por la función principal para procesar el número en bloques.
    precondiciones:
    - n es un entero en el rango 0-999.
    postcondiciones:
    - Retorna una cadena que representa el número en palabras.
    """
    try:
        if not isinstance(n, int) or not (0 <= n <= 999):
            raise ValueError("La entrada para _convertir_grupo_de_tres debe ser un entero entre 0 y 999.")

        # Descomponer el número de 3 dígitos en centenas, decenas y unidades.
        c = n // 100  # Obtiene la centena
        d = (n % 100) // 10  # Obtiene la decena
        u = n % 10  # Obtiene la unidad

        partes = []  # Lista para almacenar las partes del número en texto

        if c > 0:  # Si hay centenas
            if c == 1 and (d > 0 or u > 0):  # Caso especial para "ciento" (ej: ciento veinte)
                partes.append("ciento")
            else:  # Para "cien", "doscientos", etc.
                partes.append(CENTENAS[c])

        decenas_y_unidades = n % 100  # El número formado por decenas y unidades
        if decenas_y_unidades > 0:  # Si hay decenas o unidades
            if 10 <= decenas_y_unidades <= 19:  # Números especiales del 10 al 19
                partes.append(ESPECIALES[decenas_y_unidades])
            elif 21 <= decenas_y_unidades <= 29:  # Números del 21 al 29
                partes.append(f"veinti{UNIDADES[u]}")
            else:  # Para el resto de los números
                if d > 0:  # Añade la decena (ej: "treinta")
                    partes.append(DECENAS[d])
                if u > 0:  # Añade la unidad (ej: "uno")
                    if d > 0:  # Si hay decena, se une con "y" (ej: "treinta y uno")
                        partes.append("y")
                    partes.append(UNIDADES[u])

        return " ".join(partes)  # Une todas las partes con espacios

    except (TypeError, IndexError, ValueError) as e:
        # Captura cualquier error inesperado durante la conversión del grupo
        raise ValueError(f"Error interno al convertir el grupo de tres dígitos: {e}")

def numeros_a_letras(numero_str: str) -> str:
    """
    Esta función convierte un número entero en su representación en palabras en español.

    Precondiciones:
    - El parámetro 'numero_str' debe ser un string que represente un número entero no negativo.

    Postcondiciones:
    - La función retorna una cadena que representa el número en palabras en español.
    - Lanza ValueError si el parámetro no es un número entero válido o es negativo.
    """
    try:
        numero = int(numero_str)
    except ValueError:
        raise ValueError("La entrada debe ser un string que represente un número entero.")

    if numero < 0:
        raise ValueError("El número debe ser no negativo.")

    if numero == 0:
        return "cero"

    if numero > 999_999_999_999_999:
        raise ValueError("El número es demasiado grande. El máximo soportado es 999,999,999,999,999.")

    # Lista de sufijos para miles, millones, billones, etc.
    sufijos = ["", "mil", "millón", "billón"]

    num_str = str(numero).zfill((len(str(numero)) + 2) // 3 * 3) #
    grupos = [int(num_str[i:i+3]) for i in range(0, len(num_str), 3)]

    partes = []
    num_grupos = len(grupos)

    for i, grupo in enumerate(grupos):
        if grupo == 0:
            continue

        indice_sufijo = num_grupos - i - 1  # Calcular el índice del sufijo EJEMPLO: 0,1,2,3
        sufijo = sufijos[indice_sufijo] # Obtener el sufijo correspondiente ejemplo: mil, millón, billón

        # Convertir el grupo de tres dígitos a palabras
        texto_grupo = _convertir_grupo_de_tres(grupo)

        # Casos especiales para "un" y plurales
        if sufijo == "mil":
            if texto_grupo == "uno":
                partes.append("mil")
            else:
                partes.append(f"{texto_grupo} mil")
        elif sufijo in ["millón", "billón"]:
            if texto_grupo == "uno":
                partes.append(f"un {sufijo}")
            else:
                partes.append(f"{texto_grupo} {sufijo}es")
        else: # Grupo de unidades
            partes.append(texto_grupo)

    
    resultado_final = " ".join(partes).strip()
    resultado_final = resultado_final.replace("uno millones", "un millón")
    resultado_final = resultado_final.replace("uno billones", "un billón")

    return resultado_final

if __name__ == "__main__":
    numero_input = input("Ingrese un número entero no negativo: ")
    try:
        resultado = numeros_a_letras(numero_input)
        print(f"Número en palabras: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

    



    