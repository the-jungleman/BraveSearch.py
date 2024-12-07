import tkinter as tk
from tkinter import ttk, messagebox
import json,requests
from tkhtmlview import HtmlFrame
from ConsumeAPI import ConsumeAPI

class Tela:
    def __init__(self, root):
        self.root = root
        self.root.title("BraveSearch.py")
        self.root.geometry("800x600")  # Ajuste do tamanho da janela

        self.query_label = tk.Label(self.root, text="Pesquisar")
        self.query_label.pack(pady=5)

        # Caixa de pesquisa
        self.query_entry = tk.Entry(self.root, width=40)
        self.query_entry.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Buscar", command=self.command_search_button)
        self.search_button.pack(pady=10)

        # Frame para armazenar os botões de resultados
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=10)

        # Frame para exibir o conteúdo HTML da página
        self.html_frame = HtmlFrame(self.root, width=750, height=400)
        self.html_frame.pack(pady=10)

        self.data_list = []

    def search(self):
        search = self.query_entry.get()

        # Limpa os resultados anteriores
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        api = ConsumeAPI()
        data = api.consume_api(search)

        if data and 'web' in data:
            for result in data['web']['results']:
                self.insert_button(result)
        else:
            messagebox.showerror("Error", "Nenhum resultado encontrado")

    def insert_button(self, result):
        try:
            title = result['title']
            url = result['url']

            # Criando o botão com o título
            button = tk.Button(self.results_frame, text=title, command=lambda: self.open_url(url))
            button.pack(fill='x', pady=5)

            # Armazenando os dados na lista
            self.data_list.append({'title': title, 'url': url})

        except KeyError as e:
            print(f"Chave {e} não encontrada")

    def open_url(self, url):
        # Fazendo a requisição da página para obter o conteúdo
        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
                self.html_frame.set_content(html_content)  # Exibe o conteúdo HTML no Tkinter
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
