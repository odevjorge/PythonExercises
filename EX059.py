from time import sleep
num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))
s = '-'*20
print(s)
sleep(1)

while True:
    print(" -> Selecione uma das opções abaixo")
    print(" [ 1 ] somar\n [ 2 ] multiplicar\n [ 3 ] maior\n [ 4 ] novos números\n [ 5 ] sair do programa")
    resp = str(input(" >> Digite a opção: "))
    while resp not in '12345':
        resp = str(input("Resposta errada tente novamente: "))

    if resp == "1":
        r = num1 + num2
    if resp == "2":
        r = num1 * num2
    if resp == "3":
        r = f"O menor é {sorted([num1, num2])[0]}, e o maior é {sorted([num1, num2])[1]}"
    if resp == "4":
        num1 = int(input("Digite o 1° numero: "))
        num2 = int(input("Digite o 2° numero: "))
        sleep(1)
    if resp == "5":
        print("Fim")
        break

    if resp in "123":
        print(f"{s}\nA resposta é: {r}\n{s}")
        sleep(1)