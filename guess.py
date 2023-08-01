import random as r

score = 100
while True:
    number = r.randrange(10)
    while True:
        print (number)
        try:
            ninput = int(input('Guess the number from 0 to 9? '))
            if ninput not in range(10):
                raise ValueError


            if ninput == number and score >= 70:
                print('Wow... you are a wizard!')
                print('Your score:', score)
                break
            elif ninput == number and score <= 70:
             print('Correct... but you can be better')   
            else:
                print('Wrong answer')
                score -= 10
        except ValueError:
            print('Please enter a valid number')
