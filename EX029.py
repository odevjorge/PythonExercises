v = int(input('Qual a velocidade do carro?\n>>> '))
if v >= 80:
    print(f'Você foi multado, valor da multa: R$\033[32m{((v-80)*7)}')
print('OK, pode ir')
