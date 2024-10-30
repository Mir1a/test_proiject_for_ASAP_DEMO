from rest_framework import viewsets, filters
from rest_framework.mixins import (CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer


class BookViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['published_date', 'language', 'author']
    ordering = ['author']
