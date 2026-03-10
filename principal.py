import tkinter as tk

def abrir_janela_novo_usuario():
    nova_janela = tk.Toplevel()
    nova_janela.title("Novo Usuario")
    nova_janela.geometry("300x300")

    tk.Label(nova_janela, text="Nome: ").grid(row=0, column=0, padx=10, pady=10)
    input_nome = tk.Entry(nova_janela, width=35)
    input_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(nova_janela, text="Email: ").grid(row=1, column=0, padx=10, pady=10)
    input_email = tk.Entry(nova_janela, width=35)
    input_email.grid(row=1, column=1, padx=10, pady=10)

    def salvar_usuario():
        nome = input_nome.get()
        email = input_email.get()

        lista_usuario.insert(tk.END, f"{nome} - {email}")
        nova_janela.destroy()

    btn_salvar = tk.Button(nova_janela, text="Salvar", command=salvar_usuario)
    btn_salvar.grid(row=2, column=1, padx=10, sticky="e")



janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("600x600")

menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Sair", command=janela.quit)

menu_usuario = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Usuario", command=menu_usuario)
menu_usuario.add_command(label="Cadastro", command=janela.quit)
menu_usuario.add_command(label="Excluir", command=janela.quit)
menu_usuario.add_command(label="Alterar", command=janela.quit)

btn_cad = tk.Button(janela, text="Novo Cadastro", command=abrir_janela_novo_usuario)
btn_cad.grid(row=0, column=0, padx=10, pady=10, sticky="e")

lista_usuario = tk.Listbox(janela, width=60)
lista_usuario.grid(row=1, column=0, padx=10, pady=10, sticky="e")

janela.mainloop()