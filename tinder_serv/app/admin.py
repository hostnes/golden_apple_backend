from django.contrib import admin
from .models import *


# Регистрация модели User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']  # Поля, отображаемые в списке


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(AnswerOption)