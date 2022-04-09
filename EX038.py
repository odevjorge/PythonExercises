n1 = int(input("Digite o primeiro numero:\n >>> "))
n2 = int(input("Digite o segundo numero\n >>> "))

if n1 > n2:
    print(f"O PRIMEIRO é o maior!")
elif n1 < n2:
    print(f"O SEGUNDO é o maior!")
else:
    print(f"Não tem numero maior! Os dois tem o mesmo valor!")
