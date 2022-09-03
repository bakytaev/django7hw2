from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} - {self.description}'


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    QR = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.QR}'
