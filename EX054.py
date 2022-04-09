from datetime import date
maior = 0
menor = 0
for c in range(7):
    idade = int(input("Digite a idade: "))
    idade = date.today().year - idade
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print("{} pessoas já são de maior e {} são de menor".format(maior, menor))
