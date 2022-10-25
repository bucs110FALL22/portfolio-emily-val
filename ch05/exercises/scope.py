def multiply(a, b):
  number = 0
  for i in range(b):
    number = number + a
  return number

def exponent(c, d):
  number = 1
  for i in range(d):
    number = number * c
  return number

def square(e):
  return exponent(e, 2)

def main():
  print(multiply(3, 9))
  print(exponent(2, 8))
  print(square(4))

main()
  