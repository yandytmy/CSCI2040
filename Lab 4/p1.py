#python_version == '3.7'

import math
# list1 = []
# list2 = []
a = map(lambda x: math.sqrt(x), [1,2,3,4,5,6,7,8,9,10])
# for x in a: 
#     list1.append(math.floor(x))
# print (list1)

a = map(lambda x: x+1, [1,2,3,4,5,6,7,8,9,10])
# for x in a: 
#     list2.append(math.floor(x))
# print (list2)

a = [ x for x in [1,2,3,4,5,6,7,8,9,10] if x <= 7]
# print(a)

a = [ x**2 for x in [1,2,3,4,5,6,7,8,9,10] if x % 2 != 0]
# print(a)
