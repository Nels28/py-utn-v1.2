from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from modelo2 import Abmc
from tkinter import ttk

# from tktemas import temas


class Ventanita:
    def __init__(self, window):
        self.objeto_base = Abmc()
        self.root = window
        self.root.title("Tarea POO")

        self.titulo = Label(
            self.root,
            text="Ingrese sus datos",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=60,
        )
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w")

        self.producto = Label(self.root, text="Producto")
        self.producto.grid(row=1, column=0, sticky="w")
        self.cantidad = Label(self.root, text="Cantidad")
        self.cantidad.grid(row=2, column=0, sticky="w")
        self.precio = Label(self.root, text="Precio")
        self.precio.grid(row=3, column=0, sticky="w")

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val, self.c_val = StringVar(), DoubleVar(), DoubleVar()
        w_ancho = 20

        self.entrada1 = Entry(self.root, textvariable=self.a_val, width=w_ancho)
        self.entrada1.grid(row=1, column=1)
        self.entrada2 = Entry(self.root, textvariable=self.b_val, width=w_ancho)
        self.entrada2.grid(row=2, column=1)
        self.entrada3 = Entry(self.root, textvariable=self.c_val, width=w_ancho)
        self.entrada3.grid(row=3, column=1)

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="cantidad")
        self.tree.heading("col3", text="precio")
        self.tree.grid(row=10, column=0, columnspan=4)

        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.boton_alta.grid(row=6, column=1)

        self.boton_borrar = Button(
            self.root, text="Borrar", command=lambda: self.borrar()
        )
        self.boton_borrar.grid(row=8, column=1)

    def alta(
        self,
    ):
        self.objeto_base.alta(
            self.a_val.get(), self.b_val.get(), self.c_val.get(), self.tree
        )

    def borrar(
        self,
    ):
        self.objeto_base.baja(self.tree)

    # def modificar(
    #    self,
    # ):
    #    self.objeto_base.modificar(self.a_val.get(), self.b_val.get(), self.c_val.get(), self.tree)

    def actualizar(
        self,
    ):
        self.objeto_base.actualizar_treeview(self.tree)
