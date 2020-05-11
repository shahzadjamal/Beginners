def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print('Please enter a positive number for factorial')
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

#user_input = int(input('Please enter the number to find the factorial for: '))
#for num == user_input:
#    factorial = num(num - 1)


