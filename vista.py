from tkinter import ttk
from tkinter import Label
from tkinter import RIDGE
from tkinter import IntVar
from tkinter import StringVar
from tkinter import LabelFrame
from tkinter import Entry
from tkinter import FLAT
from tkinter import Button
from tkinter import RAISED
from tkinter import Scrollbar
from tkinter import VERTICAL
from tkinter import Text
from tkinter import RIGHT
from tkinter import BOTH
from tkinter import Frame
from tkinter import GROOVE
import random


def vista_principal(root):
    # ============main vista============================
    class Bill_App:
        def __init__(self, root):
            self.root = root
            self.root.geometry("1300x716+0+0")
            self.root.title("Sistema de Facturación")
            bg_color = "#7A92B8"
            title = Label(
                self.root,
                text="Sistema de Facturación",
                font=("times new roman", 30),
                pady=2,
                bd=0,
                bg="#0B1320",
                fg="white",
                relief=RIDGE,
            )
            title.pack(fill="x")
            # ============comidas==============================
            self.arroz = IntVar()
            self.aceite = IntVar()
            self.harina = IntVar()
            self.pan = IntVar()
            self.pasta = IntVar()
            self.carne = IntVar()
            # =============bebidas=============================
            self.sprite = IntVar()
            self.fernet = IntVar()
            self.vino = IntVar()
            self.coca = IntVar()
            self.fanta = IntVar()
            self.agua = IntVar()
            # ==============precio_total_productos================
            self.mercado = StringVar()
            self.bebidas = StringVar()
            # ==============Cliente==========================
            self.c_name = StringVar()
            self.c_phone = StringVar()
            self.bill_no = StringVar()
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill = StringVar()
            self.find_bill = StringVar()

            # ===============Alta Cliente Nuevo================================
            self.c_name_nuevo = StringVar()
            self.c_tel_nuevo = StringVar()

            # ===============Tax================================
            self.grocery_tax = StringVar()
            self.cold_drinks_tax = StringVar()
            # =============Informacion_cliente======================
            F1 = LabelFrame(
                self.root,
                text="Información del Cliente",
                font=("times new roman", 15, "bold"),
                bd=1,
                fg="White",
                bg="#1C3F60",
                width=20,
            )
            F1.place(x=0, y=51, relwidth=1)
            cname_lbl = Label(
                F1,
                text="Nombre del cliente:",
                bg="#1C3F60",
                fg="White",
                font=("times new roman", 15, "bold"),
            )
            cname_lbl.grid(row=0, column=0, padx=20, pady=5)
            cname_txt = Entry(
                F1,
                width=15,
                textvariable=self.c_name,
                font="arial 15",
                bd=7,
                relief=FLAT,
            )
            cname_txt.grid(row=0, column=1, pady=5, padx=10)

            cphn_lbl = Label(
                F1,
                text="Teléfono:",
                bg="#1C3F60",
                fg="white",
                font=("times new roman", 15, "bold"),
            )
            cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
            cphn_txt = Entry(
                F1,
                width=15,
                textvariable=self.c_phone,
                font="arial 15",
                bd=7,
                relief=FLAT,
            )
            cphn_txt.grid(row=0, column=3, pady=5, padx=10)

            c_bill_lbl = Label(
                F1,
                text="N° de cliente:",
                bg="#1C3F60",
                fg="white",
                font=("times new roman", 15, "bold"),
            )
            c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
            c_bill_txt = Entry(
                F1,
                width=15,
                textvariable=self.search_bill,
                font="arial 15",
                bd=7,
                relief=FLAT,
            )
            c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

            bil_btn = Button(
                F1,
                text="Buscar",
                command=self.find_bill,
                width=10,
                bd=2,
                font=("arial", 12, "bold"),
                relief=RAISED,
            )
            bil_btn.grid(row=0, column=6, pady=5, padx=10)

            # =============alta de clientes=======================
            # Panel para dar de alta clintes nuevos a la Base de datos

            F2 = LabelFrame(
                self.root,
                text="Alta Clientes Nuevos",
                font=("times new roman", 13, "bold"),
                bd=1,
                fg="Black",
                bg="#D9D9D9",
            )
            F2.place(x=0, y=135, relwidth=1)
            c_name_nuevo_lbl = Label(
                F2,
                text="Nombre Completo:",
                bg="#D9D9D9",
                font=("times new roman", 15, "bold"),
            )
            c_name_nuevo_lbl.grid(row=1, column=0, padx=20, pady=5)
            c_name_nuevo_txt = Entry(
                F2,
                width=15,
                textvariable=self.c_name_nuevo,
                font="arial 15",
                bd=1,
                relief=RIDGE,
            )
            c_name_nuevo_txt.grid(row=1, column=1, pady=5, padx=10)

            c_tel_nuevo_lbl = Label(
                F2, text="Teléfono:", bg="#D9D9D9", font=("times new roman", 15, "bold")
            )
            c_tel_nuevo_lbl.grid(row=1, column=2, padx=20, pady=5)
            c_tel_nuevo_txt = Entry(
                F2,
                width=15,
                textvariable=self.c_tel_nuevo,
                font="arial 15",
                bd=1,
                relief=RIDGE,
            )
            c_tel_nuevo_txt.grid(row=1, column=3, pady=5, padx=10)

            bil_btn = Button(
                F2,
                text="Guardar",
                command=self.add_clientes,
                width=10,
                bg="#AFC1D0",
                bd=2,
                font=("times new roman", 12, "bold"),
                relief=RAISED,
            )
            bil_btn.grid(row=1, column=4, padx=20, pady=5)

            limp_datos = Button(
                F2,
                text="Borrar",
                command=self.clear_clientes,
                width=10,
                bg="#E86666",
                bd=2,
                font=("times new roman", 12, "bold"),
                relief=RAISED,
            )
            limp_datos.grid(row=1, column=5, padx=20, pady=5)

            # ==========productos_comida=========================
            F3 = LabelFrame(
                self.root,
                text="Productos del Supermercado",
                font=("times new roman", 15, "bold"),
                bd=5,
                fg="Black",
                bg="#AFC1D0",
            )
            F3.place(x=5, y=205, width=400, height=380)

            arroz_lbl = Label(
                F3,
                text="Arroz",
                font=("arial", 16),
                bg="#AFC1D0",
                fg="black",
            )
            arroz_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="W")
            arroz_txt = Entry(
                F3,
                width=10,
                textvariable=self.arroz,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            arroz_txt.grid(row=0, column=1, padx=10, pady=10)

            aceite_lbl = Label(
                F3,
                text="Aceite",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            aceite_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")
            aceite_txt = Entry(
                F3,
                width=10,
                textvariable=self.aceite,
                font=("times new roman", 16, "bold"),
                bd=1,
                relief=RIDGE,
            )
            aceite_txt.grid(row=1, column=1, padx=10, pady=10)

            harina_lbl = Label(
                F3,
                text="Harina",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            harina_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")
            harina_txt = Entry(
                F3,
                width=10,
                textvariable=self.harina,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            harina_txt.grid(row=2, column=1, padx=10, pady=10)

            pan_lbl = Label(
                F3,
                text="Pan",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            pan_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="W")
            pan_txt = Entry(
                F3,
                width=10,
                textvariable=self.pan,
                font=("times new roman", 16, "bold"),
                bd=1,
                relief=RIDGE,
            )
            pan_txt.grid(row=3, column=1, padx=10, pady=10)

            pasta_lbl = Label(
                F3,
                text="Pasta",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            pasta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="W")
            pasta_txt = Entry(
                F3,
                width=10,
                textvariable=self.pasta,
                font=("times new roman", 16, "bold"),
                bd=1,
                relief=RIDGE,
            )
            pasta_txt.grid(row=4, column=1, padx=10, pady=10)

            carne_lbl = Label(
                F3,
                text="Carne",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            carne_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="W")
            carne_txt = Entry(
                F3,
                width=10,
                textvariable=self.carne,
                font=("times new roman", 16, "bold"),
                bd=1,
                relief=RIDGE,
            )
            carne_txt.grid(row=5, column=1, padx=10, pady=10)

            # ===========Bebidas================================
            F4 = LabelFrame(
                self.root,
                text="Bebidas",
                font=("times new roman", 15, "bold"),
                bd=5,
                fg="Black",
                bg="#AFC1D0",
            )
            F4.place(x=400, y=205, width=435, height=380)

            sprite_lbl = Label(
                F4,
                text="Sprite",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="W")
            sprite_txt = Entry(
                F4,
                width=10,
                textvariable=self.sprite,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            sprite_txt.grid(row=0, column=1, padx=10, pady=10)

            fernet_lbl = Label(
                F4,
                text="Fernet",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            fernet_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="W")
            fernet_txt = Entry(
                F4,
                width=10,
                textvariable=self.fernet,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            fernet_txt.grid(row=1, column=1, padx=10, pady=10)

            vino_lbl = Label(
                F4,
                text="Vino",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            vino_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="W")
            harina_txt = Entry(
                F4,
                width=10,
                textvariable=self.vino,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            harina_txt.grid(row=2, column=1, padx=10, pady=10)

            coca_lbl = Label(
                F4,
                text="Coca",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            coca_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="W")
            coca_txt = Entry(
                F4,
                width=10,
                textvariable=self.coca,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            coca_txt.grid(row=3, column=1, padx=10, pady=10)

            fanta_lbl = Label(
                F4,
                text="Fanta",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="W")
            fanta_txt = Entry(
                F4,
                width=10,
                textvariable=self.fanta,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            fanta_txt.grid(row=4, column=1, padx=10, pady=10)

            agua_lbl = Label(
                F4,
                text="Agua",
                font=("times new roman", 16),
                bg="#AFC1D0",
                fg="black",
            )
            agua_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="W")
            agua_txt = Entry(
                F4,
                width=10,
                textvariable=self.agua,
                font=("times new roman", 16),
                bd=1,
                relief=RIDGE,
            )
            agua_txt.grid(row=5, column=1, padx=10, pady=10)

            # =================Area_Facturacion======================
            F5 = Frame(self.root, bd=10, relief=GROOVE)
            F5.place(x=825, y=205, width=450, height=380)

            bill_title = Label(
                F5,
                text="Área de Facturación",
                font="arial 15 bold",
                bd=7,
                relief=GROOVE,
            )
            bill_title.pack(fill="x")
            scroll_y = Scrollbar(F5, orient=VERTICAL)
            self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill="y")
            scroll_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH, expand=1)

            # =======================ButtonFrame=============
            F6 = LabelFrame(
                self.root,
                text="Area de Factura",
                font=("times new roman", 14, "bold"),
                bd=2,
                fg="White",
                bg="#1C3F60",
            )
            F6.place(x=0, y=585, relwidth=1, height=130)

            m2_lbl = Label(
                F6,
                text="Total Comida",
                font=("times new roman", 14, "bold"),
                bg="#1C3F60",
                fg="white",
            )
            m2_lbl.grid(row=1, column=0, padx=20, pady=10, sticky="W")
            m2_txt = Entry(
                F6,
                width=18,
                textvariable=self.mercado,
                font="arial 10 bold",
                bd=1,
                relief=RIDGE,
            )
            m2_txt.grid(row=1, column=1, padx=18, pady=1)

            m3_lbl = Label(
                F6,
                text="Total Bebidas",
                font=("times new roman", 14, "bold"),
                bg="#1C3F60",
                fg="white",
            )
            m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky="W")
            m3_txt = Entry(
                F6,
                width=18,
                textvariable=self.bebidas,
                font="arial 10 bold",
                bd=1,
                relief=RIDGE,
            )
            m3_txt.grid(row=2, column=1, padx=18, pady=1)

            m5_lbl = Label(
                F6,
                text="IVA Comida",
                font=("times new roman", 14, "bold"),
                bg="#1C3F60",
                fg="white",
            )
            m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky="W")
            m5_txt = Entry(
                F6,
                width=18,
                textvariable=self.grocery_tax,
                font="arial 10 bold",
                bd=1,
                relief=RIDGE,
            )
            m5_txt.grid(row=1, column=3, padx=18, pady=1)

            m6_lbl = Label(
                F6,
                text="IVA Bebidas",
                font=("times new roman", 14, "bold"),
                bg="#1C3F60",
                fg="white",
            )
            m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky="W")
            m6_txt = Entry(
                F6,
                width=18,
                textvariable=self.cold_drinks_tax,
                font="arial 10 bold",
                bd=1,
                relief=RIDGE,
            )
            m6_txt.grid(row=2, column=3, padx=18, pady=1)

            # =======Buttons-======================================
            btn_f = Frame(F6, bd=7, relief=GROOVE)
            btn_f.place(x=680, width=580, height=90)

            total_btn = Button(
                btn_f,
                command=self.total,
                text="TOTAL",
                bg="#7AB89A",
                bd=2,
                fg="black",
                pady=15,
                width=12,
                font="arial 13 bold",
            )
            total_btn.grid(row=0, column=0, padx=5, pady=5)

            generateBill_btn = Button(
                btn_f,
                command=self.bill_area,
                text="FACTURA",
                bd=2,
                bg="#FFFCA9",
                fg="black",
                pady=15,
                width=12,
                font="arial 13 bold",
            )
            generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

            clear_btn = Button(
                btn_f,
                command=self.clear_data,
                text="BORRAR",
                bg="#E86666",
                bd=2,
                fg="black",
                pady=15,
                width=12,
                font="arial 13 bold",
            )
            clear_btn.grid(row=0, column=2, padx=5, pady=5)

            exit_btn = Button(
                btn_f,
                command=self.exit_app,
                text="SALIR",
                bd=2,
                bg="#AFC1D0",
                fg="black",
                pady=15,
                width=12,
                font="arial 13 bold",
            )
            exit_btn.grid(row=0, column=3, padx=5, pady=5)
            self.welcome_bill()
