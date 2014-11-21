class Counter:
    def __init__(self):
        self._value = 0
        self._maximum = 0
    
    def reset(self):
        self._value = 0

    def click(self):
        if self._value < self._maximum:
            self._value += 1
        else:
            print("Limit Exceeded!")

    def getValue(self):
        return self._value

    def undo(self):
        if self._value > 0:
            self._value -= 1
        else:
            print("Cannot undo from a zero count")

    def setLimit(self, maximum):
        self._maximum = maximum
