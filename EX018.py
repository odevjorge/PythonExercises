from math import sin, cos, tan, radians
ang = float(input('Qual é o angulo?\n >>> '))
print(f'O seno vale: {sin(radians(ang)):.2f}\n'
      f'O cosceno vale: {cos(radians(ang)):.2f}\n'
      f'A tangente vale: {tan(radians(ang)):.2f}')

