from src.ConsumeAPI import ConsumeAPI
from    src.Browser import  Browser
import tkinter as tk
from tkinter import ttk, messagebox
from tkinterweb import HtmlFrame
import json

class TelaAPI:
    def __init__(self, tela):
        self.data_list = []
        self.tela = tela
        self.browser = Browser()
    
    def open_url(self, url):
        self.browser.open_url(url, self.tela)

    def search(self):
        search = self.tela.query_entry.get()

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

            self.tela.data_list.append({'title': title, 'url': url})
            print(f"Dado inserido: {title} - {url}") 
            
            button = tk.Button(
                self.tela.results_frame,
                text=title,
                command=lambda: self.browser.open_url(self.tela, url)
            )
            button.pack(fill='x', pady=5)

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
        filename = "searchresults.json"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(self.tela.data_list, file, ensure_ascii=False, indent=4)
            print(f"Dados exportados para {filename}")
        except Exception as e:
            print(f"Erro ao exportar dados: {e}")

    def command_search_button(self):
        self.search()
        self.export_to_json()
