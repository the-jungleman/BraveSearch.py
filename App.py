import tkinter as tk
from Tela import Tela   

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.show_main()
        self.root.mainloop()

    def show_main(self):
        self.main_tela = Tela(self.root)
