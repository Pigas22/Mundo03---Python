# Exercício 99 – Função que descobre o maior
from time import sleep


def linha():
  print(20 * '-=')


def maior(*num):
  
  maior = 0
  print(f'Analisando um total de {len(num)} valores')
  print('  ', end='')
  for numero in num:
    sleep(0.5)
    print(numero, end=' ', flush=True)
    if numero > maior:
      maior = numero
  print('Fim')
  print(f'O maior valor infomado foi: {maior}')
  linha()

  
# Código Principal:
linha()
maior(1, 2, 3, 4, 5, 6, 7, 10, 9)
maior(1, 2)
maior(6)
maior()
