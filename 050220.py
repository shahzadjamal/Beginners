## Using book from Springer for the tutorial. Book name is Beginner's guide to Python. Book is downloaded in G:\Documentation
print("Hello World")
user_name = input('Enter your name: ')
print('Hello', user_name)
user_name = input('Enter your city: ')
print('Your city name is', user_name)
user_name = ''  # resetting the variable to empty
print(user_name)
z = """
This is
Good Stuff
"""
print(z)
print(type(print))
print(type(user_name))
print(len(user_name))  # after resetting the variable above, you will notice the length of the string user_name is 0
my_string = 'Hello World'
print(my_string[8])  # This will print the character stored in position 4. Remember the position starts from 0 zero
print('Hi' * 10)  # repeat the string 10 times
print(my_string[1:5])  # from position 1 to 5
print(my_string[:5])  # from start to position 5
##Below code written on 5/3/20
my_phone_version = ('Currently I have iPhone7 in black color')
print(my_phone_version.split(' '))
print(my_phone_version.count(' '))  # counting spaces in variable my_phone_version
print(my_phone_version.replace('I', 'i'))
################################################
Text1 = 'My name is '
Text2 = 'Shahzad'
print(Text1 + Text2)
## the next code will output same same result as above
Text1 = input('My name is:')
print('My name is ', Text1)
Text2 = input('My city name is:')
print('My city name is ', Text2)
Text3 = Text1 + Text2
print(Text3)
print('The line above has', len(Text3), 'characters')  ##length of the output viariable
my_phone = 'iPhone7'
print(my_phone[0])
print(type(my_phone))
print(my_phone.find('e'))  ##Find inside a variable
print('Edward John Alun'.find('Alun'))

# This is the first program created in python during lockdown and Ramazan. Date started May 1st, 2020. An important point in this
# example is that the variable (user_name) is used twice can be used multiple times with different values. This is a
# feature of python and is not possible in other languages. A variable can have only single value

#msg = 'Black Hawk Down' + 21  ## Gives an error because of integar
msg = 'Black Hawk Down' + str(21)  ## Prints with concatenate
msg = 'Black Hawk Down' + str(' ') + str(21)  ## Prints with concatenate. Added space before 21
print(msg)

# ########################################################
# Date: 050520

powercase = 'Today is 10th or 11th of Ramadan. Its Tuesday, May 5th 2020. The time is 6PM.'
print(powercase.istitle(),('S')
some_string = "Hello World"
print('some_string.istitle()', some_string.istitle())
print (some_string.format()

format_string = "{artist} sang {song} in {year}"
print(format_string.format(artist='Paloma Faith',
song='Guilty', year=2017))

print('|{:>25}|'.format('Apple')) ## right aligned in a 25 characters width
print('|{:^30}|'.format('Orange')) ## center aligned in a 30 characters width

num_example1 = 16 ** 3  ## Arithmetic OPERATORS: // = divide and ignore any remainder, % = returns any remainder,
# ** = to the power of
print(num_example1)
# Below is example of complex number computation
c1 = 1j
c2 = 2j
c3 = c1 * c2
print(c3)
# You use 'is or is not" to check if the cariable is set to None
winner = None
print(winner is not None)
print(type(winner))
winner = True
print(winner is not False)
print(type(winner))

## Convert