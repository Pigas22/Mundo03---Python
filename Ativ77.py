tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
         'FUTURO')

for palavra in tupla:
  vogais_salvas = []

  for letra in range(0, len(palavra)):

    if palavra[letra] in 'AEIOU':
      vogais_salvas.append(palavra[letra])
      
    else:
      continue

  print(f'Na palavra {palavra} temos as vogais: ', end='')
  
  for vogais in range(0, len(vogais_salvas)):
    if vogais == (len(vogais_salvas) - 1):
      print(f'{vogais_salvas[vogais]}')

    else:
      print(f'{vogais_salvas[vogais]}', end=' ' )
    
