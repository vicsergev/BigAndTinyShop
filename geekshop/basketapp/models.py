from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        return sum(list(map(lambda x: x.quantity, self.user.basket.all())))

    @property
    def total_cost(self):
        return sum(list(map(lambda x: x.product_cost, self.user.basket.all())))

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()
