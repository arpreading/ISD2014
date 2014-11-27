class AdvCashRegister:
    def __init__(self):
        self._itemCount =0
        self._totalPrice =0

    def addItem(self, price):
        self._itemCount = self._itemCount +1
        self._totalPrice = self._totalPrice + price

    def addItems(self,numItems,price):
        for i in range(numItems):
            self.addItem(price)
        
    def getTotal(self) :
        return self._totalPrice

    def getCount(self):
        return self._itemCount

    def clear(self) :
        self._itemCount =0
        self._totalPrice =0
		
    def __repr__(self):
        return("My Advanced Cash Register has seen " + str(self.getCount()) + " items\n with a total value of " +str(self.getTotal()) )
        
        
