import tkinter
from tkinter import *
root = tkinter.Tk()


#functions to be used in the game


def setup(): #setup function for game
    canvas = tkinter.Canvas(root, bg="white", height=600, width=600)
    title = Label(root, text="Snake Game" , font=("Arial", 30))
    title.pack()
    canvas.create_oval(60,60,210,210, fill = "purple")
    button = Button (root,bg="#c1eb9d", text = "Quit", width = 2, height = 2, command=root.destroy )
    button.place(x=500, y=2)
    canvas.pack()
    root.mainloop()
def start():
    
    c = tkinter.Canvas(root, bg="white", height=200, width=300)
    label = Label(root, text="Start Game?" , font=("Arial", 20))
    label.pack()
    btn = Button (root,bg="#c1eb9d", text = "Yes", width = 2, height = 2, command=setup())
    b = Button (root,bg="#c1eb9d", text = "No", width = 2, height = 2, command=root.destroy )
    b.place(x=500, y=2)
    btn.place(x=400, y=200) 


# The program that is run, calling of functions is below:

start()



