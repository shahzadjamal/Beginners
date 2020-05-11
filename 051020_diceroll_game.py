import random
Min = 1
Max = 6

roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dice....')
    print('The values are ...')
    dice1 = random.randint(Min, Max)
    print(dice1)
    dice2 = random.randint(Min, Max)
    print(dice2)
    roll_again = input('Roll the dices again? (y/n)? ')
