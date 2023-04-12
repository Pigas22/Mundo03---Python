def leia_dinheiro():
  while True:
    valor = str(input('Digite um preço: R$ '))

    for carac in valor:
      if carac in '1234567890,.':
        parametro = True
        continue
      else:
        parametro = False
        break

    if valor == '':
      parametro = False
    
    if parametro:
      if ',' in valor:
        valor = valor.replace(',', '.').strip()
        
      result = float(valor)
      break
    
    else:
      print('\033[1;31m' + f'-> [{valor}] é um Valor Inválido' + '\033[0;0m')

  return result

