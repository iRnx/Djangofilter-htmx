from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.name')
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('name', 'author_name', 'price', 'genre')

    def get_genre(self, obj):
        return obj.get_genre_display()