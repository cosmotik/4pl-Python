from data import question_data
from question import Question
from quiz import Quiz

question_bank = []
for n in question_data:
    question_category = n["category"]
    question_type = n["type"]
    question_difficulty = n["difficulty"]
    question_text = n["question"]
    question_answer = n["correct_answer"]
    question_incorrect = n["incorrect_answers"]

    new_question = Question(question_category, question_type, question_difficulty, question_text, question_answer,
                            question_incorrect)

    question_bank.append(new_question)

quiz = Quiz(question_bank)

while quiz.remaining_question():
    quiz.next_question()

print(f"You completed the Quiz. Your final score is {quiz.score}/{quiz.question_num}")
