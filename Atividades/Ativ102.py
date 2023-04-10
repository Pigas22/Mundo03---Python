# Exercício 102 – Função para Fatorial


def fatorial(i, show=0):
  """
  
  -> A função 'fatorial()' irá realizar o cálculo fatorial de um número.

  i = número base do cálculo
  total = resultado
  num = multiplicador
  show = mostra o processo do cálculo caso seja 'True'
  """

  print(f'Fatorial de {i}: ')
  total = 1
  for num in range(1, i + 1):
    total *= num
    if show == True:
      if num < i:
        print(total, 'x ', end='')

      else:
        return total

    else:
      return total


# Código Pricipal:
print(20 * '-=')
print(fatorial(5, True))
help(fatorial)