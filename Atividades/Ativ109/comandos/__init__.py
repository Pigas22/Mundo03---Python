def dobro(valor, form=False):
  result = valor * 2
  return result if form is False else formatacao(result)


def metade(valor, form=False):
  result = valor / 2
  return result if not form else formatacao(result)


def aumenta(valor, taxa=10, form=False):
  result = valor + valor * (taxa / 100)
  return result, taxa if not form else formatacao(result, taxa)


def diminuir(valor, taxa=10, form=False):
  result = valor - valor * (taxa / 100)
  return result, taxa if not form else formatacao(result, taxa)


def formatacao(valor=0, taxa=0, moeda='R$'):
  """
  -> Função de formatação para Moedas.

  Valor: Valor inteiro ou float;
  Taxa: Para formatação de porcentagens;
  Moeda: Sigla de indentificação da moeda.
  """
  valor = f'{moeda}{valor:>8.2f}'.replace('.', ',')
  taxa = f'{taxa}%'
    
  return valor, taxa

