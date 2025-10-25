import re

def validar_y_listar_emails()->set[str]:
    """Solicita al usuario ingresar una lista de correos electrónicos separados por comas,valida cada correo utilizando una expresión regular y retorna una lista de correos válidos (deen ser alfanumerico). al menos un carácter y tiene que finalizar con .com o .com.ar.
    precondiciones: ninguna
    postcondiciones:
    - Retorna un conjunto de cadenas que representan los correos electrónicos válidos ingresados por el usuario.
    
    """

    emails_validos = set()
    expresion_regular = r'^[a-zA-Z0-9]+@[^@\s]+\.com(\.ar)?$'

    while True:
        entrada = input("ingrese un email : ")
        if entrada == "":
            break
        
        elif entrada in emails_validos:
            print(f"el email {entrada} ya existe")

        elif re.match(expresion_regular, entrada):
            emails_validos.add(entrada)
            print(f"el email {entrada} es valido y se ha agregado a la lista")

        else:
            print(f"el email {entrada} no es valido")
    return emails_validos

emails = validar_y_listar_emails()
print("Los emails validos son:")
for email in emails:
    print(email)
print("Los emails ordenados alfabeticamente son:")
lista_email_ordenada = sorted(emails,key=str.lower)

for email in lista_email_ordenada:
    print(email)
        