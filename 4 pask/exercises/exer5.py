def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("Input a number to compute the factiorial : "))

print(factorial(x))