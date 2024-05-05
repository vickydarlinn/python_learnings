class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_have_questions(self):
        return len(self.question_list) > self.question_number


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Ques {self.question_number}. {current_question.text} (True/False)?: ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans ,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The Correct answer was {correct_ans}")
        print(f"Your current score is {self.score}/{len(self.question_list)}")
