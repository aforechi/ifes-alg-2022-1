import triangulo

def main():
  quantidade_de_triangulos_validos = 0
  while quantidade_de_triangulos_validos < 10:
    x1, y1 = triangulo.vertices()
    x2, y2 = triangulo.vertices()
    x3, y3 = triangulo.vertices()

    a = triangulo.distancia(x1, y1, x2, y2)
    b = triangulo.distancia(x3, y3, x2, y2)
    c = triangulo.distancia(x1, y1, x3, y3)

    if triangulo.valido(a, b, c):
      print('Area = %.2f' % triangulo.area(a, b, c))
      quantidade_de_triangulos_validos += 1
    else:
      print('Não é triangulo')
      print(a, b, c)
      print(x1, y1, x2, y2, x3, y3)

if __name__ == '__main__':
    main()