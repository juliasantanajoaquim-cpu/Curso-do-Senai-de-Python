import customtkinter as ctk

# Criar janela principal
tela = ctk.CTk(fg_color='darkgray') # fg_color: muda a cor de fundo da tela

# Configurar tamanho da tela
tela.geometry('400x400+800+200')
# travar abertura da janela
tela.resizable(width=False, height=False)
tela.title('Calculadora IMC.') # Altera o nome que aprece na janela

# Função
def calcular_imc():
    try:
        nome = box_nome.get()
        peso = float(box_peso.get())
        altura = float(box_altura.get())
        imc = peso / altura**2
        msg = f'Bem vindo {nome}!\nO seu IMC é de {imc:0.2f}.'
        txt_resultado.configure(text=msg)
    except:
        txt_resultado.configure(text='Verifique os valores digitados!')



#configurar colunas
tela.grid_columnconfigure(0, weight=1)
tela.grid_columnconfigure(1, weight=1)


txt_titulo = ctk.CTkLabel(tela, text='CALCULADORA IMC', font=('Calibri',25))
txt_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

txt_nome = ctk.CTkLabel(tela, text='Nome:', font=('Calibri',15))
txt_nome.grid(row=1, column=0, padx=10, pady=10, sticky='e')

box_nome = ctk.CTkEntry(tela, width=200, height=30)
box_nome.grid(row=1, column=1, padx=10, pady=10, sticky='w')

txt_peso = ctk.CTkLabel(tela, text='Peso:', font=('Calibri',15))
txt_peso.grid(row=2, column=0, padx=10, pady=10, sticky='e')

box_peso = ctk.CTkEntry(tela, width=200, height=30)
box_peso.grid(row=2, column=1, padx=10, pady=10, sticky='w')

txt_altura = ctk.CTkLabel(tela, text='Altura:', font=('Calibri',15))
txt_altura.grid(row=3, column=0, padx=10, pady=10, sticky='e')

box_altura = ctk.CTkEntry(tela, width=200, height=30)
box_altura.grid(row=3, column=1, padx=10, pady=10, sticky='w')

btn_calcular = ctk.CTkButton(tela, text='CALCULAR', width=100, height=30, command=calcular_imc)
btn_calcular.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

txt_resultado = ctk.CTkLabel(tela, text='',font=('Calibri',25))
txt_resultado.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

tela.mainloop()
