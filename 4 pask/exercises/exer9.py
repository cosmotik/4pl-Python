def prime_number(numb):
    if (numb == 1):
        return False
    if (numb == 2):
        return True;
    else:
        for x in range(2, numb):
            if(numb % x == 0):
                return False
        return True
x = int(input("Input a number: "))
print(prime_number(x))