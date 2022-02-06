def reverse_str(str):
    str1 = ""
    for x in str:
        str1 = x + str1
    return str1
str = str(input("Input some word: "))
print(reverse_str(str))