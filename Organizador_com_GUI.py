import os
import shutil
import tkinter as tk
from tkinter import filedialog


def organizador_de_arquivos():
    caminho = filedialog.askdirectory(title="Selecione o diretório")
    if caminho:
        arquivos = os.listdir(caminho)
        for arquivo in arquivos:
            arquivonome, extensao = os.path.splitext(arquivo)
            extensao = extensao.replace(".xlsx", ".Excel") if extensao == ".xlsx" else extensao
            extensao = extensao[1:]
            if os.path.exists(os.path.join(caminho, extensao)):
                shutil.move(os.path.join(caminho, arquivo), os.path.join(caminho, extensao, arquivo))
            else:
                os.makedirs(os.path.join(caminho, extensao))
                shutil.move(os.path.join(caminho, arquivo), os.path.join(caminho, extensao))


# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Organizador de Arquivos")

# Cria a etiqueta na tela,pack posiciona com 10 px de espaço vertical entre as partes inferior e superior
etiqueta = tk.Label(janela, text="Clique no botão para organizar os arquivos por extensão:")
etiqueta.pack(pady=10)

# cria o botao organizar que chama a função organizador_de_arquivos quando for acionado,pack posiciona de forma padrão
botao_organizar = tk.Button(janela, text="Organizar Arquivos", command=organizador_de_arquivos)
botao_organizar.pack()

# cria um looping pra manter a janela aberta
janela.mainloop()
