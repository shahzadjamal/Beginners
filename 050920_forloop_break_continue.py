user_input = int(input('Please enter a value between 0 to 10: '))
for loop1 in range (0,8):
    if loop1 == user_input:
        break
    print(loop1, ' ', end='')
print('Done')