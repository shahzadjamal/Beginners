Kilometers = int(input('Enter the value of Kilometers: ')) #input from user and converting to integer
print(type(Kilometers))
con_factor = 0.6214
print(type(con_factor))
con_km_to_mile = Kilometers * con_factor
##print('Your entered kilometers = ', ('{:,}'.format(con_km_to_mile),"miles"))
## working code # print('Your entered kilometers =','{:,}'.format(con_km_to_mile),'miles')
## print('{:,}'.format(1234567890))
print('{:,}'.format(Kilometers),"kilometers is equal to: "'{:,}'.format(con_km_to_mile),'miles')