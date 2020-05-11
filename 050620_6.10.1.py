user_input = int(input('Enter a numeric value:'))
if user_input >= 1:
    print('{:,}'.format(user_input), ' is a positive non zero number')
elif user_input == 0:
    print('{:,}'.format(user_input), ' is a zero value')
else:
    print('{:,}'.format(user_input), ' is a negative number')



