from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('categories-with-items/', CategoryItemsListView.as_view(), name='category-items-list'),
    path('tests/<int:pk>/', TestDetailView.as_view(), name='test-detail'),
    path('items/', ItemsListCreateView.as_view(), name='test-detail'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='test-detail'),
]
