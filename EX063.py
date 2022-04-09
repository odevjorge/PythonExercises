num = int(input("Digite um numero: "))

c = 0
i = 1
b = 1
while True:
    b += 1
    if b == num:
        print(c)
        break
    print(c, end=" -> ")
    a = c + i
    c = i
    i = a

