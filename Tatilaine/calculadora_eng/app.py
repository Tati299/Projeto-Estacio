import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

# Adiciona o diretório pai ao sys.path para encontrar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o módulo operacoes_basicas
import operacoes_basicas

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

def abrir_operacoes_basicas():
    def calcular():
        operacao = operacao_var.get()
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get()) if entrada_b.get() else None
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")
            return

        if operacao == "Soma":
            resultado = operacoes_basicas.soma(a, b)
        elif operacao == "Subtração":
            resultado = operacoes_basicas.subtracao(a, b)
        elif operacao == "Multiplicação":
            resultado = operacoes_basicas.multiplicacao(a, b)
        elif operacao == "Divisão":
            resultado = operacoes_basicas.divisao(a, b)
        elif operacao == "Potenciação":
            resultado = operacoes_basicas.potenciacao(a, b)
        elif operacao == "Raiz Quadrada":
            resultado = operacoes_basicas.raiz_quadrada(a)

        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")
        else:
            resultado_label.config(text="Erro na operação")

    nova_janela = tk.Toplevel(app)
    nova_janela.title("Operações Básicas")

    operacao_var = tk.StringVar(nova_janela)
    operacao_var.set("Soma")  # Operação padrão

    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Potenciação", "Raiz Quadrada"]
    operacao_menu = tk.OptionMenu(nova_janela, operacao_var, *operacoes)
    operacao_menu.grid(row=0, column=0, padx=10, pady=5)

    entrada_a = tk.Entry(nova_janela)
    entrada_a.grid(row=1, column=0, padx=10, pady=5)
    entrada_a.insert(0, "Valor 1")

    entrada_b = tk.Entry(nova_janela)
    entrada_b.grid(row=2, column=0, padx=10, pady=5)
    entrada_b.insert(0, "Valor 2")

    # Ajuste para mostrar apenas um campo de entrada conforme a operação selecionada
    def mostrar_entrada_b():
        entrada_b.grid() if operacao_var.get() != "Raiz Quadrada" else entrada_b.grid_remove()

    operacao_var.trace_add('write', lambda *args: mostrar_entrada_b())

    calcular_button = tk.Button(nova_janela, text="Calcular", command=calcular)
    calcular_button.grid(row=3, column=0, padx=10, pady=5)

    resultado_label = tk.Label(nova_janela, text="Resultado:")
    resultado_label.grid(row=4, column=0, padx=10, pady=5)

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
label_titulo_basica.grid(row=0, column=0, padx=10, pady=10)

botao_operacoes_basicas = tk.Button(aba_basica, text="Operações Básicas", command=abrir_operacoes_basicas)
botao_operacoes_basicas.grid(row=1, column=0, padx=10, pady=5)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Funções de Engenharia Civil")
label_titulo_engenharia_civil.grid(row=0, column=0, padx=10, pady=10)

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
