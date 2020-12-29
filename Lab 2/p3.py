#python_version == '3.7'

def fibo(x1, x2):
  value = 0
  while value < 1000:
    value = x1 + x2
    x1 = x2
    x2 = value
  return value