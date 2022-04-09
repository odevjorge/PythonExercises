soma = 0
a = 0
for c in range(3, 501, 2):
    if c % 3 == 0:
        soma += c
        a += 1

print("A soma dos {} numeros é: {}".format(a, soma))