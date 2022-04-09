from random import randint
print('Oieee vamos brincar?? Vou pensar em um numero tenta adivinhar haha')
n = int(input('Digite um numero entre 1 e 5\n >>> '))
m = randint(0, 5)
if n == m:
    print('Nossa você acertou!')
else:
    print('Ihhh tenta de novo vai que acerta :)')
print(f"Numero escolhido: {m}")