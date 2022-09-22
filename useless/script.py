import tkinter
from tkinter import *
root = tkinter.Tk()
tk = Tk()


#functions to be used in the game


def setup(): #setup function for game
    canvas = Canvas(tk, bg="white", height=600, width=600)
    tk.title("Snake Game") 
    canvas.create_oval(30,60,210,210, fill = "purple")
    #button = Button (root,bg="#c1eb9d", text = "Quit", width = 2, height = 2, command=root.destroy )
    #update and pack/place everything
    #button.place(x=500, y=2)
    btn = Button(tk, text = 'start game?', command = game)
    btn.pack()
    canvas.pack()

    tk.mainloop()


# The program that is run, calling of functions is below:

setup()



