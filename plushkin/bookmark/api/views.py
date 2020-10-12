from rest_framework import viewsets

from bookmark.api.serializers import BookmarkSerializer
from bookmark.models import Bookmark


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()


