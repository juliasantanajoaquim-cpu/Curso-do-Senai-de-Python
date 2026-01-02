print('\n----BEM VINDO A PIZZARIA----')
print('\nEscolha o sabor da pizza:')
print('1 - Calabresa')
print('2 - Napolitana')
print('3 - Portuguesa')
print('4 - Marguerita')

pizza = int(input('\nDigite o numero do sabor da pizza: '))
refri = input('\nGostaria de refrigerante? Digite S ou N:')

if pizza == 1:
    pizza = 42.50
elif pizza == 2:
    pizza = 35.50
elif pizza == 3:
    pizza = 36.50
elif pizza == 4:
    pizza = 39.80

if refri == 'S':
    refri = 8.90
else:
    refri = 0

print(f'O seu pedido fica no total de R${pizza + refri}')
