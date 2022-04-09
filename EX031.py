k = float(input('Qual a quantidade de Km?\n>>> '))
if k <= 200:
    print(f'O valor sera: R$\033[32m{k*0.50:.2f}')
else:
    print(f'O valor sera: R$\033[32m{k*0.45:.2f}')
