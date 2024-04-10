from books.models import Book
from books.serializers import BookSerializer
from libs.global_columns_state import get_book_columns_provider
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):

    queryset = Book.objects.all().order_by("name")
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return BookSerializer

    def list(self, request, *args, **kwargs):
        book_columns_provider = get_book_columns_provider(username=request.user.username)
        context = super().get_serializer_context()
        context.update(
            {
                "request": request,
                "exclude_fields": [key for key, value in book_columns_provider.columns_state.items() if value is False],
            }
        )
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
