import os
import tkinter as tk
from tkinter import filedialog

def merge_files(folder_path, output_folder):
    # Criar a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obter a lista de arquivos na pasta
    files_list = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    merged_content = ""

    # Para cada arquivo na lista
    for file_name in files_list:
        file_path = os.path.join(folder_path, file_name)
        # Verificar se é um arquivo HTML, JavaScript ou CSS
        if file_path.endswith('.html') or file_path.endswith('.js') or file_path.endswith('.css'):
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

    print("Arquivos foram mesclados com sucesso.")

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

# Iniciar o loop da interface gráfica
root.mainloop()
