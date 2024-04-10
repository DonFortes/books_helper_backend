from books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):

    def get_fields(self):
        fields = super().get_fields()
        # logging.info(f"{fields=}")
        exclude_fields = self.context.get("exclude_fields", [])
        for field in exclude_fields:
            fields.pop(field)

        return fields

    class Meta:
        model = Book
        fields = ["id", "name", "title", "author", "description", "price"]
