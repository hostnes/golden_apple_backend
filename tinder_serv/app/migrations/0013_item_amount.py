# Generated by Django 4.2.13 on 2024-12-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_user_photo_alter_item_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]