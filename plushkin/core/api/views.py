from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions

from bookmark.api.permissions import IsOwnerOrReadOnly
from core.api.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

