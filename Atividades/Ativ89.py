# dados = [pessoa[nome, nota[0, 0], media]]
dados = list()

while True:
  aluno = str(input('Digite o nome do aluno: ')).strip()
  nota0 = float(input('1° Nota: '))
  nota1 = float(input('2° Nota: '))
  media = (nota0 + nota1) / 2
 
  dados.append([aluno, [nota0, nota1], media])
  
  continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()
  if continuar == 'N':
    break

  else:
    continue

print(20 * '-=')
print(5 * ' ' + 'BOLETIM ESCOLAR')
print(15 * '-=')
print(f' {"Núm.":<4}{"Aluno":<10}{"Média":>8}')
print(30 * '-')

for n, p in enumerate(dados):
  print(f' {n:<4}{p[0]:<10}{p[2]:>8.1f}')

print(30 * '-')

while True:
  pergunta2 = int(input('Mostrar as notas de qual aluno? (999 para interromper) '))

  if pergunta2 == 999:
    break
  
  else:
    print(f'As notas de {dados[pergunta2][0]} são {dados[pergunta2][1]}')
    print(20 * '-=')

print(20 * '-=')
print(13 * ' ' + 'VOLTE SEMPRE')
print(20 * '-=')

