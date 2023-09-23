# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
"""
Ghadir Alfadhl
ITS265
09/05/2021

"""

from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    
    minPrice = 0.0
    totalPrice = 0
    shopObj = fruitShops[0]
    minPrice = shopObj.getPriceOfOrder(orderList)
    
    for shopFruit in fruitShops:
        totalPrice = shopFruit.getPriceOfOrder(orderList)
        
        if totalPrice < minPrice:
            shopObj = shopFruit
            minPrice = totalPrice
    return shopObj



if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    
    
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    print("Thank you for your order!")
    



"""
Fill in the function shopSmart(orderList,fruitShops) in shopSmart.py,
 which takes an orderList (like the kind passed in to FruitShop.getPriceOfOrder)
 and a list of FruitShop and returns the FruitShop 
 where your order costs the least amount in total. 
 DO NOT change the file name or variable names

"""
