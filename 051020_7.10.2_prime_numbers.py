# Take the input from the user:
upper = int(input("Enter upper range: "))

for num in range(2, upper):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            print(num)
