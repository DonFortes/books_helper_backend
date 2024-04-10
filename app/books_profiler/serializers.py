from books_profiler.models import BookProfilerPost
from rest_framework import serializers


class BookProfilerCreateSerializer(serializers.Serializer):
    column_name = serializers.CharField(max_length=20)
    is_visible = serializers.BooleanField(default=True)

    class Meta:
        model = BookProfilerPost
        fields = "__all__"
        abstract = True


class BookProfilerListSerializer(serializers.Serializer):
    name = serializers.BooleanField(default=True)
    title = serializers.BooleanField(default=True)
    author = serializers.BooleanField(default=True)
    description = serializers.BooleanField(default=True)
    price = serializers.BooleanField(default=True)

    class Meta:
        model = BookProfilerPost
        abstract = True
