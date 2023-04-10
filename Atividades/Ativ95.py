dados = list()
jogador = dict()
gols_marcados = list()
total_gols = 0

while True:
  jogador['Nome'] = str(input(' - Jogador: ')).strip().capitalize()
  partida = int(input(f' - Quantas partidas {jogador["Nome"]} jogou? '))
  
  for p in range(0, partida):
    gols_marcados.append(int(input(f'    - Quantos gols ele fez na partida {p}: ')))
    total_gols += gols_marcados[p]

  jogador['Gols'] = gols_marcados[:]
  jogador['Total'] = total_gols
  dados.append(jogador.copy())
  gols_marcados.clear()
  total_gols = 0
  
  continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
  while continuar not in 'SN':
    print('ERRO: Por favor, Digite apenas S ou N.')
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

  if continuar == 'N':
    break

  else:
    continue

print(20 * '-=')
print(f'{"Núm.":<5}|{"Nome":<10}|{"Gols":<19}|{"Total":>4}')

for p, j in enumerate(dados):
  print(f' {p:<5}{j["Nome"]:<11}{str(j["Gols"]):<19}{j["Total"]:>5}')

print(20 * '-=')

while True:
  mostrar_dados = int(input('Mostrar os dados de qual jogador? (999 interrompe) '))
  print(20 * '-=')
  if mostrar_dados == 999:
    break

  elif mostrar_dados > len(dados):
    print('ERRO: Não possui nenhum jogador com esse número.')

  else:
    print(f' -- LEVANTAMENTO DO JOGADOR ({dados[mostrar_dados]["Nome"]}):')
    for c in range(0, len(dados[mostrar_dados]["Gols"])):
      print(f'    - No jogo {c}, ele fez: {dados[mostrar_dados]["Gols"][c]} gols')

  print(20 * '-=')
print(' -- VOLTE SEMPRE -- ')
