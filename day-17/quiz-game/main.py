from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for ques in question_data:
    new_question = Question(ques["text"], ques["answer"])
    question_bank.append(new_question)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_have_questions():
    quiz_brain.next_question()

print("Quiz Completed")
print(f"You scored {quiz_brain.score}/{len(quiz_brain.question_list)}")
