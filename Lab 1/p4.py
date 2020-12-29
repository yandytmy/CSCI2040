import getpass

target = getpass.getpass(prompt = 'Player 1, write down your number secretly: ')
target = int(target)
while (target < -100) or (target > 100):
    target = getpass.getpass(prompt = 'Player 1, invalid input, write down your number secretly: ')
    target = int(target)

tried = 0
while (tried < 6):
    tried += 1
    guess = input('Player 2, input your guess: ')
    guess = int(guess)
    if (guess == target):
        print('You are right after trying for', tried, 'times.Program ends.')
        break
    elif (tried == 6):
        print('You have tried 6 times and it is still wrong!The answer is', target, 'and program ends.')
    elif (guess < target):
        print('Your guess is too low!')
    elif (guess > target):
        print('Your guess is too high!')