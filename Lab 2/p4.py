#python_version == '3.7'
import math

def check_invalid(triangle):
  if triangle[0] > 0 and triangle[1] > 0 and triangle[2] > 0 :
    if triangle[0] + triangle[1] > triangle[2] :
      if triangle[2] + triangle[1] > triangle[0] :
        if triangle[2] + triangle[0] > triangle[1] :
          return False
  return True

def is_isosceles_triangle(triangle):
  if check_invalid(triangle) == False:
    if triangle[0] == triangle[1]:
      return True
    elif triangle[2] == triangle[1]:
      return True
    elif triangle[2] == triangle[0]:
      return True
  return False

def perimeter(triangle):
  return (triangle[0] + triangle[1] + triangle[2])

def area(triangle):
  a = triangle[0]
  b = triangle[1]
  c = triangle[2]
  s = (a + b + c)/2
  return math.sqrt(s*(s-a)*(s-b)*(s-c))