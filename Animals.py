#Including POLYMORPHISM
class Animal:
	def __init__(self, name):
		self.name = name

	def talk(self):
		pass


pet_mike = Animal("CAWWW")
print(pet_mike.name)
print(pet_mike.talk())


class Dog(Animal):
	def talk(self):
		return "Woof"

pet = Dog("Dot")
print (pet.name)
print(pet.talk())


class Cat(Animal):
	def talk(self):
		return "MEOW"

pets = Cat("Kibbles")
print(pets.name)
print(pets.talk())


