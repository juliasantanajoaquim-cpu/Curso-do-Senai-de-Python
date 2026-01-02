# espaço para as funções
def somar(num1, num2):
    res = num1 + num2
    print(f'A soma dos valores é {res}')

def subtrair(num1, num2):
    res = num1 - num2
    print(f'A subtração dos valores é {res}')

def multiplicar(num1, num2):
    res = num1 * num2
    print(f'A multiplicação dos valores é {res}')

def dividir(num1, num2):
    while True:
        if num2 == 0:
            print('O segundo valor não pode ser 0!')
            num2 = float(input('Digite o segundo valor: '))
        else:
            res = num1 / num2
            print(f'A divisão dos valores é {res}')
            break

#corpo do código
while True:
    print('***MINI CALCULADORA****') 
    print('\nQual operação deseja fazer')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - multiplicar')
    print('4 - Dividir')
    print('5 - Sair')
    op = input('Digite a operação desejada: ')
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundoo valor: '))
    if op == '5':
        print('Obrigado, Volte sempre!!!')
        break
    elif op == '1':
        somar(num1, num2)
    elif op == '2':
        subtrair(num1, num2)
    elif op == '3':
        multiplicar(num1, num2)
    elif op == '4':
        dividir(num1, num2)

  
