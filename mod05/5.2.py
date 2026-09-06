while True:
    inches = float(input("Enter inches: "))

    if inches < 0:
        break

    centimeters = inches * 2.54
    print("Centimeters:", centimeters)