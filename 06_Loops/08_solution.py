number  = 4
isPrime = True

if number > 1:
    for num in range(2,number):
        if (number % num) == 0:
            isPrime = False
            break

print(isPrime)