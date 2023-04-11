def dobro(valor):
  result = valor * 2
  return result


def metade(valor):
  result = valor / 2
  return result


def aumenta(valor, taxa=10):
  result = valor + valor * (taxa / 100)
  return result, taxa


def diminuir(valor, taxa=10):
  result = valor - valor * (taxa / 100)
  return result, taxa


def formatacao(valor=0, taxa=10, moeda='R$'):
  if valor != 0 and taxa != 0:
    valor = f'{moeda}{valor:>8.2f}'.replace('.', ',')
    taxa = f'{taxa}%'
    
    return valor, taxa

