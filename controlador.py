from tkinter import Tk
import vista

class Controller:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = vista.Bill_App(self.root_controler)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)
    try:
        application.objeto_vista.actualizar()
    except:
        print("Aún no existe estructura")
    root_tk.mainloop()