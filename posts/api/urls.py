from django.urls import path

from posts.api.views import api_detail_document_view, api_update_document_view, api_delete_document_view, api_create_document_view, api_list_document_view

urlpatterns = [
    path('', api_list_document_view, name='list'),
    path('<id>/', api_detail_document_view, name='detail'),
    path('update/<id>', api_update_document_view, name='update'),
    path('delete/<id>', api_delete_document_view, name='delete'),
    path('create', api_create_document_view, name='create')
]