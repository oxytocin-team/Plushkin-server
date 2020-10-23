from django_filters.rest_framework import FilterSet

from bookmark.models import Bookmark


class BookmarkFilter(FilterSet):

    class Meta:
        model = Bookmark
        fields = {
            'id': ['exact'],
            'type': ['exact'],
            'title': ['exact', 'contains'],
            'user': ['exact'],
        }
