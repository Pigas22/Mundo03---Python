def leiaInt():
  while True:
    try:
      num_int = int(input('Digite um número inteiro: '))

    except KeyboardInterrupt:
      print('\033[1;31m' + 'ERROR: O usuário preferiu não informar o valor.' + '\033[0;0m')
      return 0

    except (ValueError, TypeError):
      print('\033[1;31m' + 'ERROR: O número digitado não é um valor inteiro' + '\033[0;0m')
      continue
      
    else:
      return num_int


def leiaFloat():
  while True:
    try:
      num_real = float(input('Digite um número real: '))

    except KeyboardInterrupt:
      print('\033[1;31m' + 'ERROR: O usuário preferiu não informar o valor.' + '\033[0;0m')
      return 0

      
    except (ValueError, TypeError):
      print('\033[1;31m' + 'ERROR: O número digitado não é um valor real' + '\033[0;0m')
      continue
    
    else:
      return num_real

      