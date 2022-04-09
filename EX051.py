pt = int(input("Digite o 1° termo: "))
ra = int(input("Digite a RAZÃO: "))
print(f"Os 10 primeiros termos são:")
for c in range(1, 11):
    print(pt + (c - 1) * ra, end=' ')
