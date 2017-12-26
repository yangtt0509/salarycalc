from django.db import models

OVERTIME_FACTOR = 1.5

class Employee(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField()
    unit = models.FloatField(default=1)

class SalaryItem(models.Model):
    employee = models.ForeignKey(Employee)
    product = models.ForeignKey(Product)
    complete = models.FloatField()
    is_overtime = models.BooleanField(default=False)
    date = models.DateField()

    @property
    def price(self):
        unit_price = self.product.unit_price
        unit = self.product.unit
        item_price = self.complete*unit_price/unit
        if self.is_overtime:
            item_price *= OVERTIME_FACTOR
        return item_price


