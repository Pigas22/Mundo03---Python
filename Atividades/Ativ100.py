# Exercício 100 – Funções para sortear e somar
from random import randint
from time import sleep


def linha():
  print(20 * '-=')

def sorteia(lista):
  linha()
  print('Sorteando 5 números, são eles: ', end='')
  for c in range(0, 5):
    num = randint(1, 10)
    sleep(0.5)
    print(num, end=' ', flush=True)
    lista.append(num)
  print('Fim')
  lista.sort()
  linha()
  

def soma_par(lista):
  linha()
  pares = 0
  for numeros in lista:
    if numeros % 2 == 0:
      pares += numeros

  sleep(0.5)
  print(f'A soma dos números pares em {lista}, é igual à: {pares}', flush=True)
  linha()


# Código Principal:
numbers = []
sorteia(numbers)
soma_par(numbers)
