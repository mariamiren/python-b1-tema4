"""
Enunciado:
Crea una función llamada 'add_elapsed_time(dictionary, key, value)' que
almacenará el último registro del tiempo de carrera de los atletas.
La fucnión recibe como parámetros un diccionario llamado 'dictionary',
una clave llamada 'key' y un valor llamado 'value'. La función debe
ser capaz de agregar el nuevo elemento al diccionario utilizando la
clave y el valor proporcionados.

Si la clave ya existe en el diccionario, se debe reemplazar el valor
anterior por el nuevo valor. La función debe retornar el diccionario
actualizado.

Parámetros:
    dictionary = Un diccionario al que se debe agregar un nuevo elemento.
    key = Una cadena que representa la clave del nuevo elemento a agregar.
    value = El valor del nuevo elemento a agregar.

Ejemplo:
    Entrada:
    my_dict = {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}
    mi_diccionario = add_elapsed_time(my_dict, 'Juan', 8.6)

    Salida:
    {'Juan': 8.6, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}

Enunciat:

"""


def add_elapsed_time(dictionary, key, value):
    
    #Test con una lista vacía
    assert add_elapsed_time({}, "Juan", 8.6) == {"Juan": 8.6}, "add_elapsed_time does not return the correct value for input {}, 'Juan', 8.6. It should be {'Juan': 8.6}"
    
    
    #Test con un diccionario que ya tiene elementos
    my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
    assert add_elapsed_time(my_dict, "Juan", 8.6) == {
        "Juan": 8.6,
        "Peter": 14.2,
        "Sofia": 6.5,
        "Alex": 8.7,
    }, "add_elapsed_time does not return the correct value for input {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}, 'Juan', 8.6. It should be {'Juan': 8.6, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}"
    
    
    #Test con una clave nueva
    my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
    assert add_elapsed_time(my_dict, "Lucas", 11.2) == {
        "Juan": 8.6,
        "Peter": 14.2,
        "Sofia": 6.5,
        "Alex": 8.7,
        "Lucas": 11.2,
    }, "add_elapsed_time does not return the correct value for input {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}, 'Lucas', 11.2. It should be {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7, 'Lucas': 11.2}"
    
    
    #Test con un valor actualizado
     my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
    assert add_elapsed_time(my_dict, "Juan", 10.2) == {
        "Juan": 10.2,
        "Peter": 14.2,
        "Sofia": 6.5,
        "Alex": 8.7,
    }, "add_elapsed_time does not return the correct value for input {'Juan': 9.5, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}. It should be {'Juan': 10.2, 'Peter': 14.2, 'Sofia': 6.5, 'Alex': 8.7}"
        


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# my_dict = {"Juan": 9.5, "Peter": 14.2, "Sofia": 6.5, "Alex": 8.7}
# my_dict = add_elapsed_time(my_dict, "Juan", 8.8)
# my_dict = add_elapsed_time(my_dict, "Alice", 7.3)
# print(my_dict)
