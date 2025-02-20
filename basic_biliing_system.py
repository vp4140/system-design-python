"""
Basic requirements:
User
-
Are there different ways?
Should user get notified on payment? What are different methods?

"""
import uuid
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    def pay(self,amount):
        pass
class CreditCard(PaymentStrategy):
    def pay(self,amount):
        print("Paid by Credit card")

class CashPayment(PaymentStrategy):
    def pay(self,amount):
        print("Paid by Cash")


class Observer(ABC):
    def update(self,message):
        pass
class EmailNotification(Observer):
    def update(self, message):
        print(f"[Email Notification] {message}")

class SMSNotification(Observer):
    def update(self, message):
        print(f"[SMS Notification] {message}")

class Invoice:
    def __init__(self,amount,user_id,due_date):
        self.invoice_id = str(uuid.uuid4())[:8]
        self.bill_amount = amount
        self.user_id = user_id,
        self.due_date = due_date
        self.status = "PENDING"
    def make_payment(self):
        self.status = "PAID"


class BillingServices:
    def __init__(self):
        self.invoices = {}
        self.observers = []

    def add_observers(self,observer):
        self.observers.append(observer)

    def notify(self,message):
        for observer in self.observers:
            observer.update(message)

    def generate_invoices(self,amount,user_id,due_date):
        invoice = Invoice(amount,user_id,due_date)
        self.invoices[invoice.invoice_id] = invoice
        self.notify(f"Invoice {invoice.invoice_id} generated for User {user_id}. Amount: ${amount}")
        return invoice

    def process_payment(self,strategy:PaymentStrategy,invoice_id):
        if invoice_id not in self.invoices:
            return "No invoices present"
        invoice = self.invoices[invoice_id]
        if invoice.status == "PAID":
            return "Bill Already Paid"
        payment_message = strategy.pay(invoice.bill_amount)
        invoice.make_payment()

        return payment_message
from _datetime import  datetime
if __name__ == "__main__":
    billing_service = BillingServices()
    email_notifier = EmailNotification()


    billing_service.add_observers(email_notifier)
    invoice_generated = billing_service.generate_invoices(100,1,due_date=datetime(2025,3,3))

    strategy = CashPayment()
    print(billing_service.process_payment(strategy,invoice_generated.invoice_id))
