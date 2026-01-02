import os
import time

agenda = {}

def inserir():
    while True:
        nome = input('Digite o nome a inserir: ')
        
        if nome in agenda.keys():
            os.system('cls')
            print('\nEsse nome já está na lista de contatos!')

        else:
            telefone = input('Digite o telefone a inserir: ')
            agenda[nome]=telefone
            os.system('cls')
            print('Dados inseridos com sucesso!')
            time.sleep(2)
            break


def imprimir():
    if agenda == {}:
        print('Sua agenda não possui contatos!')

    else:
        cont = 1
        print('LISTA DE CONTATOS:')
        for i, j in agenda.items():
            print(f'{cont} - {i} : {j}')
            cont += 1

def alteração():
    while True:
        nome = input('\nDigite o contato a ser alterado: ')
        telefone = input('Digite o novo número: ')
        if nome in agenda.keys():
            agenda[nome] = telefone
            break
        else:
            print('Digite o nome corretamente:')

def deletar():
    while True:
        nome = input('Digite o nome do contato a remover: ')
        if nome in agenda.keys():
            agenda.pop(nome)
            break
        else:
            print('Este contato não existe!')



# Criar o menu

while True:
    os.system('cls')
    print('****AGENDA****')
    print('\nEscolha uma opção:')
    print('1 - Inserir um contato: ')
    print('2 - Imprimir lista de contatos:')
    print('3 - Alterar um número;')
    print('4 - Deletar contato')
    print('5 - Sair da aplicação;')

    op = input('\nDigite a número da opção: ')

    if op == '5':
        print('Obrigado por usar nosso APP!')
        break
    
    elif op =='1':
        os.system('cls')
        inserir()

    elif op == '2':
        os.system('cls')
        imprimir()
        time.sleep(3)

    elif op =='3':
        os.system('cls')
        imprimir()
        alteração()

    elif op == '4':
        os.system('cls')
        deletar()
