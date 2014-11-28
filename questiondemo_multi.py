from choiceQuestion import *

def presentQuestion(q):
    q.display()
    response = input("Your answer is: ")
    print(q.checkAnswer(response))

first = ChoiceQuestion()
first.setText("In what year was Python first released?")
first.addChoice("1991", True)
first.addChoice("1992", False)
first.addChoice("1992", False)

second = Question()
second.setText("Who is the inventor of Python?")
second.setAnswer("Guido van Rossum")     

presentQuestion(first)
presentQuestion(second)

