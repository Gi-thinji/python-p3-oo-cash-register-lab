#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0,items=None):
    self.discount = discount
    self.total = 0
    self.items = items if items is not None else []
    self.previous_transactions = []
  
  def add_item(self, item_name, item_price, quantity=1):
   
    self.total += item_price * quantity
    # item_names = [item[0] for item in self.items]
    for _ in range(quantity):
       self.items.append(item_name)
    
    self.previous_transactions.append(
       {
          "item_name": item_name, 
          "quantity": quantity, 
          "item_price": item_price
       }
    )
    

    

  def apply_discount(self):
    if self.discount:
        self.total = int(self.total * ((100-self.discount)/100))
        print(f"After the discount, the total comes to ${self.total}.")
    else:
       print("There is no discount to apply.")

  def void_last_transaction(self):
      if not self.previous_transactions:
          return "There are no transactions to void."
      else:
         self.total -= (self.previous_transactions[-1]["item_price"]*self.previous_transactions[-1]['quantity'])
      for _ in range(self.previous_transactions[-1]["quantity"]):
         self.items.pop()
      self.previous_transactions.pop()
    

  

    

  


  
   
    
