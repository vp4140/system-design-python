from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        return f"Paid ${amount} using Credit Card: {self.card_number} (Card Holder: {self.card_holder})"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid ${amount} using PayPal (Email: {self.email})"

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin (Wallet: {self.wallet_address})"

# Step 3: Context Class
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        return self.strategy.pay(amount)

# Step 4: Use the Strategy
# Example usage
credit_card = CreditCardPayment("1234-5678-9876-5432", "Alice")
paypal = PayPalPayment("alice@example.com")
bitcoin = BitcoinPayment("1BitcoinWallet123")

# Context
payment_context = PaymentContext(credit_card)
print(payment_context.execute_payment(100))  # Pay with credit card

# Change strategy to PayPal
payment_context.set_strategy(paypal)
print(payment_context.execute_payment(200))  # Pay with PayPal

# Change strategy to Bitcoin
payment_context.set_strategy(bitcoin)
print(payment_context.execute_payment(300))

payment_context.set_strategy(paypal)
print(payment_context.execute_payment(300))
# Pay with Bitcoin
