s = int(input('Qual salario do funcionario?\n>>> '))
if s >= 1250:
    print(f'O novo salario do funcionario é: R$\033[32m{s + (s * 10 / 100):.2f}')
else:
    print(f'O novo salario do funcionario é: R$\033[32m{s + (s * 15 / 100):.2f}')
