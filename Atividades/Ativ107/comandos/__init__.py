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