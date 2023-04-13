# Exercício 109 - Formatando Moedas em Python

import comandos

num = float(input('Digite um preço: R$ '))

print(f'A metade de R${num:.2f} é: {comandos.metade(num, form=True)[0]}')

print(f'O dobro de R${num:.2f} é:  {comandos.dobro(num, form=True)[0]}')

print(f'Aumentando {comandos.aumenta(num, form=True)[1][1]}, temos:  {comandos.aumenta(num, form=True)[1][0]}')

print(f'Diminuindo {comandos.diminuir(num, 13, form=True)[1][1]}, temos:  {comandos.diminuir(num, 13, form=True)[1][0]}')
