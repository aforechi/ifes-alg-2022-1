import triangulo

def main():
  for i in range(10):
    x1, y1 = triangulo.vertices()
    x2, y2 = triangulo.vertices()
    x3, y3 = triangulo.vertices()

    a = triangulo.distancia(x1, y1, x2, y2)
    b = triangulo.distancia(x3, y3, x2, y2)
    c = triangulo.distancia(x1, y1, x3, y3)
  
    if triangulo.triangulo_valido(a, b, c):
      print('Area = ', triangulo.area(a, b, c))
    else:
      print('As coordenadas abaixo não formam um triângulo válido!')    
      print(x1, y1, x2, y2, x3, y3)
      print(a, b, c)

if __name__ == '__main__':
    main()