n = str(input('Digite um numero\n >>> '))
b = len(n)
c = int(n[b-1])
if c in [2, 4, 6, 8, 0]:
    print('Numero par')
else:
    print('Numero Impar')
