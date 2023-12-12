#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    '''takes one optional argument, a discount, on initialization.'''
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, item, price, quantity=1):
    '''accepts a title and a price and increases the total.'''
    price  = float(price)
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
    self.transactions.append(
      {"item": item, "price": price, "quantity": quantity}
    )

  def apply_discount(self):
    '''applies the discount to the total price.'''
    if self.discount:
      self.total = int (self.total * (100 - self.discount) / 100)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.transactions:
      last_transaction = self.transactions.pop()
      last_item_price = last_transaction["price"] * last_transaction["quantity"]
      self.total -= last_item_price
      print(f"The total comes to ${self.total}.")
    else:
      print("There are no transactions to void.")    

