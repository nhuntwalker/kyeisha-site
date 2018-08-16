"""Serializer for the objects in the Speaking app."""
from rest_framework import serializers
from speaking.models import Presentation


class PresentationSerializer(serializers.ModelSerializer):
    """Serializer for the Presentation object."""

    class Meta:
        """Meta data about the serializer."""

        model = Presentation
        fields = ['title', 'subtitle', 'details']
