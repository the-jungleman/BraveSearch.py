import tkinter as tk
from tkinter import ttk, messagebox
from tkinterweb import HtmlFrame
from TelaAPI import TelaAPI

class Tela:
    def __init__(self, root):
        self.root = root
        self.telaapi=TelaAPI(self)
        self.root.title("BraveSearch.py")
        self.root.geometry("1368x768")

        self.query_label = tk.Label(self.root, text="Pesquisar")
        self.query_label.pack(pady=5)

        self.query_entry = tk.Entry(self.root, width=40)
        self.query_entry.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Buscar", command=self.telaapi.command_search_button)
        self.search_button.pack(pady=10)

        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=10)

        self.html_frame = HtmlFrame(self.root, width=750, height=400)
        self.html_frame.pack(pady=10)

        self.data_list = []

        self.tela_api = TelaAPI(self)

    def search(self):
        query = self.query_entry.get()
        self.tela_api.search(query)