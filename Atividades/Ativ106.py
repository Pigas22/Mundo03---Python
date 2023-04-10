# Exercício 106 – Interactive helping system in Python

from time import sleep

"""  
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
"""


def reset():
  print('\033[0;0m', end='')


def linha():
  print(20 * ('\033[1;36m' + '-='), flush=True)


def py_help():
  while True:
    linha()
    reset()
    comando = str(input('\033[7;32;40m' + 'Digite uma função/biblioteca para saber sobre sua características: ')).strip()
    reset()
    sleep(1)
    if comando == 'fim' or comando == 'FIM':
      print('\033[0;30;41m' + 'FINALIZANDO O PROGRAMA...', flush=True)
      reset()
      break
      
    else:
      print('\033[7;30;47m')
      help(comando)
      reset()


# Código Principal
py_help()
