from question_model import Question
from data import question_data
from quiz_game import QuizGame

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question ["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizGame(question_bank)

while quiz.still_has_question():
    quiz.next_question()

quiz.next_question()