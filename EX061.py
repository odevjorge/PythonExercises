pt = int(input("Digite o primeiro termo: "))
rz = int(input("Digite a razão: "))
a = pt
c = 1
while c != 11:
    print(a, "-> " if c != 10 else "", end="")
    a += rz
    c += 1