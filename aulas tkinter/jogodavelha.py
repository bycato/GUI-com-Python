import tkinter as tk
from tkinter import messagebox

#Função para a mecânica de pontuar O ou X nos botões da tela.
def Clique(npos): #passa a posição como parâmetro, conforme visto no for da túpla.
    
    global count, tabuleiro #variáveis globais

    if tabuleiro[npos] != "": #não retorna nada se estiver vazio
        return

    if count == 0: #alternando cliques entre X e O -> O jogo começará com O e alternará o contador para o próximo, X.
        count = 1
        simbolo = "O" #variável para reaproveitamento de código
    else:
        count = 0
        simbolo = "X"

    tabuleiro[npos] = simbolo 
    globals()[f'btn{npos}'].config(text=simbolo, state="disabled") #variavel utilizada aqui

    win = verifyVitoria() #verificador de vitória
    if win: #se true:
        messagebox.showinfo("Fim de jogo", f'{win} venceu!') #mostra a mensagem
        disabledBt() #desabilita os botões temporáriamente
        Limpar() #e os limpa
    elif "" not in tabuleiro: #se der velha, empate:
        messagebox.showinfo("Fim de jogo", f'Empate!') #mostra a mensagem
        disabledBt() #desabilita os campos
        Limpar() #e os limpa

#Função para verificar a vitória do jogo: 
def verifyVitoria():
    combinacoes = [ #combinações de vitória do jogo
        (0,1,2), (3,4,5), (6,7,8), #combinações horizontais, numeradas pelos npos dos botões feitos por for
        (0,3,6), (1,4,7), (2,5,8), #combinações verticais
        (0,4,8), (2,4,6) #combinações diagonais
    ]

    for a, b, c in combinacoes: #para cada número dos campos inserido, sempre verifica se existe 3 inputs do mesmo tipo nas combinações antes inputadas
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != "": #se combinação for true, e não estiver vazia em qualquer combinação 
            return tabuleiro[a] #retona win
    
    return None #se não, o jogo continua até ganhar/empatar

#Funçao para desabilitar os botões:
def disabledBt():
    for i in range(9): #gira o for 9 vezes
        globals()[f'btn{i}'].config(state = "disabled") #para associar cada btn o disable no state
    
#Função para limpar os campos:
def Limpar():

    global count , tabuleiro #variáveis globais
 
    tabuleiro = [""] * 9 #sobrescreve na variável global para vazio, para apagar os inputs

    for i in range(9): #gira o for 9 vezes
        globals()[f'btn{i}'].config(text="", state="normal") #para reativar cada botão, e limpar o texto

janela = tk.Tk()
janela.title("Jogo da Velha")
janela.geometry("400x500")

#Variáveis globais
count = 0 #contador
tabuleiro = [""] * 9 #lista de combinações -> serve para trackear as combinações possíveis para alcançar a vitória com base nas posições.

botoes = [ #túpla para gerar os botões gráficamente
    ('', 1, 0, 0),('', 1, 1, 1),('', 1, 2, 2), # ("texto do botão", fileira, coluna, posição)
    ('', 2, 0, 3),('', 2, 1, 4),('', 2, 2, 5),
    ('', 3, 0, 6),('', 3, 1, 7),('', 3, 2, 8),
    ('Limpar', 4, 1, 9)
]

for(texto, linha, coluna, npos) in botoes: #para a túpla, criamos um for para otimizar a criação dos botões
    if npos < 9: #verificando se não é o limpar, se não:
        #cria um botão normal, com a mecânica (Clique), com o parâmetro de sua posição sendo passado por lambda
        globals()[f'btn{npos}'] = tk.Button(janela, text=texto, width=12, height=6, command= lambda t = npos: Clique(t))
        globals()[f'btn{npos}'].grid(row=linha, column=coluna, padx=5, pady=5)
    else: #se for o botão limpar:
        #cria um botão normal, com a mecânica que ativa a função Limpar().
        globals()[f'btn{npos}'] = tk.Button(janela, text=texto, width=6, height=3, command=Limpar)
        globals()[f'btn{npos}'].grid(row=linha, column=coluna, padx=5, pady=5)

#bota a janela em funcionamento loopando a execução dela, até que seja terminada forçadamente.
janela.mainloop()