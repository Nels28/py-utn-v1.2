from tkinter import Tk
from vista import MainWindow


class Controller:
    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = MainWindow(self.root_controler)


if __name__ == "__main__":
    root = Tk()
    application = Controller(root)
    root.mainloop()
