from django.db import models


class Beverage(models.Model):
    """
    Represents a beverage in the vending machine.
    """
    name = models.CharField(max_length=256)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)

    def is_available(self) -> bool:
        return self.stock > 0
    
    def decrement_stock(self) -> None:
        assert self.is_available(), "Stock is already empty"
        self.stock -= 1

    def purchaseable(self, to_check: float) -> bool:
        return to_check >= self.price

    def __str__(self) -> str:
        return f"{self.name}(${self.price}, {self.stock})"


class Transaction(models.Model):
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE)
    inserted_amount = models.FloatField()
    return_amount = models.FloatField()
    trans_time = models.DateTimeField()

    def calc_revenue(self) -> float:
        # Note that this amount may different from directly using beverage.price since the price can be later changed,
        # but this amount is sealed when transaction took place.
        return self.inserted_amount - self.return_amount
    
    def __str__(self) -> str:
        return f"{self.beverage.name}({self.trans_time})"
