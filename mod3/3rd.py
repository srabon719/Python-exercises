n1=int(input("Enter first number: "))
n2=int(input("enter second number: "))

total=n1 + n2
print("The sum of the numbers is :",total)

multiplication=n1 * n2
print("The multiplication of the numbers is :",multiplication)

if n2 == 0:
	print("The division is undefined because the second number cannot be zero.")
else:
	division=n1 / n2
	print("The division of the numbers is :",division)
