#Imports de tkinter
import tkinter
from tkinter import * 
from tkinter.ttk import *

#Propriétées de la fenêtre
root = Tk()
root.geometry("300x300")
root.title("Notes Rapides")
root.configure(bg="#e0e065")
root.attributes('-topmost', True)

#Zone de texte
zonetext = Text(root, bg="#e0e065")
zonetext.pack()

#lancer la fenêtre
root.mainloop()
