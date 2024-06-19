import tkinter as tk
from tkinter import ttk, messagebox

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
        

# Interface gráfica
app = tk.Tk()
app.title("Calculadora de Engenharia Civil")

# Frame para a aba de Engenharia Civil
aba_engenharia_civil = ttk.Frame(app)
aba_engenharia_civil.pack(fill=tk.BOTH, expand=True)

# Labels e entradas para carga e distância
label_carga = ttk.Label(aba_engenharia_civil, text="Carga (N):")
label_carga.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entrada_carga = ttk.Entry(aba_engenharia_civil)
entrada_carga.grid(row=0, column=1, padx=10, pady=10)

label_distancia = ttk.Label(aba_engenharia_civil, text="Distância (m):")
label_distancia.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entrada_distancia = ttk.Entry(aba_engenharia_civil)
entrada_distancia.grid(row=1, column=1, padx=10, pady=10)

# Botão para calcular o Momento Fletor
botao_calcular = ttk.Button(aba_engenharia_civil, text="Calcular Momento Fletor", command=calcular_momento_fletor)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Rodar o loop principal da aplicação
app.mainloop()
