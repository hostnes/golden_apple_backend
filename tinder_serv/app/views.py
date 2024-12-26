import re

from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django_filters import rest_framework as filters

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
class UserFilter(filters.FilterSet):
    email = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = User
        fields = ['email', 'password']


class UserListCreateView(generics.ListCreateAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("owner_id")

        if user_id:
            return self.queryset.exclude(id=user_id)
        return self.queryset


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryItemsListView(APIView):
    def get(self, request):
        # Фильтруем категории, у которых есть хотя бы один item
        categories = Category.objects.annotate(num_items=Count('item')).filter(num_items__gt=0)
        serializer = CategoryWithItemsSerializer(categories, many=True)
        return Response(serializer.data)


class TestDetailView(APIView):
    def get(self, request, pk):
        try:
            test = Test.objects.get(pk=pk)
            serializer = TestSerializer(test)
            return Response(serializer.data)
        except Test.DoesNotExist:
            return Response({"error": "Test not found"}, status=status.HTTP_404_NOT_FOUND)


class ItemsListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer