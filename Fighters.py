class Fighters:
	def __init__(self, name, style, location):
		self.name = name
		self.style = style
		self.location = location 


michael = Fighters("michael", "MuayThai", "Thailand")


alicia = Fighters("Alicia", "Boxing", "Eloy")

print("My name is " + michael.name, "I Fight in " + michael.style, "and I am from " + michael.location)
print( "My name is " + alicia.name, "I fight in " + alicia.style, "and I am from " + alicia.location)

		