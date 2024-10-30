from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
