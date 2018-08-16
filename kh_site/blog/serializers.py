"""Serializer for the objects in the Blog app."""
from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for the Presentation object."""

    class Meta:
        """Meta data about the serializer."""

        model = Article
        fields = [
            'title', 'short_title', 'slug', 'excerpt', 'content',
            'status', 'tags', 'date_created', 'last_modified', 'date_published'
        ]
