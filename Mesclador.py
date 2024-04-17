import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import pyperclip

def merge_files(selected_files):
    merged_content = ""
    try:
        for file_path in selected_files:
            with open(file_path, 'r') as file:
                merged_content += file.read() + "\n"
        pyperclip.copy(merged_content)
        messagebox.showinfo("Sucesso", "Conteúdo mesclado e copiado para a área de transferência!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def select_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    root = tk.Toplevel()
    root.title('Selecionar Arquivos para Mesclar')

    tree = ttk.Treeview(root, selectmode='extended')
    ysb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    xsb = ttk.Scrollbar(root, orient='horizontal', command=tree.xview)
    tree.configure(yscroll=ysb.set, xscroll=xsb.set)
    tree.heading('#0', text='Arquivos', anchor='w')

    def insert_files(path, parent=''):
        for p in sorted(os.listdir(path)):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = tree.insert(parent, 'end', text=p, open=False)
            if isdir:
                insert_files(abspath, oid)

    insert_files(folder_path)
    tree.pack(fill='both', expand=True)
    ysb.pack(fill='y', side='right')
    xsb.pack(fill='x', side='bottom')

    def on_merge_selected():
        selected_files = [
            os.path.join(folder_path, tree.item(item)["text"]) for item in tree.selection()
            if not os.path.isdir(os.path.join(folder_path, tree.item(item)["text"]))
        ]
        merge_files(selected_files)
        root.destroy()

    def toggle_item_selection(event):
        item = tree.identify('item', event.x, event.y)
        if tree.tag_has('selected', item):
            tree.item(item, tags=())
            tree.selection_remove(item)
        else:
            tree.item(item, tags=('selected',))
            tree.selection_add(item)
            tree.tag_configure('selected', background='yellow')

    tree.bind('<1>', toggle_item_selection)

    merge_btn = ttk.Button(root, text="Mesclar Selecionados", command=on_merge_selected)
    merge_btn.pack(fill='x', expand=True)

    root.mainloop()

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Mesclador de Arquivos")
    app.geometry("300x250")

    open_btn = ttk.Button(app, text="Selecionar Pasta", command=select_files)
    open_btn.pack(expand=True)

    app.mainloop()
