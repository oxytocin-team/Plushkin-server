from rest_framework import serializers

from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}, 'date': {'read_only': True}, 'type': {'required': False}}

    def create(self, validated_data):
        bookmark = Bookmark(
            title=validated_data['title'],
            url=validated_data['url'],
            type=self.data.get('type', Bookmark._meta.get_field('type').get_default()),
            user=self.context['request'].user,
        )
        bookmark.save()
        return bookmark
