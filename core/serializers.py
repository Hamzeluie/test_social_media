from rest_framework.serializers import Serializer, ModelSerializer
from .models import *


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'videofile',
            'summary',
            'created_at',
        )

class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'id',
            'content',
            'created_at',
            'post',
        )


class CategoryModelSerializer(ModelSerializer):
    model = Category
    fields = (
        'id',
        'title',
        'summary',
    )