from rest_framework import serializers

from author.models import Author
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
