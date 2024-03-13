form random import randint

answer = randint(1, 10)

guess = int('guess a number between 1 and 10: ')

while True:
    try:
        if int(guess) > 0 and int (guess) < 11:
            if int(guess) == answer:
                print('you are a genius!')
                break
    except:
        print('hey bozo, I said 1~10')
    else:
        print('hey bozo, I said 1~10')
    guess = input('guess a number between 1 and 10: ')

