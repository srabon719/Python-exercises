def averages(float_numbers):
    sum=0
    for n in range(len(float_numbers)):
        sum+=float_numbers[n]
    return sum /len(float_numbers)
float_numbers = [14.76,23.45,34.65,34.76,45.67,56.78,67.89,78.90,89.01,90.12]
result = averages(float_numbers)
print(f"The average of the numbers is: {result:.2f}")
