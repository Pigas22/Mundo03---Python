# Exercício 103 – Ficha do Jogador

def ficha(nome='Desconhecido', gols=''):
  if gols == '' or not gols.isnumeric():
    gols = 0

  return f'O jogador {nome} fez {gols} gols no campeonato: '

  
#Código Principal:
print(20 * '-=')
nome_jogador = str(input('Nome do Jogador: '))
quant_gols = str(input('Número de gols feitos: '))
print(ficha(nome_jogador, quant_gols))
