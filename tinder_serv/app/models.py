from django.utils import timezone

from django.db import models
from django.db.models import Q


class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.TextField()
    cost = models.FloatField(default=0)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_cost = models.IntegerField(default=0)


class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text
