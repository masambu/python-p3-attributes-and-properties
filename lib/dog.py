#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = 'Dog', breed = 'Beagle'):

        self.set_name(name)
        if hasattr(self, '_name'):  # Only set breed if name is valid
            self.set_breed(breed)

    def get_name(self):
        print('Retrieving name.')
        return self._name

    def set_name(self, name):

        if type(name) == str and 1 <= len(name) <= 25:
            print(f'Setting name to {name}.')
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        print('Retrieving breed')
        return self._breed

    def set_breed(self, breed):
        
        if breed in APPROVED_BREEDS:
            print(f'Setting breed to {breed}.')
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

fido = Dog('Fido','Human')
print(fido.breed)