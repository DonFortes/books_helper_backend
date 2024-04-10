from django.db import models


class BookProfilerPost(models.Model):
    column_name = models.CharField(max_length=20)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.column_name} visible: {self.is_visible}"

    class Meta:
        abstract = True


class BookProfilerList(models.Model):
    id = models.BooleanField()
    name = models.BooleanField()
    title = models.BooleanField()
    author = models.BooleanField()
    description = models.BooleanField()
    price = models.BooleanField()

    def __str__(self):
        return ", ".join((f"{k} = {v}" for k, v in self.__dict__.items()))

    class Meta:
        abstract = True
