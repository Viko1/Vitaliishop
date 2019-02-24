from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Product %s" % self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):

    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media/products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s" % self.id

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
