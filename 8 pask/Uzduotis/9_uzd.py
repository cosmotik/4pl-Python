import os
with open("SMTH.txt") as f:
    info = os.stat("SMTH.txt")
    print(info.st_size)