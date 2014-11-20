import os
os.chdir("I:\ISD2014")
from cashRegister import *
basket = CashRegister()
print("The value of the basket is: £{:.2f}".format(basket.getTotal()))
basket.addItem(0.99)
basket.addItem(2.95)
basket.addItem(4.50)
print("The value of the basket is: £{:.2f}".format(basket.getTotal()))
print("The number of items in the basket is: ",basket.getCount())
basket.clear()
print("The value of the basket is: £{:.2f}".format(basket.getTotal()))
print("The number of items in the basket is: ",basket.getCount())
