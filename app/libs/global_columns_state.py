import functools

from books.models import Book
from django.db import models
from settings.settings import MAX_USERS_CACHE_PER_TIME


class GlobalColumnsProvider:
    """Class to store model columns state to include or exclude fields from final response"""

    def __init__(self, model: type[models.Model]):
        self.model: type[models.Model] = model
        self.columns_state: dict = self.__get_dict_from_django_model_fields()
        self.columns = tuple(self.columns_state)
        self.column_names_repr: str = ", ".join(self.columns)

    def __get_dict_from_django_model_fields(self) -> dict:
        return {key.name: True for key in self.model._meta.fields}


@functools.lru_cache(maxsize=MAX_USERS_CACHE_PER_TIME)
def get_book_columns_provider(username) -> GlobalColumnsProvider:  # noqa
    """Using cache functionality to return instance of GlobalColumnsProvider with different state for every user.

    #TODO: Implement Redis caching
    This is thread safe cache, so it will affect on cache state for every thread.
    So if you want to run app in several workers, it is necessary to use Redis or KeyDB instead
    Using in memory caching to simplify for now
    """
    model = Book
    return GlobalColumnsProvider(model)
