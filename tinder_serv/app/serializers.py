from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'name', "password", "last_name"]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'brand', 'description', 'photo', 'cost', 'amount']


class CategoryWithItemsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='title')
    items = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'items']

    def get_items(self, category):
        items = Item.objects.filter(category=category)
        return ItemSerializer(items, many=True).data

class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    options = AnswerOptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'title', 'description', 'questions']
