import requests
from tkinter import messagebox

class Browser:
    def __init__(self):
        pass

    def open_url(self, tela, url):
        """
        Carrega uma página HTML dentro do HtmlFrame da instância de Tela.
        """
        if not url.startswith("http://") and not url.startswith("https://"):
            messagebox.showerror("Erro", f"URL inválida: {url}")
            return

        try:
            response = requests.get(url)
            if response.status_code == 200:
                html_content = response.text
                tela.html_frame.load_html(html_content)  # Carrega o conteúdo no HtmlFrame
                tela.results_frame.pack_forget()  # Esconde o frame de resultados
                tela.html_frame.pack(pady=10)  # Mostra o HtmlFrame
            else:
                messagebox.showerror("Erro", f"Falha ao carregar a página: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao acessar a página: {e}")
