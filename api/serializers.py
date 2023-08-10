# serializers.py
from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    description_file = serializers.FileField(write_only=True, required=False)

    class Meta:
        model = Book
        fields = '__all__'


