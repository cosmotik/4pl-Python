with open("SMTH.txt") as f:
    words = f.read().split()
    max_lenght = max(words, key=len)
    print(max_lenght)