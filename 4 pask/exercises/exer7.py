def string(text):
    count ={"Upper_case":0, "Lower_case":0}
    for letter in text:
        if letter.isupper():
           count["Upper_case"]+=1
        elif letter.islower():
           count["Lower_case"]+=1
        else:
           pass
    print ("Original String : ", text)
    print ("No. of Upper case characters : ", count["Upper_case"])
    print ("No. of Lower case Characters : ", count["Lower_case"])

text = str(input("Input a sentence: "))
print(string(text))
