import customtkinter as ctk

# Criar janela principal
tela = ctk.CTk(fg_color='darkgray') # fg_color: muda a cor de fundo da tela

# Configurar tamanho da tela
tela.geometry('350x400+800+200')
# travar abertura da janela
tela.resizable(width=False, height=False)
tela.title('Tela de login') # Altera o nome que aprece na janela
 
# Configurando estrutura da coluna
tela.grid_columnconfigure(0, weight=1)

# Criando as funções de validação
def validacao():
    email = box_usuario.get()
    senha = box_senha.get()
    if email == 'ed@ed.com' and senha == '123':
        msg = 'Dados validados com sucesso!'
        txt_saida.configure(text=msg, text_color='Olive')
    
    else:
        msg = 'Dados não conferem!\nVerifique e-mail e senha!'
        txt_saida.configure(text=msg, text_color='red')
    
tela.bind('<Return>',lambda event: validacao())

# Acrscentando os Widgets (elementos de tela).
txt_login = ctk.CTkLabel(tela, text='Login', font=('Calibri',30), text_color='white')
txt_login.grid(row=0, column=0, padx=20, pady=20)

txt_usuario = ctk.CTkLabel(tela, text='Usuário', font=('Calibri',22), text_color='white')
txt_usuario.grid(row=1, column=0, padx=50, pady=(10,0), sticky='w')

box_usuario = ctk.CTkEntry(tela, width=250, height=30, placeholder_text='Digite seu email...' )
box_usuario.grid(row=2, column=0, padx=20, pady=(5,10))

txt_senha = ctk.CTkLabel(tela, text='Senha', font=('Calibri',22), text_color='white')
txt_senha.grid(row=3, column=0, padx=50, pady=(10,0), sticky='w')

box_senha = ctk.CTkEntry(tela, width=250, height=30, placeholder_text='Digite sua senha...', show='*' )
box_senha.grid(row=4, column=0, padx=20, pady=(10,0))

btn_enviar = ctk.CTkButton(tela, text='Enviar', width=70, height=40, fg_color='white', text_color='black', command=validacao)
btn_enviar.grid(row=5, column=0, padx=20, pady=20)

txt_saida = ctk.CTkLabel(tela, text='', font=('Calibri', 20))
txt_saida.grid(row=6, column=0, padx=20, pady=20)




tela.mainloop()  # manter a janela em atividade.
