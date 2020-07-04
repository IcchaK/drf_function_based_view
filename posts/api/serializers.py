from rest_framework import serializers
from posts.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'eBookName', 'eBookFile', 'eBookData', 'createdDatetime', 'updatedDatetime', 'addedBy']