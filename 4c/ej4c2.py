"""
Enunciado:
Se pide crear una interfaz "Vehicles" que tenga un método abstracto "drive".
Además, se deben crear las clases concretas "Car" y "Bicycle" que implementen
la interfaz "Vehicles".

El método "drive" debe imprimir "Driving a car" para la clase "Car" y "Riding
a bicycle" para la clase "Bicycle".

Parámetros:
    La clase Car y Bicycle no reciben parámetros.
        
Ejemplo:
    Entrada:
        car = Car()
        print(car.drive())

        bicycle = Bicycle()
        print(bicycle.drive())
    Salida:
        Driving a car
        Riding a bicycle


Enunciat:
Es demana crear una interfície "Vehicles" que tingui un mètode abstracte "drive".
A més, cal crear les classes concretes "Car" i "Bicycle" que implementin
la interfície "Vehicles".

El mètode "drive" ha d'imprimir "Driving a car" per a la classe "Car" i "Riding"
a bicycle" per a la classe "Bicycle".

Paràmetres:
     La classe Car i Bicycle no reben paràmetres.
        
Exemple:
     Entrada:
         car = Car()
         print(car.drive())

         bicycle = Bicycle()
         print(bicycle.drive())
     Sortida:
         Driving a car
         Riding a bicycle
"""
import pytest
from abc import ABC, abstractmethod
from ej4c2 import Car, Bicycle, Vehicles

    
    def test_drive_car(self):
        car = Car
        assert car drive() == "Driving a car", "Car drive() should return 'Driving a car'"


    def test_drive_bicycle(self):
        bicycle = Bicycle ()
        assert bicycle drive() == "Riding a bicycle", "Bicycle drive" should return 'Riding a bicycle'"
    
    
    def test_drive_vehicles_abstract_method(self):
        with pytest.raises(TypeError):
        vehicles = vehicles()
        vehicle.drive
    
        
    def test_drive_car_insinstance_of_vehicles_class(self):
        car = Car
        assert insinstance(car, vehicles), "Car should be a insinstance of vehicles"

    
    def test_drive_bicycle_insistance_of_vehicles_class(self):
        bicycle = Bicycle ()
        assert insinstance(bicycle, vehicles), "Bicycle should be a insinstance of vehicles"



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# car = Car()
# print(car.drive())

# bicycle = Bicycle()
# print(bicycle.drive())
