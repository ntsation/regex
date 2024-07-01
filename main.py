import tkinter as tk
from tkinter import messagebox
import re


def obter_padrao(tipo):
    expressoes = {
        "Dígito": r'^\d+$',
        "Decimal": r'^[+-]?((\d+|\d{1,3}(\.\d{3})+)(\,\d*)?|\,\d+)$|^[-+]?([0-9]*\,[0-9]+|[0-9]+)$',
        "Letra": r'^[[:alpha:]]+$',
        "URL": r'^((http)|(https)|(ftp)):\/\/([\- \w]+\.)+\w{2,3}(\/ [%\-\w]+(\.\w{2,})?)*$',
        "E-mail": r'^([\w\-]+\.)*[\w\- ]+@([\w\- ]+\.)+([\w\-]{2,3})$',
        "Endereço IP": r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        "Tempo (24 horas)": r'^([0|1|2]{1}\d):([0|1|2|3|4|5]{1} \d)$',
        "Data (dd/mm/aaaa)": r'^((0[1-9]|[12]\d)\/(0[1-9]|1[0-2])|30\/(0[13-9]|1[0-2])|31\/(0[13578]|1[02])) \/\d{4}$',
        "Telefone": r'^\(\d{3}\)-\d{4}-\d{4}$',
        "Senha": r'^\w{4,10}$|^[a-zA-Z]\w{3,9}$|^[a-zA-Z]\w*\d+\w*$'
    }
    return expressoes.get(tipo, "Tipo não reconhecido")


def validar_entrada():
    tipo = tipo_var.get()
    entrada = entrada_entry.get()

    padrao = obter_padrao(tipo)

    if padrao == "Tipo não reconhecido":
        messagebox.showerror("Erro", f"Tipo '{tipo}' não reconhecido.")
    elif re.match(padrao, entrada):
        messagebox.showinfo("Validação", f"A entrada '{
                            entrada}' é válida para o tipo '{tipo}'.")
    else:
        messagebox.showerror("Validação", f"A entrada '{
                             entrada}' não é válida para o tipo '{tipo}'.")


def atualizar_padrao(*args):
    tipo = tipo_var.get()
    padrao = obter_padrao(tipo)
    padrao_entry.delete(0, tk.END)
    padrao_entry.insert(0, padrao)


# Criando a janela principal
root = tk.Tk()
root.title("Validador de Entrada")

# Criando os widgets
root.grid_columnconfigure(1, weight=1)

tipo_label = tk.Label(root, text="Tipo de Validação:")
tipo_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

tipos_validacao = [
    "Dígito",
    "Decimal",
    "Letra",
    "URL",
    "E-mail",
    "Endereço IP",
    "Tempo (24 horas)",
    "Data (dd/mm/aaaa)",
    "Telefone",
    "Senha"
]
tipo_var = tk.StringVar(root)
tipo_var.set(tipos_validacao[0])
tipo_var.trace("w", atualizar_padrao)
tipo_option = tk.OptionMenu(root, tipo_var, *tipos_validacao)
tipo_option.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

padrao_label = tk.Label(root, text="Expressão Regular:")
padrao_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
padrao_entry = tk.Entry(root)
padrao_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

entrada_label = tk.Label(root, text="Entrada:")
entrada_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_entry = tk.Entry(root)
entrada_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

validar_button = tk.Button(root, text="Validar", command=validar_entrada)
validar_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Iniciando o loop da interface
root.mainloop()
