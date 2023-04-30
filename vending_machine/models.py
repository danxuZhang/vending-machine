from django.db import models


class Beverage(models.Model):
    """
    Represents a beverage in the vending machine.
    """
    name = models.CharField(max_length=256)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)

    def increment_stock(self):
        self.stock += 1

    def decrement_stock(self):
        assert self.stock > 0, "Stock is already empty"
        self.stock -= 1

    def enough_price(self, to_check: float) -> bool:
        return to_check >= self.price
    
    def available(self) -> bool:
        return self.stock > 0

    def __str__(self) -> str:
        return f"{self.name}(${self.price}, {self.stock})"


class Transaction(models.Model):
    """
    Represents a vending machine transaction.
    """
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    inserted_amount = models.FloatField()
    return_amount = models.FloatField()
    trans_time = models.DateTimeField()

    def calc_return(self) -> float:
        return self.beverage.price - self.inserted_amount
