aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))

if aluno['média'] > 7:
  aluno['situação'] = 'Aprovado'

elif 5 <= aluno['média'] < 7: 
  aluno['situação'] = 'Recuperação'
  
else:
  aluno['situação'] = 'Reprovado'

print(20 * '-=')
for k, v in aluno.items():
  if k == 'nome':
    print(f' - O {k} é: {v}')

  else:
    print(f' - A {k} é: {v}')
