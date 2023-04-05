# Aula 10 (Parte 1) - Funções

def linha():
  print(20 * '-=')


def mensagem(msg):
  linha()
  print(10 * ' ' + f'{msg}')
  linha()
  
# Código Principal:
linha()
print(10 * ' ' + ' ABACATE ')
linha()

mensagem(' ABACATE ')


# Parte Práticas:
def soma(a, b):
  print(f'A = {a}, B = {b}')
  s = a + b  
  print(s)


soma(7, 8)
soma(b=1, a=3)


# Tupla
def contador(*num):
  tam = len(num)
  print(f'Recebi os valores {num} e são ao todo: {tam}')

  for v in num:
    print(f'{v} ', end='')
  print()


contador(1, 5, 3)
contador(1, 20)
contador(7, 8, 9, 6, 4, 5)


# Lista
def dobra(lista):
  pos = 0
  while pos < len(lista):
    lista[pos] *= 2


valores = [1, 2, 8, 4, 60, 7, 6]
dobra(valores)
print(valores)


# Atividades:
# Ativ95.py até Ativ100.py
