jogador = dict()
quant_gols = list()
total_gols = 0

jogador['Nome'] = str(input('Nome: '))
quant = int(input(f'Quantos jogos {jogador["Nome"]} jogou? '))

for partida in range(0, quant):
  gols = int(input(f' - Quantos gols na partida {partida}: '))
  total_gols += gols
  quant_gols.append(gols)

jogador['Gols'] = quant_gols
jogador['Total de gols'] = total_gols

print(20 * '-=')
for k, v in jogador.items():
  print(f' - {k}: {v}')
print(20 * '-=')

print(f'O jogador {jogador["Nome"]} jogou {quant} partidas.')
for c in range(0, quant):
  print(f' - Na partida {c}, fez {quant_gols[c]} gols.')
print(f'Foi um total de {total_gols} gols.')
