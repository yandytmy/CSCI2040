isnum = False
num = ['0']*4

while isnum == False :
  s = input('Please input the first number:')
  try:
    float(s)
    isnum = True
  except ValueError:
    print('Your input is not a number!')
num[0]=float(s)

isnum = False
while isnum == False :
  s = input('Please input the second number:')
  try:
    float(s)
    isnum = True
  except ValueError:
    print('Your input is not a number!')
num[1]=float(s)

isnum = False
while isnum == False :
  s = input('Please input the third number:')
  try:
    float(s)
    isnum = True
  except ValueError:
    print('Your input is not a number!')
num[2]=float(s)

isnum = False
while isnum == False :
  s = input('Please input the fourth number:')
  try:
    float(s)
    isnum = True
  except ValueError:
    print('Your input is not a number!')
num[3]=float(s)

num.sort()
#print(num)
print('The second smallest value is '+ str(num[1]))
num.sort(reverse=True)
print('The second biggest value is '+ str(num[1]))
print('Program ends.')
