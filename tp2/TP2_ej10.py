#ejercicio 10
import random


cantidad = 20
lista_random = [random.randint(1,100) for x in range(cantidad)]
impares = list(filter(lambda x : x % 2 != 0 , lista_random))
print(lista_random)
print(impares)