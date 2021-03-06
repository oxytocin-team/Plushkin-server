import datetime

from django.db import models


class Bookmark(models.Model):
    TYPE = (
        ('U', 'Unsorted'),
        ('L', 'Liked'),
        ('T', 'Trash'),
    )

    type = models.CharField(max_length=1, choices=TYPE, default='U')
    user = models.ForeignKey('auth.User', related_name='bookmarks', related_query_name='bookmark',
                             on_delete=models.CASCADE)
    title = models.TextField()
    url = models.TextField()
    date = models.DateField(default=datetime.date.today)


