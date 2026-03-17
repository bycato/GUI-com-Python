import tkinter as tk
import mysql.connector 
from mysql.connector import connect
from tkinter import ttk
from tkinter import messagebox


contador_id = 1

class Usuario:
    def __init__(self, id_usuario=None, nome="", email="", endereco=""):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email 
        self.endereco = endereco

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_usuario"
    )

def salvar_dados():

    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = input_nome.get()
        email = input_email.get()
        endereco = input_end.get()

        sql = "INSERT INTO usuario (nome, email, endereco) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, endereco))
        conn.commit()

        id_banco = cursor.lastrowid

        tabela.insert("", "end", values=(id_banco, nome, email, endereco))

        messagebox.showinfo("Sucesso", "AEEE deu certo, tá no banco!")
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f'Erro ao inserir os dados: \n{erro}')
    finally:
        cursor.close()
        conn.close()

    return

def carregar_usuarios():
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "SELECT id, nome, email, endereco FROM usuario"
        cursor.execute(sql)

        registros = cursor.fetchall()

        # limpa a tabela antes de carregar
        for item in tabela.get_children():
            tabela.delete(item)

        # insere os dados na tabela
        for usuario in registros:
            tabela.insert("", "end", values=usuario)

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro ao carregar usuários:\n{erro}")

    finally:
        cursor.close()
        conn.close()

def novo_usuario():
    global contador_id
    u = Usuario()
    u.nome = input_nome.get()
    u.email = input_email.get()
    u.endereco = input_end.get()


    if u.nome == "" or u.email == "" or u.endereco == "":
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
        return
    
    tabela.insert("", "end", values=(contador_id, u.nome, u.email, u.endereco))
    contador_id += 1
    limpar_campos()

def selecionar_usuario(event):
    selecionado = tabela.selection()

    if selecionado:
        limpar_campos()
        valores = tabela.item(selecionado, "values")

        input_id.insert(0, valores[0])
        input_nome.insert(0, valores[1])
        input_email.insert(0, valores[2])
        input_end.insert(0, valores[3])

def editar_usuario():
    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um usuário para alterar.")
        return

    valores = tabela.item(selecionado, "values")
    id_usuario = valores[0]
    
    nome = input_nome.get()
    email = input_email.get()
    endereco = input_end.get()

    if nome == "" or email == "" or endereco == "":
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "UPDATE usuario SET nome = %s, email = %s, endereco = %s WHERE id = %s"    

        cursor.execute(sql, (nome, email, endereco, id_usuario))
        conn.commit()

        messagebox.showinfo("Sucesso", "Dados alterados no banco.")
        
        carregar_usuarios()
        limpar_campos()
    except mysql.connector.Error as erro:
        messagebox.showerror("Erro", f"Erro na alteração do usuário. {erro}")
    finally:
        cursor.close()
        conn.close()
    
def confirmar_del():
    confirm = tk.Toplevel()
    confirm.title("Confirmar")
    confirm.geometry("300x100")

    text = tk.Label(confirm, text="Você deseja REALMENTE deletar o registro?")
    text.grid(row=0, column=0)

    def excluir_usuario():
        selecionado = tabela.selection()
        id = input_id.get()

        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um usuário para deletar.")
            return 

        try:
            conn = conectar()
            cursor = conn.cursor()

            sql = "DELETE FROM usuario WHERE id = %s"
            valor = (id,)

            cursor.execute(sql, valor)
            conn.commit()

            tabela.delete(selecionado)
            limpar_campos()

            messagebox.showinfo("Sucesso", "AEEE foi deletado no banco :D")
        except mysql.connector.Error as erro:
            messagebox.showinfo("Erro", f"Erro na deleção do usuário: \n{erro}")
        finally:
            cursor.close()
            conn.close()

    frame_btn = tk.Frame(confirm)
    frame_btn.grid(row=1, column=0, pady=10)

    y = tk.Button(frame_btn, text="Sim", width=10, command=excluir_usuario)
    y.grid(row=1, column=0)
    n = tk.Button(frame_btn, text="Nao", width=10, command=confirm.destroy)
    n.grid(row=1, column=1)

def limpar_campos():
    input_id.delete(0, tk.END)
    input_nome.delete(0, tk.END)
    input_email.delete(0, tk.END)
    input_end.delete(0, tk.END)



#janela
janela = tk.Tk()
janela.title("Crud User")
janela.geometry("600x600")

frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

tk.Label(frame_form, text="ID:").grid(row=0, column=0, pady=5, padx=5, sticky="e")
input_id = tk.Entry(frame_form, width=10)
input_id.grid(row=0, column=1, pady=5, padx=5)

tk.Label(frame_form, text="Nome:").grid(row=1, column=0, pady=5, padx=5, sticky="e")
input_nome = tk.Entry(frame_form, width=10)
input_nome.grid(row=1, column=1, pady=5, padx=5)

tk.Label(frame_form, text="Email:").grid(row=2, column=0, pady=5, padx=5, sticky="e")
input_email = tk.Entry(frame_form, width=10)
input_email.grid(row=2, column=1, pady=5, padx=5)

tk.Label(frame_form, text="Endereço:").grid(row=3, column=0, pady=5, padx=5, sticky="e")
input_end = tk.Entry(frame_form, width=10)
input_end.grid(row=3, column=1, pady=5, padx=5)

#botoesoseo
frame_button = tk.Frame(janela)
frame_button.pack(pady=10)

btn_novo = tk.Button(frame_button, text="Novo", width=10, command=novo_usuario)
btn_novo.grid(row=0, column=1, padx=5)
btn_editar = tk.Button(frame_button, text="Editar", width=10, command=editar_usuario)
btn_editar.grid(row=0, column=2, padx=5)
btn_excluir = tk.Button(frame_button, text="Excluir", width=10, command=confirmar_del)
btn_excluir.grid(row=0, column=3, padx=5)
btn_limpar = tk.Button(frame_button, text="Limpar", width=10, command=limpar_campos)
btn_limpar.grid(row=0, column=4, padx=5)
btn_salvar = tk.Button(frame_button, text="Salvar", width=10, command=salvar_dados)
btn_salvar.grid(row=0, column=5, padx=5)
btn_load = tk.Button(frame_button, text="Carregar SQL", width=10, command=carregar_usuarios)
btn_load.grid(row=0, column=6, padx=5)


#tabela

colunas = ("ID","NOME","EMAIL","ENDEREÇO")

tabela = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=170)

tabela.pack(fill="both", expand=True, padx=20, pady=20)
tabela.bind("<<TreeviewSelect>>", selecionar_usuario)


janela.mainloop()