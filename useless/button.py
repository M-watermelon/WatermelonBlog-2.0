

#game function
def game():
    print("game started!")



from tkinter import *
tk = Tk()
#setup function for game

btn = Button(tk, text = 'start game?', command = game)
    
btn.pack() #update and pack/place everything


#call functions
tk.mainloop()