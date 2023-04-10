dados = {}

dados['Nome'] = str(input('Nome: '))
dados['Ano'] = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('CTPS: (0 não tem) '))

if dados['CTPS'] != 0:
  dados['Contratação'] = int(input('Ano de contratação: '))
  dados['Salário'] = float(input('Salário: R$ '))
  dados['Aposentadoria'] = (dados['Contratação'] + 35) - dados['Ano']

  print(20 * '-=')
  for k, v in dados.items():
    if v == dados['Salário']:
      print(f' - {k}: R$ {v}')
  
    elif v == dados['Aposentadoria']:
      print(f' - {k}: {v} anos')
  
    else:
      print(f' - {k}: {v}')

else:
  print(20 * '-=')
  for k, v in dados.items():
    print(f' - {k}: {v}')
