# Aula 19 - Dicionários

# Manipulação de Dicionários
dados = dict()
dados = {'nome':'Pedro', 'idade':'25'}

print(dados['nome']) # S: Pedro
print(dados['idade']) # S: 25

dados['sexo'] = 'M' 
# dados = {'nome':'Pedro', 'idade':'25', 'sexo':'M'}

del dados['idade'] 
# dados = {'nome':'Pedro', 'sexo':'M'}

filme = {'Título':'Star Wars',
         'Ano':'1977',
         'Diretor':'George Lucas'
}
# filme = {'Título':'Star Wars', 'Ano':'1977', 'Diretor':'George Lucas'}

print(filme.values())
# values == 'Star Wars', '1977', 'George Lucas'
# S: dict_values(['Star Wars', '1977', 'George Lucas'])

print(filme.keys())
# keys == Título', 'Ano', 'Diretor'
# S: dict_keys(['Título, 'Ano', 'Diretor'])

print(filme.items())
# items == values e keys
# S: dict_items([('Título', 'Star Wars'), ('Ano', '1977'), ('Diretor', 'George Lucas')])

for k, v in filme.items():
  print(f'O {k} é {v}')

# S: O Título é Star Wars
# S: O Ano é 1977
# S: O Diretor é George Lucas

""" É possível juntas as 3 formas de variáveis compostas: Tiplas, Listas & Dicionários

Por exemplo:
"""

locadora = [{'Título' : 'Star Wars',
             'Ano' : '1977',
             'Diretor' : 'George Lucas'},
            
            {'Título' : 'Avengers',
             'Ano' : '2012',
             'Diretor' : 'John Whadon'},
            
            {'Título' : 'Matrix',
             'Ano' : '1999', 
             'Diretor' : 'Wachowski'}]

print(locadora[0]['Ano'])
# S: 1977

print(locadora[2]['Título'])
# S: Matrix

# Parte Prática:

pessoas = {'nome' : 'Gustavo', 'sexo' : 'M', 'idade' : '22'}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# S: O Gustavo tem 22 anos.

for k in pessoas.keys():
  print(k)
# S: nome
#    sexo
#    idade

for v in pessoas.values():
  print(v)
# S: Gustavo
#    M
#    22

for k, v in pessoas.items():
  print(f'{k} = {v}')
# S: nome = Gustavo 
#    sexo = M
#    idade = 22

pessoas = {'nome' : 'Gustavo', 'sexo' : 'M', 'idade' : '22'}
pessoas['nome'] = 'Leandro'
print(pessoas['nome'])
# S: Leandro

pessoas['peso'] = '89,7Kg'
print(pessoas)
# S: {'nome' : 'Gustavo', 'sexo' : 'M', 'idade' : '22', 'peso' : '89,7Kg'}

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla' : 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
# S: Rio de Janeiro

print(brasil[1]['sigla'])
# S: SP

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

brasil = list()
estado = dict()

for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  brasil.append(estado.copy())

print(brasil)
# S: {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'....}

for e in brasil: # for para a lista
  for v in e.values(): # for para o dicionário
    print(v, end=' - ')
  print()

# S: Rio de Janeiro - RJ
#    São Paulo - SP
#    Acre - AC


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#              Atividades
#        Ativ90.py - Ativ95.py
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
