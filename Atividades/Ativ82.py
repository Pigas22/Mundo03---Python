valores = impares = pares = []

while True:
  valores.append(int(input('Digite um valor: ')))
  pergunta = str(input('Deseja continuar? [S/N] ')).upper().strip()
  if pergunta == 'N':
    break

for i, v in enumerate(valores):
  if v % 2 == 0:
    pares.append(v)
  elif v % 2 == 1:
    impares.append(v)

print(20 * '-=')
print(f'A lista completa é: {valores}')
print(f'A lista de apres é: {pares}')
print(f'A lista de impares é: {impares}')
