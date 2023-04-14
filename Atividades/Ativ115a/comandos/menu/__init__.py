def linha_simples():
  print(40 * '-')


def linha_composta():
  print(20 * '-=')


def cabecalho(nome):
  linha_composta()
  print(f'{nome:^40}')
  linha_composta()


def menu():  
  from comandos.outros import opcao_um, opcao_dois

  while True:
    # Cabeçalho
    cabecalho('MENU PRINCIPAL')
    
    # Tabela
    print('1 - Ver pessoas cadastradas' + 
          '\n' + '2 - Cadastrar uma nova pessoa' +
          '\n' + '3 - Sair do Sistema')
    linha_simples()

    # Escolha
    try:
      escolha = int(input('O que deseja fazer: '))
      
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
        print('ERROR: Por favor digite um número entre [1, 2, 3]')
  
    # Tratamento de Erro
    except Exception as error:
      print(f'Encontramos um erro: {error}')
  