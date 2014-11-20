class CashRegister:
    def __init__(self):
        self._valueItems = 0
        self._valuePrice = 0

    def addItem(self,price):
        self._valuePrice += price
        self._valueItems += 1

    def getTotal(self):
        return self._valuePrice

    def getCount(self):
        return self._valueItems

    def clear(self):
        self._valueItems = 0
        self._valuePrice = 0
