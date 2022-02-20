f = open("SMTH.txt", "r")
count = 0
content = f.read()
content_list = content.split("\n")

for i in content_list:
    if i:
        count += 1
print("The number of lines in file is: ", count)
