from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=250, verbose_name='описание')
    price = models.IntegerField(default=0, verbose_name='цена')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
