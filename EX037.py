num = int(input("Digite o valor a ser convertido:\n >>> "))
print("""Agora digite qual sistema de numeração você deseja:
 [ 1 ] - BINARIO
 [ 2 ] - OCTAL
 [ 3 ] - HEXADECIMAL
      """)

opc = int(input("Digite a opção desejada:\n >>> "))

if opc == 1:
    print(f"O valor decimal: {num}, em BINARIO é: {bin(num)[2:]}")
elif opc == 2:
    print(f'O valor deciaml: {num}, em OCTAL é: {oct(num)[2:]}')
else:
    print(f'O valor decimal: {num}, em HEXADECIMAL é: {hex(num)[2:]}')
