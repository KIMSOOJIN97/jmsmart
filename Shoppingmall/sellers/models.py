from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 32, verbose_name="상품명")
    price = models.IntegerField(verbose_name = "상품가격",default=0)
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고",default=1)

    def __str__(self):
        return self.name