t = int(input("Digite a casa da tabuada: "))

print(f" Casa do >{t: ^3}<")
for c in range(1, 11):
    print(f"{t: ^3}x {c: >3} = {c*t: >3}")
