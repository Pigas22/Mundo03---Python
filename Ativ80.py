valores = []

for x in range(0, 5):
  num = int(input('Digite um valor: '))

  if x == 0 or num > valores[-1]:
    valores.append(num)
    print('Número adicionado no final da lista.')
    
  else:
    pos = 0
    while pos < len(valores):
      if num <= valores[pos]:
        valores.insert(pos, num)
        print(f'Número adicionado na posição {pos} da lista.')
        break
      pos += 1

print(20 * '-=')

print(f'Os valores digitados em ordem foram: {valores}')
