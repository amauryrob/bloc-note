#Imports de tkinter
import tkinter
from tkinter import * 
from tkinter.ttk import *

#Propriétées de la fenêtre
root = Tk()                           #créer une fenêtre
root.geometry("300x300")              #dimensions de cette fenêtre
root.title("Notes Rapides")           #nom de la fenêtre
root.configure(bg="#e0e065")          #arrière plan de couleur jaune
root.attributes('-topmost', True)     #fenêtre toujours en avant plan

#Zone de texte
zonetext = Text(root, bg="#e0e065")   #zone de texte
zonetext.pack()                       #afficher la zone de texre

#lancer la fenêtre
root.mainloop()                       #lancer le programme
