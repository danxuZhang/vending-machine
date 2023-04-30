from django.test import TestCase

from .models import Beverage


class BeverageModelTests(TestCase):
    def setUp(self):
        beverage = Beverage.objects.create(name="water")
        beverage = Beverage.objects.create(name="juice", price=10, stock=2)
    
    def test_default_price(self):
        beverage = Beverage.objects.get(name='water')
        self.assertEqual(beverage.price, 0.0)
    
    def test_default_stock(self):
        beverage = Beverage.objects.get(name='water')
        self.assertEqual(beverage.stock, 0)

    def test_availability(self):
        water = Beverage.objects.get(name='water')
        self.assertFalse(water.available())
        juice = Beverage.objects.get(name='juice')
        self.assertTrue(juice.available())

    def test_decrement_stock_success(self):
        juice = Beverage.objects.get(name='juice')
        try:
            juice.decrement_stock()
            self.assertEqual(juice.stock, 1)
        except AssertionError as msg:
            self.fail(msg)
        
    def test_decrement_stock_fail(self):
        water = Beverage.objects.get(name='water')
        self.assertRaises(AssertionError, water.decrement_stock)
