nomes=[]
# Criando a lista interativa
while True:
    nome = input('Insira um nome ou aperte "Q" para parar: ' )
    if nome =='Q' or nome == 'q':
        break
    else:
        nomes.append(nome)

# Gerando uma lista ordenada
contador = 1
print('Lista atualizada:')
for i in nomes:
    print(f'{contador}: {i}')
    contador +=1

# Alteração dos nomes
while True:
    op = input('Deseja alterar algum nome? Digite S/N: ')
    if op == 'N' or op=='n':
        contador = 1
        print('Lista final de nomes:')
        for i in nomes:
            print(f'{contador}: {i}')
            contador +=1
        break
    else:
        indice = int(input('Qual o numero da lista que quer alterar: '))
        novo_nome = input('Digite o nome para substituir: ')
        nomes[indice - 1]=novo_nome
        contador = 1
        print('Lista atualizada:')
        for i in nomes:
            print(f'{contador}: {i}')
            contador +=1
