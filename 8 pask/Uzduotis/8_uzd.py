word_count = 0
with open("SMTH.txt") as f:
    words = f.read().split()
    for x in words:
        word_count += 1
    print(word_count)
