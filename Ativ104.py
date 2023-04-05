# Exercício 104 – Validando entrada de dados em Python

def leiaint(msg):
  while True:
    msg = str(input('Digite um número: '))
    if not msg.isnumeric():
      print('ERROR: digite um número válido')
    
    else:
      break
      
  return int(msg)


# Código Principal: 
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

