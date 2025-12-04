"""
Enunciado:

Escribe una función llamada 'descending_list_iterator(numbers_list)' que tome una lista
de números como argumento y devuelva un iterador que genere los mismos
números de mayor a menor.

Parámetros:
    numbers_list (list): Lista de números enteros a ser ordenados.

Ejemplo:
    Entrada:
    [5, 1, 8, 3, 2]

    Salida:
    El iterador debería generar los números en el siguiente orden:
    8, 5, 3, 2, 1.

Enunciat:

Escriu una funció anomenada 'descending_list_iterator(numbers_list)' que prengui una llista
de números com a argument i torni un iterador que generi els mateixos
nombres de més gran a més petit.

Paràmetres:
     numbers_list (list): Llista de nombres enters a ser ordenats.

Exemple:
     Entrada:
     [5, 1, 8, 3, 2]

     Sortida:
     L'iterador hauria de generar els números en l'ordre següent:
     8, 5, 3, 2, 1.

"""


def descending_list_iterator(numbers_list):
    
    #test with empty list
    assert descending_list_iterator([])) == [], "descending_list_iterator does not return the correct value for input []. It sould be [], that is, empty"
    
    #test with a list of one element
    assert descending_list_iterator([7]) == [7], "descending_list_iterator does not return the correct value for input [7]. It sould be [7]"

    #test with a list of multiple elements
    assert descending_list_iterator([7, 3, 5, 8]) == [7, 2, 1, 5], "descending_list_iterator does not return the correct value for input [7, 3, 5, 8]. It sould be [7, 2, 1, 5]"

    #test with a list of repeated elements
    assert descending_list_iterator([1, 1, 1, 1]) == [1, 1, 1, 1], "descending_list_iterator does not return the correct value for input [1, 1, 1, 1]. It sould be [1, 1, 1, 1]"
    
    #test with a list of negative elements
    assert descending_list_iterator([-1, -5, -3, -2]) == [-5, -4, -3, -2], "descending_list_iterator does not return the correct value for input [-1, -5, -3, -2]. It sould be [-5, -4, -3, -2]"
    
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# numeros = [2, 3, 6, 9, 11, 12, 15, 18]
# print(list(descending_list_iterator(numeros)))  
