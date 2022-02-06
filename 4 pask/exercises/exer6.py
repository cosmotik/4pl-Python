def is_range(x):
    if x in range(1, 7):
        print(f" Number {x} is in the range")
    else :
        print(f" Number {x} is not in the range")

x = int(input("Input a number: "))
print(is_range(x))