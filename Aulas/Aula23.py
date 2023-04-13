"""
-=-=-=-=-=-=-=-=-=-= Aula 23 - Tratamento de Erros e Exceções =-=-=-=-=-=-=-=-=-=-

-> Erro de Sintaxe:
    # O nome da Função está errado.
    Ex:
      primt()

-> NameError:
    # 'x' não tem nenhum atribuição.
    Ex:
      print(x)

-> ValueErro:
    # Erro de valor, esperando um valor interiro e recebendo um valor string.
    Ex:
      num = int(input('Digite um número: ')) # num recebe "oito"
      print(num)

-> ZeroDivisionError:
    # Erro de divisão por 0, onde não é possível realizar o calculo.
    Ex:
      divisao = 2 / 0

-> TypeError:
    # Erro de tipo.
    Ex:
      divisao = 2 / '2'

-> IndexErro:
    #Erro de 'key' ou índece.
    Ex:
      Lst = [3, 6, 4]
      print(Lst[3])

-> ModuleNotFoudError:
    # Erro onde um módulo não é encontrado.
    Ex:
      import uteis
      

-=-=-=-= Definição =-=-=-=-
Erro: 
Erro de sintaxe ou semântica, onde o erro é no código em si.

Exceção:
Um erro onde o comando está escrito corretamente e o erro aconteceu na entrada ou saída do código.

-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Comando para tratamento de Erros e Exceções: 'try:' e 'except:'

-> Exemplo:

    try:
      operação
    
    except:
      falha
    
-=-=-= Outros Exemplos =-=-=-
->  # Else e Finally são opcionais, nem sempre sarão necessárias.
    
    try:
      operação
    
    except:
      falha
    
    else:
      deu certo
    
    finally:
      certo/falha
      
-> # O comando 'try' e 'except' podem ter mais de um except.

    try:
      operação
    
    except TypeError:
      falhou

    except ValueError:
      falhou
      
    except OSError:
      falhou
    
    else:
      deu certo
    
    finally:
      certo/falha
      
-> # Podemos botar mais de um erro em um mesmo comando except.

    try:
      operação
    
    except (TypeError, ValueError):
      falhou
      
    except OSError:
      falhou
    
    else:
      deu certo
    
    finally:
      certo/falha
      

-=-=-= Parte Prática =-=-=-
"""
try:
  a = int(input('Numerador: '))
  b = int(input('Denominador: '))
  r = a / b

except Exception as error:
  print('Infelizmente tivemos um problema :(')
  print(f'O erro encontrado foi {error.__cause__}')

except (ValueError, TypeError):
  print('Tivemos um problema com os tipo de dados que você digitou.')

except ZeroDivisionError:
  print('Não é possível dividir um número por 0!')

except KeyboardInterrupt:
  print('O usuário preferiu não informar os dados!')

else:
  print(f'O resultado é {r:.1f}')

finally:
  print('Volte sempre! Muito Obrigado!')

"""
-=-=-=-=-=-= Desafios/Atividades =-=-=-=-=-=-
# Ativ113 até Ativ115c
"""