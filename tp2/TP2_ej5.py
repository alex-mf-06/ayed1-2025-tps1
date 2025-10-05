from typing import List
def ordenar_(lista:List[int]) -> bool : 
    """
    la funcion va a retornar True si la lista esta ordenada de manera ascendente y False en caso contrario
    siempre y cuando la lista no este vacia y este ordenada. 
    contrato : la lista no debe estar vacia y debe estar ordenada
    precondiciones : la lista no debe estar vacia
    postcondiciones : devuelve True si la lista esta ordenada de manera ascendente y False en caso contrario.
    """
    
    try:
        if len(lista) == 0:
            raise ValueError("La lista está vacía.")
    except TypeError:
        raise TypeError("Error: La entrada no es una lista válida.")            
        
    if lista == sorted(lista):
        return True
    elif lista == sorted(lista, reverse=True):
        return False
    else:
        return -1


print(ordenar_([1,2,3,4,5,6,7,8,9])) # True
print(ordenar_([9,8,7,6,5,1,3,2,1])) # -1 indica que no esta ordenada ni de manera ascendente ni descendente
assert ordenar_([1,2,3,4,5,6,7,8,9]) == True
assert ordenar_([9,8,7,6,5,4,3,2,1]) == False
assert ordenar_(["a","b","c"]) == True
assert ordenar_(["c","a","b"]) == -1
