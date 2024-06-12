from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sys
import os

# Adiciona o diretório pai ao sys.path para encontrar módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o módulo operacoes_basicas
import operacoes_basicas

def abrir_calculos_estruturais():
    messagebox.showinfo("Informação", "Abrindo cálculos estruturais...")

def abrir_derivadas_numericas():
    messagebox.showinfo("Informação", "Abrindo derivadas numéricas...")

def abrir_transformada_fourier():
    messagebox.showinfo("Informação", "Abrindo transformada de Fourier...")

def abrir_funcionalidade_basica():
    messagebox.showinfo("Informação", "Abrindo funcionalidade básica...")

def abrir_funcionalidade_memoria():
    messagebox.showinfo("Informação", "Abrindo funcionalidade de memória...")

def abrir_funcoes_engenharia_civil():
    messagebox.showinfo("Informação", "Abrindo funções de engenharia civil...")

def abrir_funcoes_matematicas():
    messagebox.showinfo("Informação", "Abrindo funções matemáticas...")

def abrir_hidraulica_saneamento():
    messagebox.showinfo("Informação", "Abrindo hidráulica e saneamento...")

def abrir_integracao_numerica():
    messagebox.showinfo("Informação", "Abrindo integração numérica...")

def abrir_mecanica_dos_solos():
    messagebox.showinfo("Informação", "Abrindo mecânica dos solos...")

def abrir_operacoes_com_potencias_raizes():
    messagebox.showinfo("Informação", "Abrindo operações com potências e raízes...")

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
            b = None  # Não precisa de b para raiz quadrada
        elif operacao == "Raiz n-ésima":
            resultado = operacoes_basicas.raiz_n_esima(a, b)

        if resultado is not None:
            resultado_label.config(text=f"Resultado: {resultado}")
        else:
            resultado_label.config(text="Erro na operação")

    nova_janela = tk.Toplevel(app)
    nova_janela.title("Operações Básicas")

    operacao_var = tk.StringVar(nova_janela)
    operacao_var.set("Soma")  # Operação padrão

    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Potenciação", "Raiz Quadrada", "Raiz n-ésima"]
    operacao_menu = tk.OptionMenu(nova_janela, operacao_var, *operacoes)
    operacao_menu.pack(pady=5)

    entrada_a = tk.Entry(nova_janela)
    entrada_a.pack(pady=5)
    entrada_a.insert(0, "Valor 7")

    entrada_b = tk.Entry(nova_janela)
    entrada_b.pack(pady=5)
    entrada_b.insert(0, "Valor B")

    calcular_button = tk.Button(nova_janela, text="Calcular", command=calcular)
    calcular_button.pack(pady=5)

    resultado_label = tk.Label(nova_janela, text="Resultado:")
    resultado_label.pack(pady=5)

def abrir_operacoes_com_memoria():
    messagebox.showinfo("Informação", "Abrindo operações com memória...")

def abrir_potenciacao_radiciacao():
    messagebox.showinfo("Informação", "Abrindo potenciação e radiciação...")

def abrir_topografia():
    messagebox.showinfo("Informação", "Abrindo topografia...")

def abrir_tratamento_de_erros():
    messagebox.showinfo("Informação", "Abrindo tratamento de erros...")

# Interface gráfica principal

app = tk.Tk()
app.title("Calculadora Engenharia")

# Criando um Notebook para as abas
notebook = ttk.Notebook(app)

# Criando frames para cada aba
aba_basica = Frame(notebook)
aba_avancada = Frame(notebook)
aba_memoria = Frame(notebook)
aba_engenharia_civil = Frame(notebook)

# Adicionando os frames ao notebook com seus respectivos títulos
notebook.add(aba_basica, text="Básica")
notebook.add(aba_avancada, text="Avançada")
notebook.add(aba_memoria, text="Memória")
notebook.add(aba_engenharia_civil, text="Engenharia Civil")

notebook.pack(expand=1, fill="both")

# Funções básicas (soma, subtração, multiplicação, divisão)
label_titulo_basica = Label(aba_basica, text="Funções Básicas")
label_titulo_basica.pack(pady=10)

botao_operacoes_basicas = tk.Button(aba_basica, text="Operações Básicas", command=abrir_operacoes_basicas)
botao_operacoes_basicas.pack(pady=5)

botao_potenciacao_radiciacao = Button(aba_basica, text="Potenciação e Radiciação", command=abrir_potenciacao_radiciacao)
botao_potenciacao_radiciacao.pack(pady=5)

botao_funcionalidade_basica = Button(aba_basica, text="Funcionalidade Básica", command=abrir_funcionalidade_basica)
botao_funcionalidade_basica.pack(pady=5)

# Funções avançadas (integração, derivada, transformada de Fourier)
label_titulo_avancada = Label(aba_avancada, text="Funções Avançadas")
label_titulo_avancada.pack(pady=10)

botao_calculos_estruturais = Button(aba_avancada, text="Cálculos Estruturais", command=abrir_calculos_estruturais)
botao_calculos_estruturais.pack(pady=5)

botao_derivadas_numericas = Button(aba_avancada, text="Derivadas Numéricas", command=abrir_derivadas_numericas)
botao_derivadas_numericas.pack(pady=5)

botao_transformada_fourier = Button(aba_avancada, text="Transformada de Fourier", command=abrir_transformada_fourier)
botao_transformada_fourier.pack(pady=5)

botao_integracao_numerica = Button(aba_avancada, text="Integração Numérica", command=abrir_integracao_numerica)
botao_integracao_numerica.pack(pady=5)

botao_funcoes_matematicas = Button(aba_avancada, text="Funções Matemáticas", command=abrir_funcoes_matematicas)
botao_funcoes_matematicas.pack(pady=5)

botao_tratamento_de_erros = Button(aba_avancada, text="Tratamento de Erros e Mensagem", command=abrir_tratamento_de_erros)
botao_tratamento_de_erros.pack(pady=5)

# Funções de memória (adicionar, remover, consultar, limpar)
label_titulo_memoria = Label(aba_memoria, text="Funções de Memória")
label_titulo_memoria.pack(pady=10)

botao_operacoes_com_memoria = Button(aba_memoria, text="Operações com Memória", command=abrir_operacoes_com_memoria)
botao_operacoes_com_memoria.pack(pady=5)

botao_funcionalidade_memoria = Button(aba_memoria, text="Funcionalidade de Memória", command=abrir_funcionalidade_memoria)
botao_funcionalidade_memoria.pack(pady=5)

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = Label(aba_engenharia_civil, text="Funções de Engenharia Civil")
label_titulo_engenharia_civil.pack(pady=10)

botao_funcoes_engenharia_civil = Button(aba_engenharia_civil, text="Funções de Engenharia Civil", command=abrir_funcoes_engenharia_civil)
botao_funcoes_engenharia_civil.pack(pady=5)

botao_hidraulica_saneamento = Button(aba_engenharia_civil, text="Hidráulica e Saneamento", command=abrir_hidraulica_saneamento)
botao_hidraulica_saneamento.pack(pady=5)

botao_mecanica_dos_solos = Button(aba_engenharia_civil, text="Mecânica dos Solos", command=abrir_mecanica_dos_solos)
botao_mecanica_dos_solos.pack(pady=5)

botao_topografia = Button(aba_engenharia_civil, text="Topografia", command=abrir_topografia)
botao_topografia.pack(pady=5)

app.mainloop()
