n = 0
while n != '-1':
 n = input('Enter an integer: ') 
 if n != '-1':
  s = input('Enter a string:') 
  for i in range(int(n)):
    for j in range (int(n)-i-1):
      print(' '*len(s), end ='')
    for k in range (i+1):
      if k == i:
        print(s, end ='\n')
      else:
        print(s, end ='')
print('Program ends.')