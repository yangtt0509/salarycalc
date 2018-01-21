from django.db import models

# Create your models here.


class Product(models.Model):
    WORK_TYPE_CHOICES = (
        (0, '个'),
        (1, '千克'),
        (2, '小时')
    )
    name = models.CharField(max_length=100, unique=True)
    unit_price = models.FloatField()
    unit = models.FloatField(default=1)
    work_type = models.IntegerField(choices=WORK_TYPE_CHOICES)

    @property
    def work_type_str(self):
        return self.WORK_TYPE_CHOICES[self.work_type][1]
