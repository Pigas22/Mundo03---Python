# Exercício 98 – Função de Contador
from time import sleep


def linha():
  print(20 * '-=')


def contador(i, f, p):
  if p == 0 or p == '':
    p = 1

  p = int(p)
  
  if i > f:
    if p > 0:
      passo_novo = p * -1
      if p != passo_novo:
        p = passo_novo
    f -= 1

    print(f'Contagem de {i} até {f + 1}, de {p} em {p}.')
    
  elif i < f:
    f += 1
    print(f'Contagem de {i} até {f - 1}, de {p} em {p}.')

  print('  ', end='')
  for c in range(i, f, p):
    sleep(0.5)
    print(c, end=' ', flush=True)
  print('Fim', flush=True)


# Código Principal
linha()

contador(1, 10, 1)

linha()

contador(10, 0, -2)

linha()

print(4 * ' ' + 'Contagem Personalizada')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = str(input('Passo: '))

linha()

contador(inicio, fim, passo)

linha()
