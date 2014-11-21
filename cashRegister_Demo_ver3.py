import os
os.chdir("I:\ISD2014")
from cashRegister_Ver3 import *
basket = CashRegister()
print("The value of the basket is: ", basket.getTotal())
basket.addItem(0.95)
basket.addItem(2.95)
basket.addItem(4.50)
print("The value of the basket is: £", basket.getTotal())
print("The number of items in the basket is: ",basket.getCount())
print(basket.displayAll())
basket.clear()
print("The value of the basket is: £", basket.getTotal())
print("The number of items in the basket is: ",basket.getCount())

