from typing import Final


class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color, favourite_food):
        self.__breed = breed
        self.__color = color
        self.__favourite_food = favourite_food


    def speak(self, addtional_comment: str = ""):
        print("Beep! Beep Imma Sheep: https://www.youtube.com/watch?v=CZlfbep2LdU")
        print(f"I'm a {self.__breed}")
        if addtional_comment:
            print(addtional_comment)

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
# su_kaa = Dog(color="Biały", breed="Jindo", favourite_food="Ludzie zadający za dużo pytań")

try:
    azorek.breed = "Jamnik"
except AttributeError as e:
    print("You can't change breed")

print('azorek :')
print(f"{azorek.animal=}")
print(f"{azorek.breed=}")
print(f"{azorek.color=}")
azorek.favourite_food = "Kiełbasa z grilla"
print(f"{azorek.favourite_food=}")

print('su_kaa:')
print(f"{su_kaa.animal=}")
print(f"{su_kaa.breed=}")
print(f"{su_kaa.color=}")
print(f"{su_kaa.favourite_food=}")

print("Koreański pies".center(80, "#"))
su_kaa.speak("Gib meh kimchi!")
print("Niemiecki pies".center(80, "#"))
azorek.speak()

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)
Dog.animal = "akschually a KATZ lololol"
print(f"{su_kaa.animal=}")
