a = float(input("Digite o valor da primeira reta: "))
b = float(input("Digite o valor da segunda reta: "))
c = float(input("Digite o valor da terceira rera: "))

nt = "Não é possivel formar um triangulo!"

"""
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    if a == b == c:
        tipo = "Equilatero"
    elif a == b or b == c or a == c:
        tipo = "Isosceles"
    else:
        tipo = "Escaleno"
    print(f'É possivel formar um triangulo e ele é: {tipo}')

else:
    print("Não é possivel formar um triangulo!")
"""

if (b - c) < a < (b + c):
    if (a - c) < b < (a + c):
        if (a - b) < c < (a + b):
            if a == b == c:
                tipo = "Equilatero"
            elif a == b or b == c or a == c:
                tipo = "Isosceles"
            else:
                tipo = "Escaleno"
            print(f'É possivel formar um triangulo e ele é: {tipo}')
        else:
            print(nt)
    else:
        print(nt)
else:
    print(nt)

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
