frase = input("Digite uma frase: ").upper()

if frase.replace(" ", "") == frase.replace(" ", "")[::-1]:
    print("A frase é um Polindromo.")
else:
    print("A frase não é um Polindromo")