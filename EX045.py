from random import choice
jkp = input("Cara!! Pedra, Papel ou Tesoura??\n >>> ").upper()

minha_vez = choice(['PEDRA', 'PAPEL', 'TESOURA'])

if jkp[:2] == 'PE' and minha_vez[:2] == 'PA':
    print(f"Ihhhh ganhei! Escolhi {minha_vez}, PAPEL ganha da PEDRA")
elif jkp[:2] == 'PA' and minha_vez[:2] == 'TE':
    print(f"Ihhhh ganhei! Escolhi {minha_vez}, TESOURA ganha da PAPEL")
elif jkp[:2] == 'TE' and minha_vez[:2] == 'PE':
    print(f"Ihhhh ganhei! Escolhi {minha_vez}, PEDRA ganha da TESOURA")
elif jkp[:2] == minha_vez[:2]:
    print(f'Eitaaa! empate, vamos tentar de novo!')
elif jkp[:2] != ['PEDRA', 'PAPEL', 'TESOURA']:
    print("OPÇÃO INVALIDA TENTE NOVAMENTE!!")
else:
    print(f'Aff, escolhi {minha_vez} e {jkp} ganha de {minha_vez}!')