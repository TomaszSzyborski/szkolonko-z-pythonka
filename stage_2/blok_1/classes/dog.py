class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
azorek = Dog("Owczarek niemiecki", "Brązowy")
su_kaa = Dog("Biały", "Jindo")

print('azorek :')
print('azorek is a', azorek.animal)
print('Breed: ', azorek.breed)
print('Color: ', azorek.color)

print('su_kaa:')
print('su_kaa is a', su_kaa.animal)
print('Breed: ', su_kaa.breed)
print('Color: ', su_kaa.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)