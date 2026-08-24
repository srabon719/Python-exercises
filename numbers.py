a1 = 10
a2 =-10
a3=1.2
a4=-2+3j
a5= 1_7673_632623_6423

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

print(type(a1))
print(type(a2))
print(type(a3))
print(type(a4))
print(type(a5))

s1="Hello"
s2='Hello'
s3="123"
s4=""
s5="Albert said: 'Hello'"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print(type(s3))
s3_converted=float(s3)
print(type(s3_converted))

a6=7
a7=2
a8mod=a6%a7
print(a8mod)

a9floor=a6//a7
print(a9floor)

a10power=a6**a7
print(a10power)

farenheit_str = input("Enter temperature in Fahrenheit: ")
farenheit = float(farenheit_str)
celcius = (farenheit - 32) * 5/9
print("Temperature in Celcius is: "+ str(celcius))
print(f"Temperature in Celcius is: {celcius:10.8f}")