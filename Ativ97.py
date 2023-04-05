# Exercício 97 – Um print especial

def escreva(msg):
  tamanho = len(msg) + 4
  print(tamanho * '=')
  print(f'  {msg}')
  print(tamanho * '=')


# Programa Principal:
while True:
  texto = str(input('Escreva uma mensagem: '))
  escreva(texto)

  pergunta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
  if pergunta not in 'SN':
    print('ERRO: Por favor, digite apenas S ou N.')
    pergunta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
  else:
    if pergunta == 'S':
      continue

    else:
      print(' -=-= VOLTE SEMPRE =-=-')
      break
