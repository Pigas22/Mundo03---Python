valores = []
cont = 0

while True:
  num = int(input('Digite um valor: '))

  if num in valores:
    print('Número repitido, não adicionado...')

  else:
    valores.append(num)
    print('Valor adicionado com sucesso...')

  continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()
  if continuar == 'N':
    break

  elif continuar == 'S':
    continue

  else:
    print('Não foi possível compreender, encerrando...')
    break

print(20 * '-=')
valores.sort()
print(f'Você digitou os valores: {valores}')
