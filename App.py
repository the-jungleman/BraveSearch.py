import tkinter as tk
from Tela import Tela   

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.main_tela = Tela(self.root)
        self.root.mainloop()
        self.root.geometry("600x400")

    def show_main(self):
        self.main_tela = Tela(self.root)
