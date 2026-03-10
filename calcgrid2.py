import tkinter as tk #isso é uma biblioteca pra criar uma interface gráfica.

def Calcular():
    op = str(op1.get())
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    if op == "+":
        soma = n1 + n2
        res.config(text=f'Resultado: {soma}')
    elif op == "-":
        sub = n1 - n2
        res.config(text=f'Resultado: {sub}')
    elif op == "*":
        mul = n1 * n2
        res.config(text=f'Resultado: {mul}')
    elif op == "/":
        div = n1 / n2
        res.config(text=f'Resultado: {div}')
    else:
        res.config(text=f'Digite uma função válida!')

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

op = tk.Label(janela, text="Operação:")
op.grid(row=4, column=1)
op1 = tk.Entry(janela)
op1.grid(row=4, column=2)

res = tk.Label(janela, text="Resultado:")
res.grid(row=5, column=1)

cal = tk.Button(janela, text="Calcular", command=Calcular)
cal.grid(row=6, column=1)


janela.mainloop() #inicializa e mantém a janela em funcionamento.

