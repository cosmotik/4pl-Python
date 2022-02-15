import random

From = int(input("Input the lower value: "))
To = int(input("Input the Upper value: "))
guesses = 0
difficulty_tries = {'Easy': 9, 'Medium': 6, 'Hard': 3}

while True:
    difficulty = input("Choose (Easy/Medium/Hard) difficulty")
    difficulty_tries = input(f"You have {difficulty_tries[difficulty]} tries")
    try:
        number = random.randint(From, To)
        break
    except KeyError:
        print("Incorrect input, try again!")
while True:
        guess = int(input("Your number: "))
        guesses += 1
        if number == guess:
            print(f"Correct guess! You used {guesses} guesses")
        elif guess < From or guess > To:
            print("Your guess is out of range!!!")
        elif guess > number:
            print("Number is too high")
        elif guess < number:
            print("Number is too low")

        if guesses >= int(difficulty_tries[int(difficulty)]):
            print("You dont have more guesses")
            print("The number was", number)
