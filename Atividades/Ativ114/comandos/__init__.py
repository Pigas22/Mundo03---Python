def verifica_site():
  import urllib
  import urllib.request

  link = str(input('Digite a URL do site que deseja verificar: \n'))
  print(20 * '-=')
  try:
    urllib.request.urlopen(str(link))
  
  except urllib.error.URLError:
    print('\033[1;31' + 'O site está indisponível.')

  except Exception as error:
    print('\033[1;31m' + 'Encontrei um Erro ao acessar o site: ' + '\033[4;34m' + f'{link}' + '\033[0;0m')
    print('\033[1;31m' + 'ERROR ENCONTRADO: ' + '\033[0;0m' + f'{error}')

  else:
    print('\033[1;32m' + 'O site está disponível.')
    
  finally:
    print('\033[0;0m' + 20 * '-=')
