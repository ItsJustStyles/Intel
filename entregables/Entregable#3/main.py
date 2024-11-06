#Se hace la función recursiva para calcular el factorial de un número
def factorial(n):
  if n == 0:
    return 1
  elif n < 0:
    return "No es un número positivo"
  else:
    return n * factorial(n-1)
try:
  n = int(input())
  print(factorial(n))
except:
  print("El valor ingresado no es un número")
