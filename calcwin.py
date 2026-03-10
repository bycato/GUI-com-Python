import tkinter as tk #isso é uma biblioteca pra criar uma interface gráfica.

def Limpar():
    display.delete(0, tk.END)

def Calcular():
    try:
        resultado = eval(display.get())
        Limpar()
        display.insert(0, str(resultado))
    except:
        Limpar()
        display.insert(0, "ERROR")

def Adicionar(valor):
    display.insert(tk.END, valor)



#criando janela
janela = tk.Tk()
janela.title("Calculadora") #título da janela
janela.geometry("330x350") #resolução em pixeis da janela

display = tk.Entry(janela, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    ('7', 1, 0),('8', 1, 1),('9', 1, 2),('/', 1, 3),
    ('4', 2, 0),('5', 2, 1),('6', 2, 2),('*', 2, 3),
    ('1', 3, 0),('2', 3, 1),('3', 3, 2),('-', 3, 3),
    ('.', 4, 0),('0', 4, 1),('=', 4, 2),('+', 4, 3),
]

for(texto, linha, coluna) in botoes:
    if texto == '=':
        tk.Button(janela, text=texto, width=5, height=2, command=Calcular).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(janela, text=texto, width=5, height=2, command= lambda t=texto : Adicionar(t)).grid(row=linha, column=coluna, padx=5, pady=5)

#botao pa limpa :D
clear = tk.Button(janela, text="C", width=22, height=2, bg = "red", fg = "white", command=Limpar)
clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

janela.mainloop() #inicializa e mantém a janela em funcionamento.