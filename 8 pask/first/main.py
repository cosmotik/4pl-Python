import os
# f = open("data.txt", "r") # r - read mode
# print(f.read())
# print(f.readline())

# text = []
# for line in f:
#     print(line)
#     text.append(line)
#
# f.close()
# print(text)

# f = open("data.txt", "a")
#
# for x in range(100):
#     f.write(f"[{x}] - This line is added from code\n")
#
# f.close()

# if os.path.exists("data2.txt"):
#     print("File exists")
#     os.remove("data2.txt")
# else:
#     print("File not found")

with open("data.txt") as file:
    print(file.read())

