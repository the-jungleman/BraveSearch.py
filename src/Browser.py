import os
from urllib.parse import urljoin
import requests
from tkinter import messagebox

class Browser:
    def __init__(self):
        pass

    def open_url(self, tela, url):
        if not url.startswith(("http://", "https://", "file://")):
            base_url = tela.current_url if hasattr(tela, "current_url") else ""
            url = urljoin(base_url, url)

        if url.startswith("file://"):
            try:
                file_path = url[7:]

                if not os.path.isabs(file_path):
                    base_path = os.getcwd()  
                    file_path = os.path.join(base_path, file_path)

                if os.path.exists(file_path):
                    with open(file_path, "r", encoding="utf-8") as file:
                        html_content = file.read()
                        tela.html_frame.load_html(html_content)
                        tela.results_frame.pack_forget()
                        tela.html_frame.pack(pady=10)  
                else:
                    messagebox.showerror("Erro", f"Arquivo não encontrado: {file_path}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao acessar o arquivo: {e}")
            return
        
        if url.startswith(("http://", "https://")):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    html_content = response.text
                    tela.html_frame.load_html(html_content)
                    tela.results_frame.pack_forget()  
                    tela.html_frame.pack(pady=10)  
                    
                    tela.current_url = url

                    tela.html_frame.on_link_click(lambda link: self.open_url(tela, link))
                else:
                    messagebox.showerror("Erro", f"Falha ao carregar a página: {response.status_code}")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Erro", f"Erro ao acessar a página: {e}")
