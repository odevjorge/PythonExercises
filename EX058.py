from random import randint

num = randint(1, 10)

vez = 1

resp = int(input("Digite um valor entre 0 e 10: "))
while resp != num:
    vez = vez + 1
    resp = int(input("Tente novamente: "))

print(f"VOCÊ ACERTOU! Precisou de {vez} tentativas")