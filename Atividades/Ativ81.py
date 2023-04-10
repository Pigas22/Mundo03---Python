elementos = []

while True:
  elementos.append(int(input('Digite um número: ')))
  pergunta = str(input('Deseja continuar? [S/N] ')).upper().strip()
  if pergunta == 'N':
    break

print(20 * '-=')

print(f'Foram digitados {len(elementos)} valores')
elementos.sort(reverse=True)
print(f'Lista em ordem decrescente: {elementos}')

if 5 in elementos:
  print('O elemento "5", está presente na lista.')  
else:
  print('O elemento "5", não está na lista.')   
 