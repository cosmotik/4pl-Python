with open("SMTH.txt", "r") as first_f, open("SMTH2.txt", "a") as second_f:
    for line in first_f:
        second_f.write(line)
