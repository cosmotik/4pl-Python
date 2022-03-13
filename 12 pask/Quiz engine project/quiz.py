class Quiz:
    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        # set current_question to question bank index
        current_question = self.question_list[self.question_num]
        # add 1 to go to the next question
        self.question_num += 1
        # get user answer by inputting it in the console
        user_answer = input(f"{self.question_num}: {current_question.question} (True/False): ")
        # check if answers match
        self.check_answer(user_answer, current_question.correct_answer)

        # checking answers and adds score
    def check_answer(self, user_answer, correct_answer):
        # .lower() you can write as lowercase as uppercase
        if user_answer.lower() == correct_answer.lower():
            # if correct than add + 1 to total score
            self.score += 1
            print("Correct!")
        else:
            # if you get it wrong printing:
            print("You got it wrong!")
            print(f"The correct answer was: {correct_answer}")
        # after each question prints your score
        print(f"Your current score: {self.score}")

    def remaining_question(self):
        # check if the current question is less than amount of the questions
        return self.question_num < len(self.question_list)
