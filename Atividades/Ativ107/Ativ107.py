# Exercício 107 - Exercitando módulos em Python

import comandos

num = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {num:.2f} é: R$ {comandos.metade(num):.2f}')
print(f'O dobro de R$ {num:.2f} é R$ {comandos.dobro(num):.2f}')
print(f'Com aumento de {comandos.aumenta(num)[1]}%, o novo valor ficar igual à: R$ {comandos.aumenta(num)[0]:.2f}')
