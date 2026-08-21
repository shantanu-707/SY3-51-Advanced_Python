"""
Payment Processing System - Strategy Pattern (Simplified)
Switch payment methods at runtime without changing the core logic.
"""

from abc import ABC, abstractmethod
from datetime import datetime



class Receipt:
    def __init__(self, amount, method, status):
        self.amount = amount
        self.method = method
        self.status = status
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.status}] {self.method} payment of {self.amount:.2f} at {self.timestamp}"

class PaymentStrategy(ABC):
    name = "Generic"

    @abstractmethod
    def validate(self) -> bool:
        pass

    def pay(self, amount) -> Receipt:
        status = "SUCCESS" if self.validate() else "FAILED"
        return Receipt(amount, self.name, status)


class CreditCardPayment(PaymentStrategy):
    name = "CreditCard"

    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self):
        return len(self.card_number) == 16


class PayPalPayment(PaymentStrategy):
    name = "PayPal"

    def __init__(self, email):
        self.email = email

    def validate(self):
        return "@" in self.email


class UPIPayment(PaymentStrategy):
    name = "UPI"

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount) -> Receipt:
        if not self.strategy:
            raise ValueError("No payment method set.")
        return self.strategy.pay(amount)


if __name__ == "__main__":
    processor = PaymentProcessor(UPIPayment("rahul@okhdfc"))
    print(processor.process_payment(1500))

    processor.set_strategy(CreditCardPayment("1234567812345678"))
    print(processor.process_payment(2500))

    processor.set_strategy(PayPalPayment("not-an-email"))
    print(processor.process_payment(99))