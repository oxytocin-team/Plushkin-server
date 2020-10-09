from django.conf.urls import url

from rest_framework.authtoken import views as rest_views
from . import views
from .views import UserViewSet

app_name = 'core'
urlpatterns = [
    url(r'user_registration/$', views.UserCreate.as_view(), name="user_registration"),
    url(r'get_token/$', rest_views.obtain_auth_token, name="get_token"),
    url(r'users/$', UserViewSet.as_view({'get': 'list'}), name='genres_list'),
]
