from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_text = ques["text"]
    question_answer = ques["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():    
    quiz.new_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")

    