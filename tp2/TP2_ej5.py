def ordenar_(lista:list[int]) -> bool : 
    """
    la funcion va a retornar True si la lista esta ordenada de manera ascendente y False en caso contrario
    siempre y cuando la lista no este vacia y este ordenada. 
    contrato : la lista no debe estar vacia y debe estar ordenada
    precondiciones : la lista no debe estar vacia
    postcondiciones : la lista debe estar ordenada
    """
    return lista == sorted(lista)


print(ordenar_([1,2,3,4,5,6,7,8,9])) # True
print(ordenar_([9,8,7,6,5,4,3,2,1])) # False
assert ordenar_([1,2,3,4,5,6,7,8,9]) == True
assert ordenar_([9,8,7,6,5,4,3,2,1]) == False
assert ordenar_(["a","b","c"]) == True
assert ordenar_(["c","b","a"]) == False
