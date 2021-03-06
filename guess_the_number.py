import random

correct = 'you guessed correctly!'
TOO_LOW = 'too low'
too_high = 'too high'



def configure_range():
    '''Set the high and low values for the random number'''

    return 1, 1000


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))
        except ValueError:
            print("please enter only whole number")


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:

        return 'too low'

    if guess > secret:
        return 'too_high'

def close_game():
    Input=input("do you want to play again? press n to end. press any key to play again")
    return Input.lower()=='n'


def main():


    (low, high) = configure_range()
    secret = generate_secret(low, high)

    counter = 0 

    while True:
         
        guess = get_guess()
        result = check_guess(guess, secret)
        counter = counter +1 
        print(result)

        if result == correct:
            print (f'Guessed {counter} times')
            if close_game():
                break
           
            
       
       




if __name__ == '__main__':
    main()
