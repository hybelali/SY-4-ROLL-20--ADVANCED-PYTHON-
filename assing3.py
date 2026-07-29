from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"${amount} paid successfully using credit card.")


class DebitCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"${amount} paid successfully using debit card.")


class UPI(PaymentMethod):
    def make_payment(self, amount):
        print(f"${amount} paid successfully using UPI.")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.make_payment(amount)


amount = float(input("Enter the payment amount: "))

print("Choose the payment method")
print("1. Credit card")
print("2. Debit card")
print("3. UPI")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    method = CreditCard()
elif choice == 2:
    method = DebitCard()
elif choice == 3:
    method = UPI()
elif choice == 4:
    print("Exiting...")
    exit()
else:
    print("Invalid choice")
    exit()

payment = PaymentProcessor(method)
payment.process_payment(amount)
    
        
    
    
           
         
