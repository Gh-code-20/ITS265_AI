# buyLotsOfFruit.py
# -----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

"""
Ghadir Alfadhl
ITS265
09/05/2021

"""

#from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    #iterating each tuple of orderList
    for fruit, numPounds in orderList:
        #if the fruit is available in fruitPrices
        if fruit in fruitPrices:
            totalCost += fruitPrices[fruit] * numPounds
        else:
            print(fruit, "price not available")
            return None
    return totalCost
        
    
# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))


"""
Add a buyLotsOfFruit(orderList) function to buyLotsOfFruit.py 
which takes a list of (fruit,pound) tuples and returns the cost of your list. 
If there is some fruit in the list which doesn’t appear in fruitPrices 
it should print an error message and return None. 
DO NOT change the fruitPrices variable. 

"""