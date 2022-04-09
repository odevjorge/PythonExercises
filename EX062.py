pt = int(input("Digite o primeiro termo: "))
rz = int(input("Digite a razão: "))
a = pt

a2 = 10
c = 1
b = 1
while c != 0:
    print(a, "-> " if c != a2 else f"", end="")
    c += 1
    a += rz

    if c == a2 + 1:
        b = int(input("\nQuantos termos a mais quer ver? "))
    if b == 0:
        c = 0
    elif c == a2 + 1:
        a2 += b