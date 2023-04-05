# Exercício 105 – Analisando e gerando Dicionários


def linha():
  print(20 * '-=')


def notas(*num, sit=False):
  """
  -> Função para obter um resumo das notas e da situação dos alunos.
  :num: recebe uma ou mais notas;
  :sit: Mostra a situação dos alunos caso for True;
  :return: A quantidade de notas, A maior e menor nota, A média das notas e A situação(opcional).
  """
  notas_aluno = {}

  notas_aluno['Quantidade de notas'] = len(num)
  notas_aluno['Maior Nota'] = max(num)
  notas_aluno['Menor Nota'] = min(num)
  notas_aluno['Média'] = float(f'{sum(num)/len(num):.2f}')

  if sit == True:
    if notas_aluno['Média'] >= 7:
      notas_aluno['Situação'] = 'BOM'

    elif notas_aluno['Média'] >= 5:
      notas_aluno['Situação'] = 'RAZOÁVEL'

    else:
      notas_aluno['Situação'] = 'PÉSSIMO'

  return notas_aluno


# Código Principal:
resp = notas(3.45, 7.5, 4.9, sit=True)
print(resp)

help(notas)
