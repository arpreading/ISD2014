class CashRegister:
    def __init__(self, items=0, price=0):
        self._valueItems = items
        self._valuePrice = price

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

    def __repr__(self):
        return ("My register has seen " + str(self.getCount()) + " items")

    def __lt__(self,y):
        if isinstance(other, CashRegister):
            return self.valueItems < y.getCount()
        else:
            return False
