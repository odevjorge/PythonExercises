from random import sample
n1 = input('Nome do 1° aluno: ')
n2 = input('Nome do 2° aluno: ')
n3 = input('Nome do 3° aluno: ')
n4 = input('Nome do 4° aluno: ')
print(f'A ordem de apresentação é: {sample([n1, n2, n3, n4], 4)}')
