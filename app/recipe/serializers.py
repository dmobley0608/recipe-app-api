"""
Serializers for Recipe API
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'price',
            'time_minutes',
            'link'
        ]
        read_only = ['id']


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe details"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
