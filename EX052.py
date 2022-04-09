# NUMERO
num = int(input("Digite um numero: "))
a = 0
for c in range(1, num+1):
    if num % c == 0:
        print("\033[0:34m"+str(c), end=" ")
        a += 1
    else:
        print("\033[0:31m"+str(c), end=" ")
if a == 2:
    print("\033[0:0m"+"\nO numero {} é um numero primo!".format(num))

else:
    print("\033[0:0m"+"\nO numero {} não é um umero primo".format(num))


# LISTA DE NUMEROS
num = int(input("Digite um numero: "))
a = 0
lista = []
for i in range(1, num+1):
    for c in range(1, i+1):
        if i % c == 0:
            a += 1
    if a == 2:
        lista.append(i)
    a = 0

print("Numeros primos: ")
for c in lista:
    print(c, end=' ')