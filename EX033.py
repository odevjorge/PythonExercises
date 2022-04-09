a = int(input('Digite um numero:\n >>> '))
b = int(input('Digite outro numero:\n >>> '))
c = int(input('Mais um numero:\n >>> '))

if a >= b and a >= c:
    print(f'{a} é o maior')
if b >= a and b >= c:
    print(f'{b} é o maior')
if c >= a and c >= b:
    print(f'{c} é o maior')

if a <= b and a <= c:
    print(f'{a} é o menor')
if b <= a and b <= c:
    print(f'{b} é o menor')
if c <= a and c <= b:
    print(f'{c} é o menor')
