class Counter:
    def __init__(self):
        self._value = 0
    
    def reset(self):
        self._value = 0

    def click(self):
        self._value = self._value + 1

    def getValue(self):
        return self._value
