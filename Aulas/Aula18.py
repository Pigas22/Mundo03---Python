pessoas = []
totalv = totalj = o

for c in range(0, 3):
  p = []
  p.append(str(input('Digite seu nome: ')))
  p.append(int(input('Digite sua idade: ')))
  print(20*'-=')
  pessoas.append(p[:])

for i in pessoas:
  if p[1] >= 19:
    print(f'{p[0]} é maior de idade.')
    totalv += 1
    
  else:
    print(f'{p[0]} é menor de idade')
    totalj += 1

print(f'Temos {totalv} maiores de idade e {totalj} menores de idade')
