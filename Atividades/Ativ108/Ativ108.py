import comandos

num = float(input('Digite um preço: R$ '))
print(f'A metade de R${num:.2f} é: {comandos.formatacao(comandos.metade(num))[0]}')
print(f'O dobro de R${num:.2f} é:  {comandos.formatacao(comandos.dobro(num))[0]}')
print(f'Aumentando {comandos.formatacao(comandos.aumenta(num)[1])[1]}, temos:  {comandos.formatacao(comandos.aumenta(num)[0])[0]}')
