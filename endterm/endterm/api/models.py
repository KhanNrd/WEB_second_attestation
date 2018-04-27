from django.db import models


class Category(models.Model):
    """
    """
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Product(models.Model):
    """
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                                        related_name="products")
    name = models.CharField(max_length=200)
    price = models.FloatField(null=False)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category.to_json(),
            'name': self.name,
            'price': self.price,
        }