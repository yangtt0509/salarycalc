from django.db import models
from products.models import Product

OVERTIME_FACTOR = 1.5


class Employee(models.Model):
    name = models.CharField(max_length=30)
    available = models.BooleanField(default=True)


class SalaryItem(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    complete = models.FloatField()
    is_overtime = models.BooleanField(default=False)
    date = models.DateField()

    @property
    def price(self):
        price={}
        unit_price = self.product.unit_price
        unit = self.product.unit
        item_price = self.complete*unit_price/unit
        if self.is_overtime:
            item_price *= OVERTIME_FACTOR
        if self.product.work_type == 1:
            formula = "{0} * {1} / {2} = {3}".format(
                str(self.complete),
                str(unit_price),
                str(unit),
                str(item_price))
        else:
            if unit == 1:
                formula = "{0} * {1} = {2}".format(
                    str(self.complete),
                    str(unit_price),
                    str(item_price))
            else:
                formula = "{0} * {1} / {2} = {3} {4}".format(
                    str(self.complete),
                    str(unit_price),
                    str(unit),
                    str(item_price),
                    "Error! Please Check.")
        price['formula'] = formula
        price['result'] = item_price
        return item_price

