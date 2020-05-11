Kilometers = int(input('Enter the value of Kilometers: ')) #input from user and converting to integer
con_factor = 0.6214
con_km_to_mile = Kilometers * con_factor
if Kilometers >=0:
    print('{:,}'.format(Kilometers), "kilometers is equal to: "'{:,}'.format(con_km_to_mile), 'miles')
else:
    print('Please enter a positive number for conversion')
##print('Your entered kilometers = ', ('{:,}'.format(con_km_to_mile),"miles"))
## working code # print('Your entered kilometers =','{:,}'.format(con_km_to_mile),'miles')
## print('{:,}'.format(1234567890))
