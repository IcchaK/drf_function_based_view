from rest_framework import serializers
from posts.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'body', 'docfile', 'created_datetime', 'updated_datetime', 'author']