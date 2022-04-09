num1 = 0
f = 0
for c in range(6):
    f += 1
    num = int(input(f"Digite o {f}° numero: "))
    if num % 2 == 0:
        num1 = num + num1

print(f"Resultado da soma dos numeros pares é: {num1}")