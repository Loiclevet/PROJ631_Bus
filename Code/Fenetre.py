# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:32:28 2022

@author: levetl
"""

from tkinter import * 

fenetre = Tk()

photo = PhotoImage(file="sibra-fb.png")

canvas = Canvas(fenetre,width=350, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

fenetre.mainloop()

