def even_number(numbers):
    num_list = []
    for x in numbers:
        if x % 2 == 0:
            num_list.append(x)
    return num_list

print(even_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))