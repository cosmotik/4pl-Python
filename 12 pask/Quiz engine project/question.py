class Question:

    def __init__(self, category, type, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
