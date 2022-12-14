import sqlite3
import re
import os
import random
from tkinter import messagebox
from tkinter import END


# ==================Area base de datos===========
db_name = "dbapp.db"
# ======================Base de Datos=======================
def run_query(self, query, param=()):
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, param)
        conn.commit()
    return result

    # ===========================Validación de campo y agregar cliente nuevo==================


def add_clientes(self):
    patron = "^[a-zA-Z0-9]"
    cadena1 = self.c_name_nuevo.get()
    if re.match(patron, cadena1):
        query = "INSERT INTO clientes VALUES(NULL, ?, ?)"
        param = (self.c_name_nuevo.get(), self.c_tel_nuevo.get())
        self.run_query(query, param)
        messagebox.showinfo("Guardado", "Cliente agregado con éxito")

    else:
        messagebox.showinfo("Error", "Ingrese caracteres validos")


# ====================Limpiar formulario=========================================
def clear_clientes(self):
    op = messagebox.askyesno(
        "Limpiar datos", "Esta seguro que desea limpiar los datos?"
    )
    if op > 0:
        self.c_name_nuevo.set("")
        self.c_tel_nuevo.set("")


# ================total_factura==========================
def total(self):
    self.g_r_p = self.arroz.get() * 30
    self.g_f_o_p = self.aceite.get() * 20
    self.g_w_p = self.harina.get() * 30
    self.g_d_p = self.pan.get() * 10
    self.g_f_p = self.pasta.get() * 15
    self.g_m_p = self.carne.get() * 200
    self.total_mercado = float(
        self.g_r_p + self.g_f_o_p + self.g_w_p + self.g_d_p + self.g_f_p + self.g_m_p
    )

    self.mercado.set("Ars. " + str(self.total_mercado))
    self.g_tax = round((self.total_mercado * 0.21), 2)
    self.grocery_tax.set("Ars. " + str(self.g_tax))

    self.c_d_s_p = self.sprite.get() * 30
    self.c_d_l_p = self.fernet.get() * 100
    self.c_d_m_p = self.vino.get() * 200
    self.c_d_c_p = self.coca.get() * 40
    self.c_d_f_p = self.fanta.get() * 40
    self.c_m_d = self.agua.get() * 20
    self.total_bebidas = float(
        self.c_d_s_p
        + self.c_d_l_p
        + self.c_d_m_p
        + self.c_d_c_p
        + self.c_d_f_p
        + self.c_m_d
    )

    self.bebidas.set("Ars. " + str(self.total_bebidas))
    self.c_d_tax = round((self.total_bebidas * 0.21), 2)
    self.cold_drinks_tax.set("Ars. " + str(self.c_d_tax))

    self.total_bill = float(
        self.total_mercado + self.total_bebidas + self.g_tax + self.c_d_tax
    )


# ==============bienvenido_factura==============================
def welcome_bill(self):
    self.txtarea.delete("1.0", END)
    self.txtarea.insert(END, "\tBienvenidos")
    self.txtarea.insert(END, f"\n Numero de Factura:{self.bill_no.get()}")
    self.txtarea.insert(END, f"\nNombre del Cliente:{self.c_name.get()}")
    self.txtarea.insert(END, f"\nNumero de telefono{self.c_phone.get()}")
    self.txtarea.insert(END, f"\n================================")
    self.txtarea.insert(END, f"\nProductos\t\tQTY\t\tPrecio")


# =========area_factura=================================================
def bill_area(self):
    if self.c_name.get() == " " or self.c_phone.get() == " ":
        messagebox.showerror("Error", "Datos del cliente son requeridos")
    elif self.mercado.get() == "Ars. 0.0" and self.bebidas.get() == "Ars. 0.0":
        messagebox.showerror("Error", "No se ha comprado nada")
    else:
        self.welcome_bill()
    # ==============comida============================
    if self.arroz.get() != 0:
        self.txtarea.insert(END, f"\n Arroz\t\t{self.arroz.get()}\t\t{self.g_r_p}")
    if self.aceite.get() != 0:
        self.txtarea.insert(END, f"\n Aceite\t\t{self.aceite.get()}\t\t{self.g_f_o_p}")
    if self.harina.get() != 0:
        self.txtarea.insert(END, f"\n Harina\t\t{self.harina.get()}\t\t{self.g_w_p}")
    if self.pan.get() != 0:
        self.txtarea.insert(END, f"\n Pan\t\t{self.pan.get()}\t\t{self.g_d_p}")
    if self.pasta.get() != 0:
        self.txtarea.insert(END, f"\n Pasta\t\t{self.pasta.get()}\t\t{self.g_f_p}")
    if self.carne.get() != 0:
        self.txtarea.insert(END, f"\n Carne\t\t{self.carne.get()}\t\t{self.g_m_p}")
    # ================bebidas==========================
    if self.sprite.get() != 0:
        self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
    if self.fernet.get() != 0:
        self.txtarea.insert(
            END, f"\n Sanitizer\t\t{self.fernet.get()}\t\t{self.c_d_l_p}"
        )
    if self.vino.get() != 0:
        self.txtarea.insert(END, f"\n Vino\t\t{self.vino.get()}\t\t{self.c_d_m_p}")
    if self.coca.get() != 0:
        self.txtarea.insert(END, f"\n Coca\t\t{self.coca.get()}\t\t{self.c_d_c_p}")
    if self.fanta.get() != 0:
        self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.c_d_f_p}")
    if self.agua.get() != 0:
        self.txtarea.insert(END, f"\n Agua\t\t{self.agua.get()}\t\t{self.c_m_d}")
        self.txtarea.insert(END, f"\n--------------------------------")
    # ===============taxes==============================
    if self.grocery_tax.get() != "0.0":
        self.txtarea.insert(END, f"\n IVA Comida\t\t\t{self.grocery_tax.get()}")
    if self.cold_drinks_tax.get() != "0.0":
        self.txtarea.insert(END, f"\n IVA Bebidas\t\t\t{self.cold_drinks_tax.get()}")

    self.txtarea.insert(END, f"\n Total:\t\t\t Ars.{self.total_bill}")
    self.txtarea.insert(END, f"\n--------------------------------")
    self.save_bill()


# =========guardar_factura============================
def save_bill(self):
    op = messagebox.askyesno("Guardar Factura", "Desea guardar la factura?")
    if op > 0:
        self.bill_data = self.txtarea.get("1.0", END)
        f1 = open(
            "/Users/nel/Documents/PythonUTN/facturas/"
            + str(self.bill_no.get())
            + ".txt",
            "w",
        )
        f1.write(self.bill_data)
        f1.close()
        messagebox.showinfo(
            "Saved", f"Factura Numero:{self.bill_no.get()} Guardada exitosamente"
        )
    else:
        return


# ===================encontrar_factura================================
def find_bill(self):
    present = "no"
    for i in os.listdir("/Users/nel/Documents/PythonUTN/facturas/"):
        if i.split(".")[0] == self.search_bill.get():
            f1 = open(f"facturas/{i}", "r")
            self.txtarea.delete("1.0", END)
            for d in f1:
                self.txtarea.insert(END, d)
                f1.close()
            present = "yes"
    if present == "no":
        messagebox.showerror("Error", "Numero de factura invalido")


# ======================borrar_datos======================
def clear_data(self):
    op = messagebox.askyesno(
        "Limpiar datos", "Esta seguro que desea limpiar los datos?"
    )
    if op > 0:
        # ============comida==============================
        self.arroz.set(0)
        self.aceite.set(0)
        self.harina.set(0)
        self.pan.set(0)
        self.pasta.set(0)
        self.carne.set(0)
        # =============bebidas=============================
        self.sprite.set(0)
        self.fernet.set(0)
        self.vino.set(0)
        self.coca.set(0)
        self.fanta.set(0)
        self.agua.set(0)
        # ====================taxes================================
        self.mercado.set("")
        self.bebidas.set("")

        self.grocery_tax.set("")
        self.cold_drinks_tax.set("")

        self.c_name.set("")
        self.c_phone.set("")

        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill.set("")
        self.welcome_bill()


# ===========Salir=======================
def exit_app(self):
    op = messagebox.askyesno("Salir", "Esta seguro que desea salir?")
    if op > 0:
        self.root.destroy()
