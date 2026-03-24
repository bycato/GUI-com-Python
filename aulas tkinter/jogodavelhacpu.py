import tkinter as tk
import random
from random import randrange
from tkinter import messagebox

def player_move(npos):
    global count, tabuleiro

    if tabuleiro[npos] != "":
        return
    
    if count == 1:
        count = 0
        simbolo = "O"
    else:
        return
    


    tabuleiro[npos] = simbolo
    globals()[f'btn{npos}'].config(text=simbolo, state="disabled")

    win = verifyVitoria() #verificador de vitória
    if win: #se true:
        messagebox.showinfo("Fim de jogo", f'{win} venceu!') #mostra a mensagem
        disabledBt() #desabilita os botões temporáriamente
        Limpar() #e os limpa
    elif "" not in tabuleiro: #se der velha, empate:
        messagebox.showinfo("Fim de jogo", f'Empate!') #mostra a mensagem
        disabledBt() #desabilita os campos
        Limpar() #e os limpa

    computer_move()

def computer_move():
    global count, tabuleiro

    if count == 0:

        # primeira jogada: centro
        if tabuleiro[4] == "":
            npos = 4
        else:
            while True:
                npos = random.randrange(0,9)
                if tabuleiro[npos] == "":
                    break

        simbolo = "X"
        tabuleiro[npos] = simbolo
        globals()[f'btn{npos}'].config(text=simbolo, state="disabled")

        count = 1   

    else:
        return
    
    tabuleiro[npos] = simbolo
    globals()[f'btn{npos}'].config(text=simbolo, state="disabled")

    win = verifyVitoria() #verificador de vitória
    if win: #se true:
        messagebox.showinfo("Fim de jogo", f'{win} venceu!') #mostra a mensagem
        disabledBt() #desabilita os botões temporáriamente
        Limpar() #e os limpa
    elif "" not in tabuleiro: #se der velha, empate:
        messagebox.showinfo("Fim de jogo", f'Empate!') #mostra a mensagem
        disabledBt() #desabilita os campos
        Limpar() #e os limpa 
    return

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

def disabledBt():
    for i in range(9): #gira o for 9 vezes
        globals()[f'btn{i}'].config(state = "disabled") #para associar cada btn o disable no state
  
def Limpar():

    global count , tabuleiro #variáveis globais
 
    tabuleiro = [""] * 9 #sobrescreve na variável global para vazio, para apagar os inputs

    for i in range(9): #gira o for 9 vezes
        globals()[f'btn{i}'].config(text="", state="normal") #para reativar cada botão, e limpar o texto

janela = tk.Tk()
janela.geometry("320x500")
janela.title("Jogo da Velha - CPU")

count = 0
tabuleiro = [""] * 9

botoes = [ 
    ('', 1, 0, 0),('', 1, 1, 1),('', 1, 2, 2), 
    ('', 2, 0, 3),('', 2, 1, 4),('', 2, 2, 5),
    ('', 3, 0, 6),('', 3, 1, 7),('', 3, 2, 8),
    ('Limpar', 4, 1, 9)
]

for(texto, linha, coluna, npos) in botoes:
    if npos < 9:
        globals()[f'btn{npos}'] = tk.Button(janela, text=texto, width=12, height=6, command= lambda t = npos: player_move(t))
        globals()[f'btn{npos}'].grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        globals()[f'btn{npos}'] = tk.Button(janela, text=texto, width=6, height=3, command=Limpar)
        globals()[f'btn{npos}'].grid(row=linha, column=coluna, padx=5, pady=5)

computer_move()

janela.mainloop()