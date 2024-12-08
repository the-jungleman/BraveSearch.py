from ConsumeAPI import ConsumeAPI
import tkinter as tk
from tkinter import ttk, messagebox
from tkinterweb import HtmlFrame
import requests
import json

class TelaAPI:
    def __init__(self, tela):
        self.tela = tela  # Recebe a instância de Tela
        self.data_list = []  # Lista para armazenar os resultados

    def search(self):
        search = self.tela.query_entry.get()

        # Limpa widgets antigos
        for widget in self.tela.results_frame.winfo_children():
            widget.destroy()

        self.tela.results_frame.pack_forget()
        self.tela.html_frame.pack_forget()

        api = ConsumeAPI()
        data = api.consume_api(search)

        if data and 'web' in data:
            for result in data['web']['results']:
                self.insert_button(result)
            self.tela.results_frame.pack(pady=10)
        else:
            messagebox.showerror("Error", "Nenhum resultado encontrado")

    def insert_button(self, result):
        try:
            title = result['title']
            url = result['url']

            button = tk.Button(self.tela.results_frame, text=title, command=lambda: self.open_url(url))
            button.pack(fill='x', pady=5)

            self.data_list.append({'title': title, 'url': url})
        except KeyError as e:
            print(f"Chave {e} não encontrada")

    def open_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
                self.tela.html_frame.load_html(html_content)
                self.tela.results_frame.pack_forget()
                self.tela.html_frame.pack(pady=10)
            else:
                messagebox.showerror("Erro", f"Falha ao carregar a página: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao acessar a página: {e}")

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
