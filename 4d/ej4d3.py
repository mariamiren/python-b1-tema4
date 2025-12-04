"""
Implementa una función 'read_and_write', no recibe ningún parámetro debido a
que, dentro de la misma se debe solicitar la entrada de 2 datos mediante
teclado.

En el momento de solicitar el ingreso de los datos se debe considerar el
siguiente texto.
'Insert your name: ' El valor introducido debe ser de tipo str.
'Insert your age: ' El valor introducido debe ser de tipo int.

Se debe crear un archivo de texto 'file.txt' donde La información entrada
por consola debe ser guardada en dicho archivo y se debe imprimir por consola
desde el archivo de texto.

Parámetro:
No recibe ningún parámetro.

Ejemplo:
    Entrada:
        'Insert your name: ' Julio 
        'Insert your age: ' 30
    Salida:
        Julio
        30

Enunciat:

Implementa una funció 'read_and_write', no rep cap paràmetre a causa de
que, dins de la mateixa cal sol·licitar l'entrada de 2 dades mitjançant
teclat.

En el moment de sol·licitar l'ingrés de les dades s'ha de considerar el
següent text.
'Insert your name: ' El valor introduït ha de ser de tipus str.
'Insert your age: ' El valor introduït ha de ser de tipus int.

S'ha de crear un fitxer de text 'file.txt' on La informació entrada
per consola s'ha de guardar en aquest fitxer i s'ha d'imprimir per consola
des del fitxer de text.

Paràmetre:
No rep cap paràmetre.

Exemple:
     Entrada:
         'Insert your name: ' Juliol
         'Insert your age: ' 30
     Sortida:
         Juliol
         30

"""
import os
import sys 
from ej4d3.py import read_and_write

def read_and_write(capsys, monkeypatch):
    imput_values = ["Julio\n". "30\n"]
    monkeypatch.setartt('builtins.imput', lamdba_: imput_values.pop(0)
    
    read_and_write():
    
    assert os.path.isfile("file_txt"), "the file.txt, file should be created"
    with open ("file_txt", "r") as file:
        assert file.read() != "", "the file.txt, file should not be empty"
        
    captured = capsys.readouterr()
    assert captured.out.strip() == "Julio\n\n30", "the output should be 'Julio\\n\\30'"
   


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# read_and_write()
