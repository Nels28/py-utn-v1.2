import sqlite3
from tkinter import ttk
import re

# ##############################################
# MODELO
# ##############################################
class Abmc:
    def __init__(
        self,
    ):
        try:
            con = sqlite3.connect("mibase.db")
            cursor = con.cursor()
            cursor.execute(
                """CREATE TABLE productos
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                producto varchar(20) NOT NULL,
                cantidad real,
                precio real)"""
            )
            con.commit()
        except:
            print("Error conexión")

    def conexion(
        self,
    ):
        con = sqlite3.connect("mibase.db")
        return con

    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM productos ORDER BY id ASC"
        con = self.conexion()
        cursor = con.cursor()
        datos = cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

    def cerrar_conexion(
        self,
    ):
        print("cerrar_conexion")

    def alta(self, producto, cantidad, precio, mitreeview):

        con = self.conexion()
        print(producto, cantidad, precio)
        cursor = con.cursor()
        data = (producto, cantidad, precio)
        sql = "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Estoy en alta todo ok")
        self.actualizar_treeview(mitreeview)

    def baja(self, mitreeview):

        valor = mitreeview.selection()
        print(valor)  # ('I005',)
        item = mitreeview.item(valor)
        print(
            item
        )  # {'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
        print(item["text"])
        mi_id = item["text"]

        con = self.conexion()
        cursor = con.cursor()
        # mi_id = int(mi_id)
        data = (mi_id,)
        sql = "DELETE FROM productos WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        # mitreeview.delete(valor)
        self.actualizar_treeview(mitreeview)

    """def modificar(self, titulo, descripcion, mitreeview):
        item_seleccionado = mitreeview.focus()
        valor_id = mitreeview.item(item_seleccionado)
        con = self.conexion()

        cursor = con.cursor()
        sql = "UPDATE noticias SET (titulo, descripcion)=(?,?) WHERE id=?"
        datos = (titulo.get(), descripcion.get(), valor_id["text"])
        cursor.execute(sql, datos)
        con.commit()
        print(sql, datos)

        self.actualizar_treeview(mitreeview)"""
