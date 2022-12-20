from tkinter import Label
from tkinter import Button


class etiqueta():
    def __init__(self, window=None, x=0, y=0, *args, **kwars):
        self.window = window
        etiqueta = Label(self.window, *args, **kwars)
        etiqueta.grid(row=x, column=y)


class boton():
    def __init__(self, window=None, x=0, y=0, *args, **kwars):
        self.window = window
        etiqueta = Button(self.window, *args, **kwars)
        etiqueta.grid(row=x, column=y)
