from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True, null=True)
    author = models.CharField(max_length=30)
    description = models.CharField(max_length=512, blank=True, null=True)
    price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)])

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.title} by {self.author}"
