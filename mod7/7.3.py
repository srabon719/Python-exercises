def gallons_to_litres(gallons):
    return gallons * 3.785


gallons = float(input("Enter gasoline in gallons: "))

while gallons >= 0:
    litres = gallons_to_litres(gallons)
    print("The amount in litres is:", litres)

    gallons = float(input("Enter gasoline in gallons: "))