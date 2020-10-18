from rest_framework import viewsets, permissions

from bookmark.api.permissions import IsOwnerOrReadOnly
from bookmark.api.serializers import BookmarkSerializer
from bookmark.models import Bookmark


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]
