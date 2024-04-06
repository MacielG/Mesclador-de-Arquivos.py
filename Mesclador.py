import os
import tkinter as tk
from tkinter import filedialog
import pyperclip  # Importar a biblioteca pyperclip para manipular a área de transferência

def merge_files(folder_path, output_folder):
    # Criar a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    merged_content = ""

    # Percorrer recursivamente todas as pastas e arquivos
    for root_folder, subfolders, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root_folder, file_name)
            # Verificar se é um arquivo com extensão .py, .html, .css ou .js
            if file_path.endswith('.py') or file_path.endswith('.html') or file_path.endswith('.css') or file_path.endswith('.js'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Adicionar o nome do arquivo como prefixo
                    merged_content += f"== {file_name} ==\n\n"
                    # Adicionar conteúdo do arquivo
                    merged_content += content
                    # Adicionar espaço em branco entre os arquivos
                    merged_content += "\n\n"

    # Criar o nome do arquivo mesclado
    output_file_name = "merged_file.txt"
    output_file_path = os.path.join(output_folder, output_file_name)
    # Escrever o conteúdo mesclado no arquivo de saída
    with open(output_file_path, 'w', encoding='utf-8') as merged_file:
        merged_file.write(merged_content)

    # Copiar o conteúdo mesclado para a área de transferência
    pyperclip.copy(merged_content)

    print("Arquivos foram mesclados com sucesso e copiados para a área de transferência.")
    # Atualizar a mensagem na interface gráfica
    status_label.config(text="Conteúdo copiado para a área de transferência", fg="red")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        merge_files(folder_path, output_folder_entry.get())

# Criar a janela principal
root = tk.Tk()
root.title("Mesclar Arquivos")

# Criar e posicionar elementos na janela
select_folder_button = tk.Button(root, text="Selecionar Pasta", command=select_folder)
select_folder_button.pack(pady=10)

output_folder_label = tk.Label(root, text="Digite o nome da pasta de saída:")
output_folder_label.pack()

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.insert(0, os.path.join(os.path.expanduser('~'), 'Desktop', 'Arquivos_Mesclados'))
output_folder_entry.pack(pady=5)

# Label para exibir o status da operação
status_label = tk.Label(root, text="", fg="red")
status_label.pack()

# Iniciar o loop da interface gráfica
root.mainloop()
