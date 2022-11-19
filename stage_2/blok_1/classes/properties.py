class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color, favourite_food):
        self.__breed = breed
        self.__color = color
        self.__favourite_food = favourite_food


    def speak(self):
        print("Beep! Beep Imma Sheep: https://www.youtube.com/watch?v=CZlfbep2LdU")

    @property
    def breed(self):
        return self.__breed

    @property
    def color(self):
        return self.__color

    @property
    def favourite_food(self):
        return self.__favourite_food

    @favourite_food.setter
    def favourite_food(self, food):
        self.__favourite_food = food


azorek = Dog("Owczarek niemiecki", "Brązowy", "Kiełbasa")
su_kaa = Dog("Biały", "Jindo", "Ludzie zadający za dużo pytań")

print('azorek :')
print(f"{azorek.animal=}")
print(f"{azorek.breed=}")
print(f"{azorek.color=}")
print(f"{azorek.favourite_food=}")

print('su_kaa:')
print(f"{su_kaa.animal=}")
print(f"{su_kaa.breed=}")
print(f"{su_kaa.color=}")
print(f"{su_kaa.favourite_food=}")

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
Dog.animal = "akschually a KATZ lololol"
print(f"{su_kaa.animal=}")

