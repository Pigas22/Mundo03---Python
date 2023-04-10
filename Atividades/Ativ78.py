pos_maior = []
pos_menor = []
num = []
maior = 0
menor = 0

for x in range(0, 5):
  abacate = int(input(f'Digite um valor para a posição {x}: '))
  num.append(abacate)
  if x == 0:
    maior = num[x]
    menor = num[x]

  else:
    if num[x] > maior:
      maior = num[x]

    elif num[x] < menor:
      menor = num[x]

for y in range(0, len(num)):
  if num[y] == maior:
    pos_maior.append(y)
  
  elif num[y] == menor:
    pos_menor.append(y)

  else:
    continue  

print(20 * '-=')

print(f'Você digitou os valores: {num}')

print(f'O maior número digitado foi {maior}, nas posições: ', end='')
for numeros in range(0, len(pos_maior)):
  print(f'{pos_maior[numeros]};', end=' ')

print(f'\nO menor número digitado foi {menor}, nas posições: ', end='')
for numeros in range(0, len(pos_menor)):
  print(f'{pos_menor[numeros]};', end=' ')
print('')
