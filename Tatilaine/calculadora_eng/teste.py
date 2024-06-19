import tkinter as tk
from tkinter import messagebox, ttk

# Função para calcular o Momento Fletor
def calcular_momento_fletor():
    try:
        # Obter os valores de entrada e converter para float
        carga = float(entrada_carga.get())
        distancia = float(entrada_distancia.get())
        
        # Calcular o Momento Fletor (M = carga * distância)
        momento_fletor = carga * distancia
        
        # Exibir o resultado em uma messagebox
        messagebox.showinfo("Resultado", f"O Momento Fletor é {momento_fletor} Nm")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos para a carga e a distância.")
        

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Engenharia")

# Criando um Notebook para as abas
notebook = ttk.Notebook(app)

# Criando frames para cada aba
aba_basica = ttk.Frame(notebook)
aba_avancada = ttk.Frame(notebook)
aba_memoria = ttk.Frame(notebook)
aba_engenharia_civil = ttk.Frame(notebook)

# Adicionando os frames ao notebook com seus respectivos títulos
notebook.add(aba_basica, text="Básica")
notebook.add(aba_avancada, text="Avançada")
notebook.add(aba_memoria, text="Memória")
notebook.add(aba_engenharia_civil, text="Engenharia Civil")

notebook.pack(expand=1, fill="both")

# Funções básicas (soma, subtração, multiplicação, divisão)
label_titulo_basica = tk.Label(aba_basica, text="Funções Básicas")
label_titulo_basica.pack(pady=10)

botao_operacoes_basicas = tk.Button(aba_basica, text="Operações Básicas")
botao_operacoes_basicas.pack(pady=5)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Funções de Engenharia Civil")
label_titulo_engenharia_civil.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

label_carga = tk.Label(aba_engenharia_civil, text="Carga (N):")
label_carga.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entrada_carga = tk.Entry(aba_engenharia_civil)
entrada_carga.grid(row=1, column=1, padx=10, pady=5)

label_distancia = tk.Label(aba_engenharia_civil, text="Distância (m):")
label_distancia.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entrada_distancia = tk.Entry(aba_engenharia_civil)
entrada_distancia.grid(row=2, column=1, padx=10, pady=5)

botao_calcular_momento_fletor = tk.Button(aba_engenharia_civil, text="Calcular Momento Fletor", command=calcular_momento_fletor)
botao_calcular_momento_fletor.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Botões adicionais de Engenharia Civil
botao_funcoes_engenharia_civil = tk.Button(aba_engenharia_civil, text="Outras Operações", command=lambda: messagebox.showinfo("Informação", "Abrindo outras operações de engenharia civil..."))
botao_funcoes_engenharia_civil.grid(row=4, column=0, columnspan=2, pady=5)

app.mainloop()
