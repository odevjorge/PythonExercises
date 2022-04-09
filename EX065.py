c = 0
b = 0
lista = []
while True:
    num = int(input("Digite um numero: "))

    a = num + c
    c = a

    lista.append(num)

    con = str(input("Quer continuar [S/N]: ")).upper()[0]
    if con == "N":
        break

lista = sorted(lista)
print(f"A media é: {c/len(lista):.2f}\nO maior numero digitado foi: {lista[-1]} o menor {lista[0]}")


