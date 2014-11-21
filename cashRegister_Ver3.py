class CashRegister:
    def __init__(self):
        self.clear()

    def addItem(self,price):
        self._values.append(price)

    def getTotal(self):
        return float(sum(self._values))

    def getCount(self):
        return len(self._values)

    def displayAll(self):
        for value in self._values:
            print(value)

    def clear(self):
        self._values = []

##    def __repr__(self):
##        return ("My register has seen " + str(self.getCount()) + " items")    


