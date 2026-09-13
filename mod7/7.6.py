import math


def calculate_unit_price(diameter, price):
    radius = diameter / 200
    area = math.pi * radius ** 2
    unit_price = price / area

    return unit_price


diameter1 = float(input("Enter the diameter of pizza 1 in centimetres: "))
price1 = float(input("Enter the price of pizza 1: "))

diameter2 = float(input("Enter the diameter of pizza 2 in centimetres: "))
price2 = float(input("Enter the price of pizza 2: "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

print("Pizza 1 unit price:", unit_price1, "euros per square metre")
print("Pizza 2 unit price:", unit_price2, "euros per square metre")

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")