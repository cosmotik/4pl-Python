class Quiz:
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1

        user_answer = input(f"{self.question_num}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.correct_answer)

    def remaining_question(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("You got it wrong!")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}")
