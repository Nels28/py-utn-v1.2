import re
from tkinter import ttk
from tkinter import Frame
from tkinter import END
from tkinter import BooleanVar
from tkinter import Entry
from herramientas import etiqueta
from herramientas import boton
from modelo import abmcProductos


class MainWindow():
    def __init__(self, window):
        self.root = window
        self.root.title("Sistema de almacenamiento")
        self.f = Frame(self.root)
        self.root.geometry("600x400")
        self.hayStock = BooleanVar()
        codigo_precio = "^[\d]+$"
        codigo_letras = "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$"

        def chequearCampos():
            print(len(self.entry_categoria.get()))
            retorno = False
            # Chequeamos que el largo del campo sea igual a la coincidencias del regex con lo que se escribio en el entry
            try:
                if re.search(codigo_precio, self.entry_precio.get()).span()[1] == len(self.entry_precio.get()) and \
                        re.search(codigo_letras, self.entry_producto.get()).span()[1] == len(self.entry_producto.get()) and \
                        re.search(codigo_letras, self.entry_categoria.get()).span()[1] == len(self.entry_categoria.get()) and len(self.entry_producto.get()) > 0 and len(self.entry_precio.get()) > 0 and len(self.entry_categoria.get()) > 0:
                    retorno = True
            except (TypeError):
                print("ERROR")
                retorno = False
            finally:
                return retorno

        def actualizarTreeview(tree):
            records = tree.get_children()
            for element in records:
                tree.delete(element)
            for i in abmcProductos.consulta(self=""):
                tree.insert("", 0, text=i.id, values=(
                    i.nombreProducto, i.categoria, i.precio, i.stock))

        def altaP():
            if chequearCampos():
                abmcProductos.alta(self, self.entry_producto.get(
                ), self.entry_categoria.get(), self.entry_precio.get(), self.hayStock.get())
                actualizarTreeview(tree=self.tree)
                self.entry_producto.delete(0, END)
                self.entry_categoria.delete(0, END)
                self.entry_precio.delete(0, END)
            else:
                print("Algo salio mal")

        def bajaP():
            for item in self.tree.selection():
                data = (self.tree.item(item)["text"])
                abmcProductos.baja(self, id=data)
            actualizarTreeview(self.tree)

        def modificarP():
            if chequearCampos():
                item = self.tree.selection()
                id = self.tree.item(item)["text"]
                abmcProductos.modificar(self="", id=id, nombre=self.entry_producto.get(), categoria=self.entry_categoria.get(),
                                        precio=self.entry_precio.get(), stock=self.hayStock.get())
                actualizarTreeview(self.tree)
                self.entry_producto.delete(0, END)
                self.entry_categoria.delete(0, END)
                self.entry_precio.delete(0, END)

        # LABELS
        label_productoT = etiqueta(self.root, 0, 0, text="PRODUCTO")
        label_categoriaT = etiqueta(self.root, 0, 1, text="CATEGORIA")
        label_precioT = etiqueta(self.root, 0, 2, text="PRECIO")
        label_stockT = etiqueta(self.root, 0, 3, text="STOCK")
        label_producto = etiqueta(self.root, 5, 0, text="insertar nombre: ")
        label_categoria = etiqueta(self.root, 6, 0, text="insertar categoria: ")
        label_precio = etiqueta(self.root, 7, 0, text="insertar precio: ")
        label_signoPesos = etiqueta(self.root, 7, 2, text="$")
        label_espacioBlanco = etiqueta(self.root, 3, 0, text="")

        # TREEVIEW
        self.estilo = ttk.Style()
        self.estilo.theme_use("default")
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("PRODUCTO", "CATEGORIA", "PRECIO", "STOCK")
        self.tree.column("PRODUCTO", width=140, minwidth=40)
        self.tree.column("CATEGORIA", width=140, minwidth=40)
        self.tree.column("PRECIO", width=140, minwidth=40)
        self.tree.column("STOCK", width=140, minwidth=40)

        # HEADINGS
        self.tree.column("#0", width=30)
        self.tree.heading("PRODUCTO", text="PRODUCTO")
        self.tree.heading("CATEGORIA", text="CATEGORIA")
        self.tree.heading("PRECIO", text="PRECIO")
        self.tree.heading("STOCK", text="STOCK")

        self.tree.grid(row=1, column=0, columnspan=4)

        # BOTONES
        self.boton_alta = boton(self.root, 2, 0, text="NUEVO", command=altaP)
        self.boton_borrar = boton(
            self.root, 2, 1, text="ELIMINAR", command=bajaP)
        self.boton_modificar = boton(
            self.root, 2, 2, text="MODIFICAR", command=modificarP)

        # entrys
        self.entry_producto = Entry(self.root)
        self.entry_producto.grid(row=5, column=1)

        self.entry_categoria = Entry(self.root)
        self.entry_categoria.grid(row=6, column=1)

        self.entry_precio = Entry(self.root)
        self.entry_precio.grid(row=7, column=1)

        self.stock_CB = ttk.Checkbutton(
            self.root, text="hay stock:", variable=self.hayStock)
        self.stock_CB.grid(row=8, column=0, columnspan=2)

        actualizarTreeview(self.tree)
