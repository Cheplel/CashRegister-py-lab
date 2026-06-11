#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.total = 0
        self.discount = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        total_price = price * quantity
        self.total += total_price
        self.previous_transactions.append(total_price)
        for _ in range(quantity):
            self.items.append(item)

    def apply_discount(self):
        if self.total > 3000:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to kshs {int(self.total)}."
        else:
            return "There is no discount to apply."
        

    def void_last_transaction(self):
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            self.total -= last_transaction

my_cash_register = CashRegister()
my_cash_register.discount = 20

my_cash_register.add_item("milk", 200.00, 2)
print(my_cash_register.total)  # Output: 400.0

my_cash_register.add_item("loaf of bread", 100.50, 1)
print(my_cash_register.total)  # Output: 500.5

my_cash_register.add_item("sausages", 335.00)
print(my_cash_register.total)  # Output: 835.5

my_cash_register.add_item("cake", 900.0, 2)
print(my_cash_register.total)  # Output: 2635.5

my_cash_register.add_item("biscuit", 300.0, 2)
print(my_cash_register.total)  # Output: 3235.5

my_cash_register.add_item("Ribena juice", 275.00, 5)
print(my_cash_register.total)  # Output: 4610.5

print(my_cash_register.apply_discount())  # Output: "After the discount, the total comes to kshs 3688."