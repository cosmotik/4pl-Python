def multi(List):
    result = 1
    for x in List:
        result *= x
    return result
list = [1, 2, 4, 7, 9]

print(multi(list))