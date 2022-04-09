b = 0
c = 0
while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    b += 1

    a = c + num
    c = a

print("FIM")
print(f"Foram digitados: {b} numeros e a soma entre eles é: {c}")