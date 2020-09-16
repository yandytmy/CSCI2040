list = []
check = False
while check == False:
    a = input('Please input the first number: ')
    print(type(a))
    if (a.isnumeric() == True):
        check = True
    else:
        try:
            float(a)
            check = True
        except:
            check = False
    if (check == False):
        print('Your input is not a number!')
list.append(a)

check = False
while check == False:
    b = input('Please input the second number: ')
    if (b.isnumeric() == True):
        check = True
    else:
        try:
            float(b)
            check = True
        except:
            print('Your input is not a number!')
list.append(b)

check = False
while check == False:
    d = input('Please input the second number: ')
    print(d.isnumeric())
    print(type(d))
    if (d.isnumeric() == True):
        check = True
    elif isinstance(d, float) == True:
        check = True
    else:
        print('Your input is not a number!')
list.append(d)

check = False
while check == False:
    c = input('Please input the third number: ')
    print(type(c))
    print(c.isnumeric())
    print(isinstance(c, float))
    if isinstance(c, int) == True:
        check = True
    elif isinstance(c, float) == True:
        check = True
    else:
        print('Your input is not a number!')
list.append(c)

for x in list:
    print(x)
