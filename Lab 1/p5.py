pali = input('Please input a palindrome: ')
check = False

while (check == False):
    check = True
    length = len(pali)
    length = int(length)
    m = length - 1
    for n in range(0, length):
        #print(n ,m)
        while (pali[n] == ' ') or (pali[m] == ' '):
            if (pali[n] == ' '):
                n += 1
            if (pali[m] == ' '):
                m -= 1
            #print(n,m)
        if (pali[n] > pali[m]) or (pali[n] < pali[m]):
            check = False
            break
        if (n == m) or (n > m):
            break
        m -= 1
    if (check == False):
        pali = input('No, you must input a palindrome: ')

print('Welcome to the wonderland!')
