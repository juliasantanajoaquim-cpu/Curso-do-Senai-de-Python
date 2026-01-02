import customtkinter as ctk
import sqlite3 as sql

# Função para coletar




# Codigo para interface de cadastro
janela = ctk.CTk()
janela.geometry('450x400+800+250')
janela.title('Cadastro cliente')

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)

txt_titulo = ctk.CTkLabel(janela, text='Cadastro cliente', font=('Helvetica', 26))
txt_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

txt_nome = ctk.CTkLabel(janela, text='Nome:', font=('Helvetica', 18),)
txt_nome.grid(row=1, column=0, padx=10, pady=10)

box_nome = ctk.CTkEntry(janela, width=200)
box_nome.grid(row=1, column=1, padx=10, pady=10)

txt_nascimento = ctk.CTkLabel(janela, text='Nascimento:', font=('Helvetica', 18))
txt_nascimento.grid(row=2, column=0, padx=10, pady=10)

box_nascimento = ctk.CTkEntry(janela, width=200)
box_nascimento.grid(row=2, column=1, padx=10, pady=10)

txt_cpf = ctk.CTkLabel(janela, text='CPF:', font=('Helvetica', 18))
txt_cpf.grid(row=3, column=0, padx=10, pady=10)

box_cpf = ctk.CTkEntry(janela, width=200)
box_cpf.grid(row=3, column=1, padx=10, pady=10)

btn_enviar = ctk.CTkButton(janela, text='Enviar')
btn_enviar.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

txt_saida = ctk.CTkLabel(janela, text='', font=('Helvetica', 18))
txt_saida.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

janela.mainloop()
