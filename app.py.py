import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        incluir_numeros = var_numeros.get()
        incluir_simbolos = var_simbolos.get()

        caracteres = string.ascii_letters  # Letras maiúsculas e minúsculas
        if incluir_numeros:
            caracteres += string.digits  # Adiciona números
        if incluir_simbolos:
            caracteres += string.punctuation  # Adiciona símbolos

        if tamanho < 1:
            raise ValueError("O tamanho deve ser pelo menos 1.")

        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Tamanho da senha
ttk.Label(janela, text="Comprimento da senha:").grid(column=0, row=0, padx=10, pady=5, sticky="w")
entry_tamanho = ttk.Entry(janela, width=10)
entry_tamanho.grid(column=1, row=0, padx=10, pady=5)

# Checkbox para incluir números
var_numeros = tk.BooleanVar(value=True)
check_numeros = ttk.Checkbutton(janela, text="Incluir números", variable=var_numeros)
check_numeros.grid(column=0, row=1, padx=10, pady=5, sticky="w")

# Checkbox para incluir símbolos
var_simbolos = tk.BooleanVar(value=True)
check_simbolos = ttk.Checkbutton(janela, text="Incluir símbolos", variable=var_simbolos)
check_simbolos.grid(column=0, row=2, padx=10, pady=5, sticky="w")

# Botão para gerar senha
btn_gerar = ttk.Button(janela, text="Gerar Senha", command=gerar_senha)
btn_gerar.grid(column=0, row=3, columnspan=2, pady=10)

# Campo para exibir a senha gerada
ttk.Label(janela, text="Senha gerada:").grid(column=0, row=4, padx=10, pady=5, sticky="w")
entry_senha = ttk.Entry(janela, width=30)
entry_senha.grid(column=0, row=5, columnspan=2, padx=10, pady=5)

# Iniciar a interface
janela.mainloop()
