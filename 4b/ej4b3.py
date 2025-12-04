"""
Enunciado:
Implementa una función llamada 'create_list(length_list)' que reciba de
parámetro un valor numérico entero llamado 'length_list'. Se deben retornar
dos listas de enteros que ilustren el almacenamiento de valores en la RAM
y en el Heap. Por lo tanto, la primera lista debe tener numeros enteros
aleatorios entre 0 y 100, que debe ser almacenada en la RAM; y la
segunda lista debe ser almacenada en el Heap reutilizando la primera lista
creada.

Para crear una lista en el Heap, se puede usar la libreria 'copy' y su función
'deepcopy(list)', en este ejemplo lo usaremos de la siguiente forma:
“copy.deepcopy('list_to_copy')”. 

Para crear numeros aleatorios se puede usar la librería 'random'. Deberás
añadir "import random" a tu código, y luego usar "random.randint(0, 100)"
para crear números aleatorios entre 0 y 100.

Considerar que en caso de que el número 'length_list' ingresado en la función
'create_list' se debe mostrar el error: 
ValueError("The number must be positive")

Parámetros:
    - length_list (int): Número entero que sea positivo.

Ejemplo:
    Entrada:
    create_list(4)

    Salida:
    ([17, 16, 30, 17], [17, 16, 30, 17])


Enunciat:

Implementa una funció anomenada 'create_list(length_list)' que rebi de
paràmetre un valor numèric enter anomenat 'length_list'. Cal retornar
dues llistes d'enters que il·lustrin l'emmagatzematge de valors a la RAM
i al Heap. Per tant, la primera llista ha de tenir números enters
aleatoris entre 0 i 100, que ha de ser emmagatzemada a la RAM; i la
segona llista ha de ser emmagatzemada al Heap reutilitzant la primera llista
creada.

Per crear una llista al Heap, es pot fer servir la llibreria 'copy' i la seva funció
'deepcopy(list)', en aquest exemple el farem servir de la següent forma:
“copy.deepcopy('list_to_copy')”.

Per crear números aleatoris es pot fer servir la llibreria 'random'. Hauràs de
afegir "import random" al teu codi, i després utilitzar "random.randint(0, 100)"
per crear números aleatoris entre 0 i 100.

Considerar que en cas que el número 'length_list' ingressat a la funció
'create_list' s'ha de mostrar l'error:
ValueError("The number must be positive")

Paràmetres:
     - length_list (int): Número enter que sigui positiu.

Exemple:
     Entrada:
     create_list(4)

     Sortida:
     ([17, 16, 30, 17], [17, 16, 30, 17])

"""
import copy
import random


def create_list(length_list):
    """
    Creates two lists of integers to illustrate the difference between RAM and
    Heap memory.

    Args:
    length_list: A numeric integer value indicating the length of the lists to
    be created.

    Returns:
    A tuple containing two lists of integers, the first one created in RAM and
    the second one created in Heap by reusing the first list.
  """
    
def test_create_list_returns_tuple_of_two_lists():
    
    #GIVEN
    length_list = 4
    
    #WHEN
    result = create_list(length_list)
    
    #THEN
    assert insinstance(result, tuple)
    assert len(result) == 2,
    assert insinstance(result[0], list),
    assert insinstance(result[1], list),

def test_create_list_lits_have_same_length():

    #GIVEN
    length_list = 6
    
    #WHEN
    ram_list, heap_list = create_list(length_list)

    #THEN
    assert len(ram_list) == len(heap_list)

def test_create_list_ram_list_contains_random_integers():

    #GIVEN
    length_list = 7

    #WHEN
    ram_list, _ = create_list(length_list)
    
    #THEN
    assert all(insinstance(i, int) for i in ram_list), "the first list returned by create_list should contain only integers"
    assert all(0<=i<=100 for i in ram_list), "the first list returned by create_list should contain only integers between 0 and 100"

def test_create_list_heap_list_is_a_copy_of_ram_list():

    #GIVEN
    length_list = 8

    #WHEN
    ram_list, heap_list = create_list(length_list)

    #THEN
    assert ram_list == heap_list, "the second list returned by create_list should be a copy of the first list"
    assert id(ram_list) != id(heap_list), "the second list returned by create_list should be a copy of the first list"

def test_create_list_with_zero_lentg():

    #GIVEN
    length_list = 0

    #WHEN
    ram_list, heap_list = create_list(length_list)

    #THEN
    assert len(ram_list) == 0, "the first list returned by create_list should be empty for lentg_list 0"
    assert len(heap_list) == 0, "the second list returned by create_list should be empty for lentg_list 0"    

def test_create_list_with_negative_length():

     #GIVEN
    length_list = -5

    #WHEN / THEN
    with pytest.raises(ValueError):
        create_list(length_list)
    
    
    
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(create_list(6))
