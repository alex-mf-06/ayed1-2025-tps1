def enter_a_romano(numero :int) -> str :
    """
    Convierte un número entero a su representación en número romano.

    Precondiciones:
        - El parámetro 'numero' debe ser un valor (preferiblemente string o int)
          que pueda ser interpretado como un número entero.
        - Para una conversión exitosa, el valor numérico debe estar en el
          rango de 1 a 3999, inclusive.

    Postcondiciones:
        - Devuelve una cadena de caracteres (str) con el número romano
          correspondiente si la entrada es válida.
        - Devuelve la cadena "el numero debe ser un entero" si la entrada
          no puede convertirse a un número entero.
        - Devuelve la cadena "el numero debe estar entre 1 y 3999" si el
          número está fuera del rango válido.
    """
    try:
        numero = int(numero)
    except ValueError:
        return "el numero debe ser un entero"
    if numero < 1 or numero > 3999 :
        return"el numero debe estar entre 1 y 3999"

    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    resultado = ""
    i = 0
    while True : 
        if numero == 0 :
            break
        for _ in range(numero // valores[i]): # recorre el resultado de la divison es decir que si la persona ingreso 3000 el primer valor que recorre es 1000  entonces solo el for va iterar 3 veces 
            resultado += simbolos[i] #Agrega los simbolos en la cariable reseltado siguiendo con el ejemplo de arriba aca se añaderia M == 1000
            numero -= valores[i] # 3000 - 1000  
        i+=1
    return resultado
numero = input("Ingrese un numero entero entre 1 y 3999 : ")
print(enter_a_romano(numero))
assert enter_a_romano("1") == "I"
assert enter_a_romano("2432") == "MMCDXXXII"
assert enter_a_romano("hola") == "el numero debe ser un entero"

