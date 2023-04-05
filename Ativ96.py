def linha():
  print(20 * '-=')


def titulo(msg):
  linha()
  print(10 * ' ' + msg)
  linha()
  

def area(l, c):
  a = l * c
  print(f'A área é de: {a:.2f} m²')


titulo('CÁLCULO DE ÁREA')

largura = float(input('Largura em metros: '))
comprimento = float(input('Comprimento em metros: '))
area(largura, comprimento)

linha()
