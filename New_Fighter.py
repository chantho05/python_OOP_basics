class New_Fighter:
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10

	def attack(self, opponent):
		opponent.health = opponent.health - self.damage
		print("{} attacks {}".format(self.name, opponent.name))
		print("{} took {} damage!".format(opponent.name, self.damage))

	def __str__(self):
		return "{}s health is {}".format(self.name, self.health)

mike = New_Fighter("Mike")	
opponent = New_Fighter("Alicia")

#print(mike) #<__main__.New_Fighter object at 0x000001A4E6D37FD0>


print(mike) #Mike
print(opponent) #Alicia

opponent.attack(mike)

print(mike)

#Incorporating Inheritance

class Boxer(New_Fighter):
	def heal(self):
		self.health += 10


boxer_mike = Boxer("Boxer Mike")
print(boxer_mike)
print(boxer_mike.damage)
print(boxer_mike.health)

boxer_mike.heal()

print(boxer_mike)