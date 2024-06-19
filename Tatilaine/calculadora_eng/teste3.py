import math
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Funções matemáticas básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        messagebox.showerror("Erro", "Divisão por zero!")
        return None
    else:
        return a / b

def potenciacao(a, n):
    return a ** n

def raiz_quadrada(a):
    if a < 0:
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        return None
    else:
        return a ** 0.5

def raiz_n_esima(a, n):
    if a < 0 and n % 2 == 0:
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        return None
    else:
        return a ** (1 / n)

# Funções para funções matemáticas
def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    if math.cos(x) == 0:
        messagebox.showerror("Erro", "Tangente indefinida!")
        return None
    else:
        return math.tan(x)

def logaritmo_natural(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo natural de número não positivo!")
        return None
    else:
        return math.log(x)

def logaritmo_decimal(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo decimal de número não positivo!")
        return None
    else:
        return math.log10(x)

# Funções para operações com memória
memoria = {}

def adicionar_memoria(nome, valor):
    memoria[nome] = valor

def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def consultar_memoria(nome):
    if nome in memoria:
        return memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Informação", "Memória limpa.")

# Funções para integração numérica
def integral_numerica(funcao_str, a, b, n):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        resultado = integrate.quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

# Funções para derivada numérica
def derivada_numerica(funcao_str, x, h):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

# Funções para transformada de Fourier
def transformada_fourier(sinal):
    fourier = np.fft.fft(sinal)
    return fourier

# Funções para cálculos estruturais (implementar de acordo com suas necessidades)
def momento_fletor(forca, distancia, tipo_apoio):
    # Implementar a lógica para cálculo de momento fletor considerando o tipo de apoio (engasta, bi-apoiada, etc.)
    pass

def cortante(forca, distancia, tipo_apoio):
    # Implementar a lógica para cálculo de cortante considerando o tipo de apoio
    pass

def normal(area, tensao):
    # Implementar a Lei de Hooke para calcular a força normal
    return area * tensao

def analise_esforcos_composta(materiais, geometrias):
    # Implementar a lógica para análise de esforços em vigas compostas
    pass

def dimensionamento_coluna(carga, material, comprimento):
    # Implementar a lógica para dimensionamento de colunas utilizando normas como a NBR 6118
    pass

def calculo_laje(carga, vão, material, espessura):
    # Implementar a lógica para cálculo de lajes utilizando métodos como o método de vigas biapoiadas
    pass

# Funções para mecânica dos solos (implementar de acordo com suas necessidades)
def capacidade_carga_estacas(metodo, parametros):
    # Implementar a lógica para cálculo da capacidade de carga de estacas utilizando métodos como Meyerhof ou Terzaghi
    pass

def estabilidade_talude(metodo, parametros):
    # Implementar a lógica para análise da estabilidade de taludes utilizando métodos como Mohr-Coulomb ou Bishop
    pass

def permeabilidade_solo(metodo, parametros):
    # Implementar a lógica para cálculo da permeabilidade do solo utilizando métodos como teste de permeabilidade
    pass

def recalque_solo(metodo, parametros):
    # Implementar a lógica para cálculo de recalque do solo utilizando métodos como elasticidade ou Winkler
    pass

# Funções para hidráulica e saneamento (implementar de acordo com suas necessidades)
def fluxo_tubulacao(vazao, diametro, rugosidade):
    # Implementar a lógica para cálculo do fluxo em tubulações utilizando equações como Darcy-Weisbach
    pass

def fluxo_canal(area_molhada, declividade, rugosidade):
    # Implementar a lógica para cálculo do fluxo em canais abertos utilizando equações como Manning
    pass

def dimensionamento_rede_hidraulica(metodo, parametros):
    # Implementar a lógica para dimensionamento de redes hidráulicas utilizando normas como NBR 10838
    pass

def tratamento_agua(metodo, parametros):
    # Implementar a lógica para cálculo de estações de tratamento de água utilizando métodos como coagulação
    pass

def tratamento_esgoto(metodo, parametros):
    # Implementar a lógica para cálculo de estações de tratamento de esgoto utilizando métodos como ativação por lodo

# Funções para topografia (implementar de acordo com suas necessidades)
def area_terreno(vertices):
    # Implementar a lógica para cálculo da área de um terreno utilizando métodos como planímetro
    pass

def volume_terreno(area, profundidade):
    # Implementar a lógica para cálculo do volume de um terreno
    pass

def nivelamento(pontos):
    # Implementar a lógica para nivelamento utilizando instrumentos como o nível
    pass

def locacao_obra(coordenadas):
    # Implementar a lógica para locação de obras utilizando instrumentos como o teodolito
    pass

def curva_nivel(pontos):
    # Implementar a lógica para traçado de curvas de nível utilizando métodos de interpolação

# Interface gráfica (utilizando tkinter como exemplo)
def interface():
    # Criar a janela principal
    janela = Tk()
    janela.title("Calculadora Científica para Engenharia Civil")

    # Criar frames para organização dos componentes
    frame_operacoes_basicas = LabelFrame(janela, text="Operações Básicas")
    frame_operacoes_basicas.grid(row=0, column=0, padx=10, pady=5)

    frame_funcoes_matematicas = LabelFrame(janela, text="Funções Matemáticas")
    frame_funcoes_matematicas.grid(row=1, column=0, padx=10, pady=5)

    frame_memoria = LabelFrame(janela, text="Memória")
    frame_memoria.grid(row=2, column=0, padx=10, pady=5)

    frame_transformada_fourier = LabelFrame(janela, text="Transformada de Fourier")
    frame_transformada_fourier.grid(row=3, column=0, padx=10, pady=5)

    frame_calculos_estruturais = LabelFrame(janela, text="Cálculos Estruturais")
    frame_calculos_estruturais.grid(row=4, column=0, padx=10, pady=5)

    # Campos e botões para operações básicas
    Label(frame_operacoes_basicas, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
    Entry(frame_operacoes_basicas, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="numero1").grid(row=0, column=1, padx=5, pady=5)

    Label(frame_operacoes_basicas, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
    Entry(frame_operacoes_basicas, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="numero2").grid(row=1, column=1, padx=5, pady=5)

    Button(frame_operacoes_basicas, text="Somar", width=10, command=lambda: executar_operacao(soma)).grid(row=0, column=2, padx=5, pady=5)
    Button(frame_operacoes_basicas, text="Subtrair", width=10, command=lambda: executar_operacao(subtracao)).grid(row=1, column=2, padx=5, pady=5)
    Button(frame_operacoes_basicas, text="Multiplicar", width=10, command=lambda: executar_operacao(multiplicacao)).grid(row=0, column=3, padx=5, pady=5)
    Button(frame_operacoes_basicas, text="Dividir", width=10, command=lambda: executar_operacao(divisao)).grid(row=1, column=3, padx=5, pady=5)

    # Campos e botões para funções matemáticas
    Label(frame_funcoes_matematicas, text="Número:").grid(row=0, column=0, padx=5, pady=5)
    Entry(frame_funcoes_matematicas, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="numero").grid(row=0, column=1, padx=5, pady=5)

    Button(frame_funcoes_matematicas, text="Seno", width=10, command=lambda: executar_funcao(seno)).grid(row=0, column=2, padx=5, pady=5)
    Button(frame_funcoes_matematicas, text="Cosseno", width=10, command=lambda: executar_funcao(cosseno)).grid(row=0, column=3, padx=5, pady=5)
    Button(frame_funcoes_matematicas, text="Tangente", width=10, command=lambda: executar_funcao(tangente)).grid(row=0, column=4, padx=5, pady=5)
    Button(frame_funcoes_matematicas, text="Log Natural", width=10, command=lambda: executar_funcao(logaritmo_natural)).grid(row=1, column=2, padx=5, pady=5)
    Button(frame_funcoes_matematicas, text="Log Decimal", width=10, command=lambda: executar_funcao(logaritmo_decimal)).grid(row=1, column=3, padx=5, pady=5)
    Button(frame_funcoes_matematicas, text="Raiz Quadrada", width=12, command=lambda: executar_funcao(raiz_quadrada)).grid(row=1, column=4, padx=5, pady=5)
    Button(frame_funcoes_matematicas, text="Raiz N-ésima", width=12, command=lambda: executar_funcao(raiz_n_esima)).grid(row=2, column=2, padx=5, pady=5)

    # Campos e botões para memória
    Label(frame_memoria, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    Entry(frame_memoria, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="nome_memoria").grid(row=0, column=1, padx=5, pady=5)
    Label(frame_memoria, text="Valor:").grid(row=1, column=0, padx=5, pady=5)
    Entry(frame_memoria, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="valor_memoria").grid(row=1, column=1, padx=5, pady=5)

    Button(frame_memoria, text="Adicionar", width=10, command=adicionar_a_memoria).grid(row=0, column=2, padx=5, pady=5)
    Button(frame_memoria, text="Remover", width=10, command=remover_da_memoria).grid(row=1, column=2, padx=5, pady=5)
    Button(frame_memoria, text="Consultar", width=10, command=consultar_memoria).grid(row=0, column=3, padx=5, pady=5)
    Button(frame_memoria, text="Limpar", width=10, command=limpar_memoria).grid(row=1, column=3, padx=5, pady=5)

    # Campos e botões para transformada de Fourier
    Label(frame_transformada_fourier, text="Sinal (valores separados por vírgula):").grid(row=0, column=0, padx=5, pady=5)
    Entry(frame_transformada_fourier, width=50, justify=LEFT, bd=5, relief=SUNKEN, name="sinal_fourier").grid(row=0, column=1, columnspan=3, padx=5, pady=5)

    Button(frame_transformada_fourier, text="Transformada", width=15, command=executar_transformada_fourier).grid(row=1, column=1, padx=5, pady=5)

    # Campos e botões para cálculos estruturais
    Label(frame_calculos_estruturais, text="Força (N):").grid(row=0, column=0, padx=5, pady=5)
    Entry(frame_calculos_estruturais, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="forca").grid(row=0, column=1, padx=5, pady=5)

    Label(frame_calculos_estruturais, text="Distância (m):").grid(row=1, column=0, padx=5, pady=5)
    Entry(frame_calculos_estruturais, width=15, justify=RIGHT, bd=5, relief=SUNKEN, name="distancia").grid(row=1, column=1, padx=5, pady=5)

    Label(frame_calculos_estruturais, text="Tipo de Apoio:").grid(row=2, column=0, padx=5, pady=5)
    tipo_apoio = StringVar()
    tipo_apoio.set("Engastada")
    OptionMenu(frame_calculos_estruturais, tipo_apoio, "Engastada", "Bi-Apoiada", "Móvel").grid(row=2, column=1, padx=5, pady=5)

    Button(frame_calculos_estruturais, text="Momento Fletor", width=15, command=executar_momento_fletor).grid(row=0, column=2, padx=5, pady=5)
    Button(frame_calculos_estruturais, text="Cortante", width=15, command=executar_cortante).grid(row=1, column=2, padx=5, pady=5)
    Button(frame_calculos_estruturais, text="Normal", width=15, command=executar_normal).grid(row=2, column=2, padx=5, pady=5)

    janela.mainloop()

# Função para execução de operações básicas
def executar_operacao(operacao):
    try:
        numero1 = float(memoria["numero1"].get())
        numero2 = float(memoria["numero2"].get())
        resultado = operacao(numero1, numero2)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Resultado da operação: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Insira números válidos.")

# Função para execução de funções matemáticas
def executar_funcao(funcao):
    try:
        numero = float(memoria["numero"].get())
        resultado = funcao(numero)
        if resultado is not None:
            messagebox.showinfo("Resultado", f"Resultado da função: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Insira um número válido.")

# Funções matemáticas
def seno(numero):
    return round(math.sin(numero), 6)

def cosseno(numero):
    return round(math.cos(numero), 6)

def tangente(numero):
    return round(math.tan(numero), 6)

def logaritmo_natural(numero):
    return round(math.log(numero), 6)

def logaritmo_decimal(numero):
    return round(math.log10(numero), 6)

def raiz_quadrada(numero):
    return round(math.sqrt(numero), 6)

def raiz_n_esima(numero):
    try:
        n = int(simpledialog.askstring("Raiz N-ésima", "Digite o valor de N para a raiz N-ésima: "))
        if n <= 0:
            return None
        return round(numero ** (1/n), 6)
    except (ValueError, TypeError):
        return None

# Funções para memória
def adicionar_a_memoria():
    nome = memoria["nome_memoria"].get()
    valor = memoria["valor_memoria"].get()
    if nome != "" and valor != "":
        try:
            valor = float(valor)
            memoria[nome] = valor
            messagebox.showinfo("Adição à memória", f"Valor {valor} adicionado à memória com nome {nome}.")
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico válido.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos para adicionar à memória.")

def remover_da_memoria():
    nome = memoria["nome_memoria"].get()
    if nome in memoria:
        del memoria[nome]
        messagebox.showinfo("Remoção da memória", f"Item {nome} removido da memória.")
    else:
        messagebox.showerror("Erro", f"O item {nome} não está na memória.")

def consultar_memoria():
    nome = memoria["nome_memoria"].get()
    if nome in memoria:
        messagebox.showinfo("Consulta à memória", f"O valor na memória com nome {nome} é: {memoria[nome]}.")
    else:
        messagebox.showerror("Erro", f"O item {nome} não está na memória.")

def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Limpeza da memória", "Todos os itens da memória foram removidos.")

# Funções para transformada de Fourier
def executar_transformada_fourier():
    sinal = memoria["sinal_fourier"].get()
    if sinal != "":
        try:
            sinal = [float(x.strip()) for x in sinal.split(",")]
            transformada = numpy.fft.fft(sinal)
            messagebox.showinfo("Transformada de Fourier", f"Transformada do sinal: {transformada}")
        except ValueError:
            messagebox.showerror("Erro", "O sinal deve conter apenas números separados por vírgula.")
    else:
        messagebox.showerror("Erro", "Insira um sinal válido para a transformada de Fourier.")

# Funções para cálculos estruturais
def executar_momento_fletor():
    try:
        forca = float(memoria["forca"].get())
        distancia = float(memoria["distancia"].get())
        tipo_apoio = memoria["tipo_apoio"].get()
        if tipo_apoio == "Engastada":
            momento_fletor = round(forca * distancia, 6)
        elif tipo_apoio == "Bi-Apoiada":
            momento_fletor = round(forca * distancia / 2, 6)
        elif tipo_apoio == "Móvel":
            momento_fletor = round(forca * distancia / 4, 6)
        messagebox.showinfo("Momento Fletor", f"O momento fletor é: {momento_fletor} Nm.")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")

def executar_cortante():
    try:
        forca = float(memoria["forca"].get())
        distancia = float(memoria["distancia"].get())
        tipo_apoio = memoria["tipo_apoio"].get()
        cortante = round(forca / (tipo_apoio == "Móvel" and 2 or 1), 6)
        messagebox.showinfo("Cortante", f"O valor do cortante é: {cortante} N.")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")

def executar_normal():
    try:
        forca = float(memoria["forca"].get())
        distancia = float(memoria["distancia"].get())
        tipo_apoio = memoria["tipo_apoio"].get()
        normal = round(forca / distancia, 6)
        messagebox.showinfo("Normal", f"O valor da normal é: {normal} N/m.")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")
