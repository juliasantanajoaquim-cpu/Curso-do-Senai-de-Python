compra = float(input('Digite o valor da compra: '))
distância = int(input('Digite a distância de entrega (km): '))

if compra >= 200:
    frete = 0

elif distância <= 50:
    frete = distância * 1

elif distância > 50:
    frete = distância * 1.5

print(f'Valor do frete: R${frete}')
print(f'Valor total da entrega: R$ {compra + frete}')
