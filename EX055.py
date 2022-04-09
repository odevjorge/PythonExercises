maior = 0
menor = 0
lista = []
for c in range(5):
    lista.append(float(input("Digite os pesos: ")))

print("O menor valor é: {}, o maior é: {}".format(sorted(lista)[0], sorted(lista)[-1]))