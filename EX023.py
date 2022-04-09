num = int(input('Digite um numero:\n >>> '))
nume = str(f'{num:>4}')
print(f"Unidade: {nume[3]}\n"
      f"Dezena : {nume[2]}\n"
      f"Centena: {nume[1]}\n"
      f"Milhar : {nume[0]}\n")
