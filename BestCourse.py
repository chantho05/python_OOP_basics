class BestCourse:
	website = "http://google.com"

	def __init__(self, name):
		self.name = name

course = BestCourse("Search for Python")
learn_command_line = BestCourse("Learn command line")

print (course.name)
print(BestCourse.website)

print(learn_command_line.name) #OBJECT_NAME.METHOD
print(BestCourse.website) #CLASS_NAME.METHOD