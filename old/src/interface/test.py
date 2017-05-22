#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()
# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

