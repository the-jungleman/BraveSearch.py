import tkinter as tk
from tkinter import ttk, messagebox
import json
from ConsumeAPI import ConsumeAPI

class Tela:
    def __init__(self, root):
        self.root = root
        self.root.title("BraveSearch.py")

        self.query_label = tk.Label(self.root, text="Pesquisar")
        self.query_label.pack(pady=5)
        self.query_entry = tk.Entry(self.root)
        self.query_entry.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Buscar", command=self.command_search_button)
        self.search_button.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=('title',), show='headings')
        self.tree.heading('title', text='Resultados')
        self.tree.pack(pady=40)
        self.data_list = []

    def search(self):
        search = self.query_entry.get()

        api = ConsumeAPI()
        data = api.consume_api(search)

        if data and 'web' in data:
            for result in data['web']['results']:
                self.insert_data(result['title'])
        else:
            messagebox.showerror("Error", "Nenhum resultado encontrado")

    def insert_data(self, title_result):
        try:
            self.tree.insert('', 'end', values=(title_result,))
            self.data_list.append({'title': title_result})
        except KeyError as e:
            print(f"Chave {e} não encontrada")

    def export_to_json(self):
        if not self.data_list:
            messagebox.showerror("Erro", "Nenhum dado disponível para exportar.")
            return

        filename = "searchresults.json"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.data_list, file, ensure_ascii=False, indent=4)
            messagebox.showinfo("Sucesso", f"Dados exportados para {filename}")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível exportar os dados: {e}")

    def command_search_button(self):
        self.search()
        self.export_to_json()
