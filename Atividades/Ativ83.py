# Minha solução(9 linhas):
sintaxe = []
sintaxe.append(str(input('Digite uma expressão: ')))
cont_esq = sintaxe[0].count('(')
cont_d = sintaxe[0].count(')')
print(20 * '-=')
if cont_esq == cont_d:
  print('Sua expressão está válida!')
else:
  print('Sua expressão está incorreta')

# Solução do Guanabara(15 linhas):

expr =  str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('Sua expressão está válida.')
else:
  print('Sua expressão está incorreta.')
