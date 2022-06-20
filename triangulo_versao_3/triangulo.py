from random import randint

def vertices():
  x = randint(0, 10)
  y = randint(0, 10)
  return x, y

def distancia(x_a, y_a, x_b, y_b):
  return ( (x_a - x_b)**2 + (y_a - y_b)**2 )**(1/2)

def valido(lado1, lado2, lado3):
  soma1 = lado1 + lado2
  soma2 = lado1 + lado3
  soma3 = lado2 + lado3

  if ((lado1 == lado2) and (lado2 == lado3)):
      return True
  elif ((soma1 > lado3) and (soma2 > lado2) and (soma3 > lado1)):
      return True
  else:
      return False

def area(a, b, c):
  p = (a + b + c)/2
  return (p * (p-a) * (p-b) * (p-c))**(1/2)
