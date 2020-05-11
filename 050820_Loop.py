count = 0
print('Starting')
while count < 10:
    count += 1
    print(count, ' ', end='')  # the end='' line removes a carriage return
print()  # This statement added a carriage return before Done
print('Done')

###############################################################################

count = 0
print('Starting')
while count < 10:
      print(count, ' ', end='')  # the end='' line removes a carriage return
      count += 1  # Since count is printed here after the above print statement, the count starts from 0
print()  # This statement added a carriage return before Done
print('Done')