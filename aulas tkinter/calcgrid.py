import tkinter as tk #isso é uma biblioteca pra criar uma interface gráfica.

def Somar():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        soma = n1 + n2
        res.config(text=f"Resultado: {soma}")       
    except:
        res.config(text=f"Informe os números válidos.")    

def Sub():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        sub = n1 - n2
        res.config(text=f"Resultado: {sub}")       
    except:
        res.config(text=f"Informe os números válidos.")   

def Mult():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        mult = n1 * n2
        res.config(text=f"Resultado: {mult}")       
    except:
        res.config(text=f"Informe os números válidos.")   

def Div():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        div = n1 / n2
        res.config(text=f"Resultado: {div}")       
    except:
        res.config(text=f"Informe os números válidos.")   




#criando janela
janela = tk.Tk()
janela.title("Calculadora") #título da janela
janela.geometry("300x400") #resolução em pixeis da janela

num1 = tk.Label(janela, text="Número 1:") #parâmetros de um texto
num1.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entrada1 = tk.Entry(janela)#função de input básico
entrada1.grid(row=0, column=2) 

num2 = tk.Label(janela, text="Número 2:")
num2.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=2)

res = tk.Label(janela, text="Resultado:")
res.grid(row=5, column=1)

botaoSm = tk.Button(janela, text="Soma", command=Somar) #botao, onde tem o texto no botao + a função que armar quando clicado.
botaoSm.grid(row=6, column=1, padx=10, pady=5, sticky="w")

botaoSb = tk.Button(janela, text="Subtrair", command=Sub)
botaoSb.grid(row=6, column=2, padx=10, pady=5, sticky="w")

botaoMult = tk.Button(janela, text="Multiplicar", command=Mult)
botaoMult.grid(row=7, column=1, padx=10, pady=5, sticky="w")

botaoDiv = tk.Button(janela, text="Divisão", command=Div)
botaoDiv.grid(row=7, column=2, padx=10, pady=5, sticky="w")



janela.mainloop() #inicializa e mantém a janela em funcionamento.

