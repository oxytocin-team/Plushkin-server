from django.conf.urls import url

from .views import BookmarkViewSet

app_name = 'bookmark'
urlpatterns = [
    url(r'bookmarks/$', BookmarkViewSet.as_view({'get': 'list', 'post': 'create'}), name='account-list'),
    url(r'bookmarks/(?P<pk>[^/]+)$', BookmarkViewSet.as_view({'get': 'retrieve', 'post': 'update'}),
        name='account-retrieve'),
]
