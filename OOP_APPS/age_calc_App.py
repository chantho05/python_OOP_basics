#Age Calculator App
from PIL import Image, ImageTk
import datetime
import tkinter as tk
#create frame
window = tk.Tk()
window.geometry("400x400")
#set title to screen
window.title("Age Calculator App")
#now = datetime.date(1989, 10, 5)
#print(datetime.date.today() - now)
#create frame geometry


#Adding Labels
year_label = tk.Label(text="Year")
year_label.grid(column = 0, row = 1)

month_label = tk.Label(text="Month")
month_label.grid(column = 0, row = 2)

day_label = tk.Label(text="Day")
day_label.grid(column = 0, row = 3)

#Text boxes

year_entry = tk.Entry()
year_entry.grid(column = 1, row= 1)

month_entry = tk.Entry()
month_entry.grid(column = 1, row= 2)

day_entry = tk.Entry()
day_entry.grid(column = 1, row= 3)

def calculate_age():
	print(year_entry.get())
	print(month_entry.get())
	print(day_entry.get())
	person = Person("You", datetime.date(int(year_entry.get()), 
										int(month_entry.get()),
									    int(day_entry.get())))


	print(person.age())
	text_answer = tk.Text(master=window, height=2, width=15)
	text_answer.grid(column=1, row=5)
	answer_text = "{name} are {age} years old!".format(name=person.name, age= person.age())
	text_answer.insert(tk.END, answer_text)



calculate_button = tk.Button(text = "Calculate Now", command = calculate_age)
calculate_button.grid(column = 1, row = 4)







class Person:
	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year
		return age

image = Image.open("/Users/cuore/Desktop/Basic_Python_OOP/python_image.jpg")
image.thumbnail((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row = 0)


#user = Person("Mike", datetime.date(1989, 10, 5))

#print(user.name, user.birthdate, user.age())


window.mainloop()
