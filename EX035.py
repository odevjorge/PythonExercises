a = float(input('Digite o valo da primeira reta do triangulo:\n >>> '))
b = float(input('Digite o valor da segunda reta do triangulo:\n >>> '))
c = float(input('Digite o valor da terceira teta do triangulo:\n >>> '))

if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('É um triangulo!')
else:
    print('Não é um triangulo')
