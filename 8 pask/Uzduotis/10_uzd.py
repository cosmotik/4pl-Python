cars = ["bmw", "audi", "porsche", "lamborghini", "buggati"]
with open("data.txt", "w") as f:
    for x in cars:
        f.write(f"{x}\n")
    content = open("data.txt")
    print(content.read())
