def linha_simples():
  print(cores(1, 35) + 40 * '-' + cores())


def linha_composta():
  print(cores(1, 35) + 20 * '-=' + cores())


def cabecalho(nome):
  linha_composta()
  print(cores (1, 34) + f'{nome:^40}' + cores())
  linha_composta()


def cores(estilo=0, texto=0, fundo=0):  
  if fundo == 0:
    return f'\033[{estilo};{texto}m'

  else:
    return f'\033[{estilo};{texto};{fundo}m'
  


def menu():  
  from comandos.outros import opcao_um, opcao_dois

  while True:
    # Cabeçalho
    cabecalho('MENU PRINCIPAL')
    
    # Tabela
    print(cores(1, 35) + '1' + cores(1, 36) + ' - ' + cores(0, 34) + 'Ver pessoas cadastradas' + 
          '\n' + cores(1, 35) + '2' + cores(1, 36) + ' - ' + cores(0, 34) + 'Cadastrar uma nova pessoa' +
          '\n' + cores(1, 35) + '3' + cores(1, 36) + ' - ' + cores(0, 34) + 'Sair do Sistema' + cores())
    linha_simples()

    # Escolha
    try:
      escolha = int(input(cores(1, 36) + ' -> O que deseja fazer: '))
      
      # Opção 1
      if escolha == 1:
        opcao_um()
        
      # Opção 2
      elif escolha == 2:
        opcao_dois()
        
      # Sair
      elif escolha == 3:
        cabecalho('Finalizando o Sistema, Até logo!')
        break

      # Erro
      else:
        print(cores(1, 31) + 'ERROR: Por favor digite um número entre [1, 2, 3]')
  
    # Tratamento de Erro
    except Exception as error:
      print(cores(1, 31) + f'Encontramos um erro: {error}')
  