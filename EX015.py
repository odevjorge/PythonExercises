d = int(input('Quantos dias ficou com o carro?\n >>> '))
km = float(input('Qual a quantidade de KM percorrido:\n >>> '))
print(f'A diaria de R$60 + R$0.15 por Km fica por R$\033[32m{((km * 0.15) + (60 * d)):.2f}')
