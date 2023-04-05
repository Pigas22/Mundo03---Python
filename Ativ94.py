dados = list()
pessoa = dict()
mulheres = list()
acima_idade = list()
cont = media = 0

while True:
  pessoa['Nome'] = str(input(' - Nome: ')).capitalize().strip()
  pessoa['Sexo'] = str(input(' - Sexo: [M/F] ')).strip().upper()[0]
  
  while pessoa['Sexo'] not in 'MF':
    print('ERRO: Por favor, digite apenas M ou F.')
    pessoa['Sexo'] = str(input(' - Sexo: [M/F] ')).strip().upper()[0]

  if pessoa['Sexo'] == 'F':
    mulheres.append(pessoa['Nome'])
    
  pessoa['Idade'] = int(input(' - Idade: '))
  
  media += pessoa['Idade']
  dados.append(pessoa.copy())
  
  cont += 1
  
  pergunta = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
  while pergunta not in 'SN':
    print('ERRO: Por favor, digite apenas S ou N.')
    pergunta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
  
  else:
    if pergunta == 'N':
      break

    else:
      continue

print(20 * '-=')

if cont > 1:
  print(f'A) Foram cadastradas {cont} pessoas')

else:
  print(f'A) Foi cadastrada {cont} pessoa')

media /= cont
print(f'B) A média de idade é: {int(media)} anos')

if len(mulheres) > 1:
  print('C) As mulheres cadastradas foram: ', end='')
  for p, mulher in enumerate(mulheres):
    if p == len(mulheres) - 1:
      print(f'{mulher}.')

    else: 
      print(f'{mulher}, ', end='')
    
else:
  print(f'C) A única mulher cadastrada foi: {mulheres[0]}')


for x in range(0, cont):
  if dados[x]['Idade'] > media:
    acima_idade.append(dados[x]['Nome'])
  else:
    continue

if len(acima_idade) > 1:
  print('D) Pessoas acima da Idade Média: ', end='')
  for p, pessoas in enumerate(acima_idade):
    if p == len(acima_idade) - 1:
      print(f'{pessoas}.')

    else: 
      print(f'{pessoas}, ', end='')

else:
  print(f'D) A única pessoa acima da Idade Média foi: {acima_idade[0]}.')
