import tkinter as tk
from tkinter import ttk
import webbrowser

#URL = "websites_name"

def Doorbell(event):
	print("You rang the Doorbell")


def click_go(event):
	webbrowser.open_new_tab("https://www.google.com")#'URL' can be used without full URL

def Reviews(event):
	webbrowser.open_new_tab("https://www.cleverprogrammer.com/reviews")#If using URL use URL + "/blog" for example

window = tk.Tk()
window.geometry("300x200")


alabel = tk.Label(text="Door")
alabel.grid(column=0, row=0)


blabel = tk.Label(text="Website")
blabel.grid(column=1, row=0)


clabel = tk.Label(text="Review")
clabel.grid(column=2, row=0)


dlabel = tk.Label(text="Mangos")
dlabel.grid(column=3, row=0)


button = tk.Button(window, text="Doorbell")
button.grid(column = 0, row=1)


button2 = tk.Button(window, text="google")
button2.grid(column=1, row=1)


button3 = tk.Button(window, text="Reviews")
button3.grid(column=2, row=1)


button4 = tk.Button(window, text="20")
button4.grid(column=3, row=1)

button.bind("<Button-1>", Doorbell) 

button2.bind("<Button-1>", click_go)

button3.bind("<Button-1>", Reviews)



window.mainloop()





