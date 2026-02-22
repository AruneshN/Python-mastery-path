"""
Topics: abstraction
desc:
1) Hiding internal details and implementation and show only the result
2) Hiding unwanted deatils to users
"""

from abc import ABC, abstractmethod

# Abstract Payment class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass  # Implementation hidden

# Concrete payment methods
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

# Function to process payment
def process_payment(payment_method: Payment, amount):
    payment_method.pay(amount)


# Example usage
credit = CreditCardPayment()
upi = UPIPayment()
paypal = PayPalPayment()

process_payment(credit, 1000)
process_payment(upi, 500)
process_payment(paypal, 750)