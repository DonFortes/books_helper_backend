import logging

from books_profiler.serializers import BookProfilerCreateSerializer, BookProfilerListSerializer
from libs.global_columns_state import get_book_columns_provider
from rest_framework import mixins, permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class BookProfilerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):

    permission_classes = [permissions.IsAuthenticated]
    view_set_serializers = {
        "create": BookProfilerCreateSerializer,
        "list": BookProfilerListSerializer,
    }
    pagination_class = None

    def get_serializer_class(self):
        return self.view_set_serializers.get(self.action)

    def create(self, request, *args, **kwargs):
        serializer: BookProfilerCreateSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        column_name, is_visible = serializer.data["column_name"], serializer.data["is_visible"]
        book_columns_provider = get_book_columns_provider(username=request.user.username)

        if column_name in book_columns_provider.columns:
            book_columns_provider.columns_state[column_name] = is_visible
        else:
            error = f"{column_name=} is not allowed. Columns are: {book_columns_provider.column_names_repr}"
            logging.error(error)
            return Response(data={"error": error}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            BookProfilerListSerializer(book_columns_provider.columns_state, many=False).data,
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, *args, **kwargs):
        book_columns_provider = get_book_columns_provider(username=request.user.username)
        serializer = self.get_serializer(book_columns_provider.columns_state, many=False)

        return Response(serializer.data)
