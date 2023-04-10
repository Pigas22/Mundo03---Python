pessoas = []
pesado = []
leve = []
cont = maior = menor = 0

while True:
  dados = []
  dados.append(str(input('Nome: ')).capitalize().strip())
  dados.append(float(input('Peso: ')))
  pessoas.append(dados[:])

  if cont == 0:
    maior = menor = dados[1]
    pesado.append(dados[:])
    leve.append(dados[:])

  else:
    if dados[1] > maior:
      pesado = []
      pesado.append(dados[:])
      maior = dados[1]

    elif dados[1] == maior:
      pesado.append(dados[:])

    elif dados[1] == menor:
      leve.append(dados[:])

    elif dados[1] < menor:
      leve = []
      leve.append(dados[:])
      menor = dados[1]
         
      
  continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
  if continuar == 'N':
    break
  
  else:
    cont += 1
    continue

print(f'Foram cadastradas {len(pessoas)} pessoas no programa.')

if len(pesado) == 1:
  print(f'O maior peso foi de {pesado[0][1]:.2f}Kg, peso de: {pesado[0][0]}')
  
elif len(pesado) > 1:
  print(f'Os maiores pesos foram de {pesado[0][1]:.2f}Kg, peso de', end=' ')
  for people in range(0, len(pesado)):
    print(pesado[people][0])
    
if len(leve) > 1:
  print(f'Os menores pesos foram de {leve[0][1]:.2f}Kg, peso de', end=' ')  
  for people in range(0, len(leve)):
    print(leve[people][0])
  
elif len(leve) == 1:
  print(f'O menor peso foi de {leve[0][1]:.2f}Kg, peso de: {leve[0][0]}')

print(leve)
print(pesado)
