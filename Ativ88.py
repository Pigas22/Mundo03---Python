import random, time

# Minha solução:
cartela = [0, 0, 0, 0, 0, 0]
cont = 0
num_repitido = []

print(20 * '-=')
print(14 * ' ', 'MEGA SENA')
print(20 * '-=')

num_jogos = int(input('Quantos jogos você deseja realizar? '))

for jogos in range(1, num_jogos + 1):
  for numeros in range(0, 6):
    num_sortido = random.randint(1, 61)
    
    if jogos == 0:
      cartela[cont] = num_sortido
    
    else:
      if num_sortido in cartela:
        num_sortido = random.randint(1, 61)
        
      cartela[cont] = num_sortido
        
    cont += 1

    for num in range(1, 61):
      contador_numeros = cartela.count(num)
      if contador_numeros > 1:
        num_repitido.append(jogos)

      else: 
        continue
  
    
  cartela.sort()
  time.sleep(1.5)
  print(f'Cartela {jogos}: {cartela}')
  cont = 0    

print(20 * '-=')
if len(num_repitido) == 1:
  print(f'Foi encontrado erros na cartela n° {num_repitido}')

elif len(num_repitido) > 1:
  print(f'Foram encontrados erros nas cartelas de n° {num_repitido}')

else:
  print('Não foi encontrado nenhum erro nos jogos.')
  print(6 * '-=', '< BOA SORTE >', 6 * '=-')


# Solução do Guanabara:
'''
lista = list()
jogos = list()
quant = int(input('Quantos jogos você deseja realizar? '))
tot = 1
while tot <= quant:  
  cont = 0
  while True:
    num = random.randint(1, 60)
    if num not in lista:
      lista.append(num)
      cont += 1
    if cont >= 6:
      break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  tot += 1

for i, l in enumerate(jogos):
  print(f'Jogo {i + 1}: {l}')
  time.sleep(1)
'''
