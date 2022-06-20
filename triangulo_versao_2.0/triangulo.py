from random import randint

def vertices():
  x = randint(0, 10)
  y = randint(0, 10)
  return x, y

def distancia(x1, y1, x2, y2):
  dx = x1 - x2
  dy = y1 - y2
  return (dx**2 + dy**2)**(1/2)

def triangulo_valido(a, b, c):
  if (a < b):
    a, b = b, a
  if (a < c):
    a, c = c, a
  if (b < c):
    b, c = c, b

  if a >= (b + c):
    return False
  else:
    return True


def area(a, b, c):
  p = (a + b + c)/2
  return ( p*(p-a)*(p-b)*(p-c) )**(1/2)

