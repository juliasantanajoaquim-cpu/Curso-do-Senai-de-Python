compra = float(input('Digite o valor da sua compra: '))

if compra < 100:
    desconto = 0

elif compra < 300:
    desconto = compra * 0.1
elif compra < 400:
    desconto = compra * 0.15
elif compra >= 500 :
    desconto = compra * 0.2

total = compra - desconto

print(f'Desconto R${desconto}')
print(f'Total a pagar R${total}')
