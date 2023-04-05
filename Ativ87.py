matriz = [
  [0, 0, 0], 
  [0, 0, 0], 
  [0, 0, 0]
]
soma_pares = soma_3coluna  = maior_2linha = 0

for l in range(0, 3):
  for c in range(0, 3):
    num = int(input(f'Digite um valor para [{l}, {c}]: '))
    matriz[l][c] = num
    
    if num % 2 == 0:
      soma_pares += num
    
    if c == 2:
      soma_3coluna += num

    if l == 1:
      if num > maior_2linha:
        maior_2linha = num

print(24 * '-=')

for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matriz[l][c]:^5}]', end='')
  print()

print(24 * '-=')
    
print(f'A soma de todos os números pares é: {soma_pares}')

print(f'A soma de todos os números da 3° coluna é: {soma_3coluna}')

print(f'O maior número da 2° linha é: {maior_2linha}')
