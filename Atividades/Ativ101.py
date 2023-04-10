# Exercício 101 – Funções para votação

# Ano atual: datetime.datetime.now().year
def linha():
  print(20 * '-=')


def voto(ano):
  import datetime
  global idade
  global situacao

  idade = (datetime.datetime.now().year) -ano_nascimento

  if idade >= 70 or idade == 16 or idade == 17:
    return f'Você tem {idade} anos, e sua situação de voto é: OPICIONAL'
  
  elif idade < 16:
    return f'Você tem {idade} anos, e sua situação de voto é: NEGADO'

  else:
    return f'Você tem {idade} anos, e sua situação de voto é: OBRIGATÓRIO'

    
# Código principal:
linha()

ano_nascimento = int(input('Digite o ano de seu nascimento: '))

print(voto(ano_nascimento))
