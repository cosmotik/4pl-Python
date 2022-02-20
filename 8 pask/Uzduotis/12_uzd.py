import string
alphabet = string.ascii_lowercase
for letter in alphabet:
    with open(f"./12 uzd output/ {letter}.txt", "w") as file:
        file.write(letter)