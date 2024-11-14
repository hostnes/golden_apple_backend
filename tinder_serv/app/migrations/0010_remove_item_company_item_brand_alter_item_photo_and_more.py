# Generated by Django 4.2.13 on 2024-11-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='company',
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]