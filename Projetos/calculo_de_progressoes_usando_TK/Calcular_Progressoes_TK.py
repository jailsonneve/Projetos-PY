import tkinter as tk
from tkinter import messagebox

# Funções de cálculo
def calc(termosList, n):
    a1, a2 = termosList[0], termosList[1]
    r = a2 - a1
    resp = a1 + r * (n - 1)
    return resp

def soma_pa(termosList, n):
    a1, a2 = termosList[0], termosList[1]
    r = a2 - a1
    soma = (n / 2) * (2 * a1 + (n - 1) * r)
    return soma

def termo_pg(a1, r, n):
    return a1 * (r ** (n - 1))

def soma_pg(a1, r, n):
    if r == 1:
        return n * a1
    else:
        return a1 * (1 - r ** n) / (1 - r)

# Função para exibir resultado na tela
def exibir_resultado(resultado):
    resultado_label.config(text=f"Resultado: {resultado}")

# Função chamada quando o botão "Soma P.A." for clicado
def calcular_soma_pa():
    try:
        n = int(entry_n.get())
        termos = [float(i) for i in entry_termos.get().split()]
        soma = soma_pa(termos, n)
        exibir_resultado(f"A soma dos {n} primeiros termos da progressão aritmética é {soma}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular P.A.: {e}")

# Função chamada quando o botão "Termo P.A." for clicado
def calcular_termo_pa():
    try:
        n = int(entry_n.get())
        termos = [float(i) for i in entry_termos.get().split()]
        termo = calc(termos, n)
        exibir_resultado(f"O {n}º termo da progressão aritmética é {termo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular P.A.: {e}")

# Função chamada quando o botão "Termo P.G." for clicado
def calcular_termo_pg():
    try:
        n = int(entry_n.get())
        termos = [float(i) for i in entry_termos.get().split()]
        a1 = termos[0]
        r = termos[1] / a1  # Razão calculada entre os dois primeiros termos
        termo_n = termo_pg(a1, r, n)
        exibir_resultado(f"O {n}º termo da progressão geométrica é {termo_n}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular P.G.: {e}")

# Função chamada para calcular a soma da P.G.
def calcular_soma_pg():
    try:
        n = int(entry_n.get())
        termos = [float(i) for i in entry_termos.get().split()]
        a1 = termos[0]
        r = termos[1] / a1
        soma = soma_pg(a1, r, n)
        exibir_resultado(f"A soma dos {n} primeiros termos da progressão geométrica é {soma}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular P.G.: {e}")

# Função chamada para limpar os campos de entrada e o resultado
def limpar_campos():
    entry_n.delete(0, tk.END)
    entry_termos.delete(0, tk.END)
    resultado_label.config(text="Resultado:")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Progressões")

# Definindo a largura e altura da janela
root.geometry("600x500")
root.config(bg="#f2f2f2")

# Fonte personalizada
font_bold = ("Arial", 12, "bold")
font_normal = ("Arial", 12)

# Labels e campos de entrada
label_n = tk.Label(root, text="Número de termos (n):", font=font_bold, bg="#f2f2f2")
label_n.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_n = tk.Entry(root, font=font_normal, width=20)
entry_n.grid(row=0, column=1, padx=10, pady=10)

label_termos = tk.Label(root, text="Digite os termos separados por espaço:", font=font_bold, bg="#f2f2f2")
label_termos.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_termos = tk.Entry(root, font=font_normal, width=30)
entry_termos.grid(row=1, column=1, padx=10, pady=10)

# Botões de operações com design aprimorado
btn_soma_pa = tk.Button(root, text="Soma dos termos da P.A.", font=font_normal, command=calcular_soma_pa, bg="#4CAF50", fg="white", width=25)
btn_soma_pa.grid(row=2, column=0, columnspan=2, pady=5)

btn_termo_pa = tk.Button(root, text="Termo da P.A.", font=font_normal, command=calcular_termo_pa, bg="#2196F3", fg="white", width=25)
btn_termo_pa.grid(row=3, column=0, columnspan=2, pady=5)

btn_termo_pg = tk.Button(root, text="Termo da P.G.", font=font_normal, command=calcular_termo_pg, bg="#FF9800", fg="white", width=25)
btn_termo_pg.grid(row=4, column=0, columnspan=2, pady=5)

btn_soma_pg = tk.Button(root, text="Soma dos termos da P.G.", font=font_normal, command=calcular_soma_pg, bg="#FF5722", fg="white", width=25)
btn_soma_pg.grid(row=5, column=0, columnspan=2, pady=5)

# Label para mostrar o resultado
resultado_label = tk.Label(root, text="Resultado:", font=font_bold, bg="#f2f2f2", fg="#333")
resultado_label.grid(row=6, column=0, columnspan=2, pady=20)

# Botão para limpar os campos
btn_limpar = tk.Button(root, text="Limpar", font=font_normal, command=limpar_campos, bg="#9E9E9E", fg="white", width=25)
btn_limpar.grid(row=7, column=0, columnspan=2, pady=10)

# Tornar as linhas e colunas redimensionáveis
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Iniciando o loop principal da interface
root.mainloop()
