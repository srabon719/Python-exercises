def remove_uneven(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


original_list = [1, 2, 3, 4, 5, 6, 7, 8]

cut_down_list = remove_uneven(original_list)

print("Original list:", original_list)
print("Cut-down list:", cut_down_list)