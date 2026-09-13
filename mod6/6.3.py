number = int(input("Enter an integer: "))

prime = True

if number < 2:
    prime = False
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            break

if prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")