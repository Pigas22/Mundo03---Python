'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
valores.sort()

print(f'Informações retiradas da Lista: {valores}')

for v in valores:
  print(v)

for c, v in enumerate(valores):
  print(f'Na posição {c + 1}, encontramos o valor: {v}')

abacate = []
print(f'Lista -> Abacate = {abacate}')
for cont in range(0, 5):
  abacate.append(int(input('Digite um valor para ser adicionado a lista: ')))

for p, num in enumerate(abacate):
  print(f'Na posição {p}°, temos o valor: {num}')

'''  

# Copia de listas

a = [1, 2, 3, 4, 5]
b = a[:]
b.append(6)

print(f'No conjunto A, temos: {a}')
print(f'No conjunto B, temos: {b}')
