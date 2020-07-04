from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from posts.models import Document
from posts.api.serializers import DocumentSerializer

@api_view(['GET'])
def api_list_document_view(request):
    documents = Document.objects.all()
    if request.method == 'GET':
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def api_detail_document_view(request,id):
    try:
        document_ob = Document.objects.get(id=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocumentSerializer(document_ob)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_document_view(request,id):
    try:
        document_ob = Document.objects.get(id=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        import os
        file_ext = os.path.splitext(str(request.data['eBookFile']))[1]
        
        if not file_ext.lower() == '.pdf':
            return Response(data={'failure':'invalid file format'})

        serializer = DocumentSerializer(document_ob, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_document_view(request,id):
    try:
        document_ob = Document.objects.get(id=id)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = document_ob.delete()
        data = {}
        if operation:
            data['success'] = "Delete Successful"
        else:
            data['failure'] = "Delete Failed"
        return Response(data=data)

@api_view(['POST',])
def api_create_document_view(request):
    user = User.objects.get(pk=1)
    document_ob = Document(addedBy=user)
    if request.method == 'POST':
        serializer = DocumentSerializer(document_ob,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    