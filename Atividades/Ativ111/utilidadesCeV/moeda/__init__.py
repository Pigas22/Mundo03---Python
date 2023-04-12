def linha():
  """
  -> Função para criar um linha de separação com 40 caracteres.
  """
  print(20 * '-=')



def dobro(valor, form=False):
  """
  -> Função para dobrar o valor recebido.

  Param. [valor] = Valor base à ser dobrado;
  Param. [form] = Em caso True, haverá formatação do resultado.
  """
  result = valor * 2
  return result if form is False else formatacao(result)


def metade(valor, form=False):
  """
  -> Função para dividir um valor pela metade.

  Param. [valor] = Valor base ã ser dividido;
  Param. [form] = Em caso True, haverá formatação do resultado.
  """
  result = valor / 2
  return result if not form else formatacao(result)


def aumentar(valor, taxa=10, form=False):
  """
  -> Função para aumentar o valor em porcentagem.

  Param. [valor] = Valor à ser alterado;
  Param. [aumento] = Porcentagem pela qual alterará o valor.
  Param. [form] = Em caso True, haverá formatação do resultado
  """
  result = valor + valor * (taxa / 100)
  return result if not form else formatacao(result)


def diminuir(valor, taxa=10, form=False):
  """
  -> Função para diminuir o valor em porcentagem.

  Param. [valor] = Valor à ser alterado;
  Param. [desconto] = Porcentagem pela qual alterará o valor.
  Param. [form] = Em caso True, haverá formatação do resultado
  """
  result = valor - valor * (taxa / 100)
  return result if not form else formatacao(result)


def formatacao(valor=0, moeda='R$'):
  """
  -> Função de formatação para Moedas.

  Param. [valor] = Valor inteiro ou float;
  Param. [moeda] = Sigla de indentificação da moeda.
  """
  valor = f'{moeda}{valor:>10.2f}'.replace('.', ',')
    
  return valor


def resumo(valor, aumento=0, desconto=0):
  """
  -> Função para mostrar um resumo geral de um valor, utilizando outras Funções.
  -> Essa Função utilizasse de outras 6 funções, são elas: linha(), dobro(), metade(), diminuir(), aumentar() e formatacao()

  Param. [valor] = Valor à ser alterado;
  Param. [aumento] = Porcentagem pela qual aumentará o valor;
  Param. [desconto] = Porcentagem pela qual diminuirá o valor.
  """
  linha()
  print(f'{"RESUMO TOTAL":^40}')
  linha()

  print(f' - Preço Analizado: {formatacao(valor)}')
  
  print(f' - Dobro do Preço:  {dobro(valor, form=True)}')
  
  print(f' - Metade do Preço: {metade(valor, form=True)}')
  
  print(f' - {aumento}% de Aumento:  {aumentar(valor, aumento, form=True)}')

  print(f' - {desconto}% de Desconto: {diminuir(valor, desconto, form=True)}')

  linha()

