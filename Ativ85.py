# numeros[0] = pares
# numeros[1] = impares
numeros = [[], []]

for v in range(0, 7):
  valor = int(input(f'Digite o {v + 1}° valor: '))

  if valor % 2 == 0:
    numeros[0].append(valor)
    numeros[0].sort()
    
  elif valor % 2 == 1:
    numeros[1].append(valor)
    numeros[1].sort()

print(20 * '-=')
print(f'Os números pares digitados foram: {numeros[0]}')
print(f'Os números ímpares digitados foram: {numeros[1]}')
