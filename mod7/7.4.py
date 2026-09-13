def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


number_list = [4, 7, 2, 9, 5]

result = calculate_sum(number_list)

print("The sum is:", result)