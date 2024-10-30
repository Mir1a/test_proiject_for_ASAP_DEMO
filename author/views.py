from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]
