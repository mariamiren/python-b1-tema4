"""
Enunciado:

Crea una función llamada 'count_fruits(fruits_list)' que reciba como parámetro una lista
de frutas y retorne un diccionario donde cada llave sea el nombre de una
fruta y su valor sea la cantidad de veces que aparece en la lista.

Parámetros:
    fruits_list: lista de frutas

Retorno:
    Un diccionario donde cada llave es el nombre de una fruta y su valor es
    la cantidad de veces que aparece en la lista.

Ejemplo:
    Entrada:
    fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
    count_fruits(fruits)

    Salida:
    {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}

Enunciat:

Crea una funció anomenada 'count_fruits(fruits_list)' que rebi com a paràmetre una llista
de fruites i retorni un diccionari on cada clau sigui el nom d'una
fruita i el seu valor sigui la quantitat de vegades que apareix a la llista.

Paràmetres:
     fruits_list: llista de fruites

Retorn:
     Un diccionari on cada clau és el nom d'una fruita i el seu valor és
     la quantitat de vegades que apareix a la llista.

Exemple:
     Entrada:
     fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
     count_fruits(fruits)

     Sortida:
     {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}    
"""


def count_fruits(fruits_list):
   fruits = [
       "apple",
       "banana",
       "orange",
       "apple",
       "kiwi",
       "banana",
       "kiwi",
       "kiwi",
       "kiwi",
   ]
    assert count_fruits(fruits) == {"apple": 2}, {"banana": 2}, {"orange": 1}, {"kiwi": 4}, "count_fruits does not return the correct value for the input ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']. It should be {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}" 
    fruits = []
    assert count_fruits(fruits) == {}, "count fruits does not return the correct value for input []. It should be {}, that is, empty"
    fruits == ["apple", "apple", "apple", "apple"]
    assert count_fruits(fruits) == {"apple": 4}, "count fruits does not return the correct value for input ['apple', 'apple', 'apple', 'apple']. It shoul be {'apple': 4}"
    fruits == ["apple", "banana", "kiwi"]
    assert count_fruits(fruits) == {"apple": 1, "banana": 1, "kiwi":1}, "count fruits does not return the correct value for input ['apple', 'banana', 'kiwi']. It should be {'apple': 1, 'banana': 1, 'kiwi':1}"

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']
# print(count_fruits(fruits))
