consumo = float(input('Insira o cosumo de WATTS do mês: '))

if consumo < 100:
    fatura = consumo * 0.65
elif consumo < 150:
    fatura = consumo * 0.70
elif consumo < 200:
    fatura = consumo * 0.75
else:
    fatura = consumo * 0.80

print(f'O valor da sua fatura é de R${fatura}.')
