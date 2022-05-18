from data import quiz_list
from quiz_model import Question
from quiz_machine import QuizMachine
from design import QuizUI

quiz_bank = []

for quiz in quiz_list:
    q_text = quiz["question"]
    q_ans = quiz["correct_answer"]
    new_quiz = Question(q_text, q_ans)
    quiz_bank.append(new_quiz)


quiz = QuizMachine(quiz_bank)

quiz_ui = QuizUI(quiz)