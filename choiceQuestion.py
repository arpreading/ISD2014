from questions import *
class ChoiceQuestion(Question):

   def __init__(self):
      super().__init__()
      self._choices = []

   def addChoice(self, choice, correct):
      self._choices.append(choice)
      if correct:
         self.setAnswer(str(len(self._choices)))

   def display(self):
      super().display()
      for i in range(len(self._choices)):
          print(i+1, " ", self._choices[i])
