from choiceQuestion import *
class MultipleChoiceQuestion(ChoiceQuestion):

   def __init__(self):
      super().__init__()

   def addChoice(self, choice, correct):
      self._choices.append(choice)
      if correct:
         ans = self.getAnswer()
         newAns = ans + " " + str(len(self._choices))
         self.setAnswer(newAns)

   def display(self):
      super().display()
      for i in range(len(self._choices)):
          print(i+1, " ", self._choices[i])
