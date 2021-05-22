# Generated by Django 3.2.3 on 2021-05-22 07:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales_manager', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='likes',
            field=models.ManyToManyField(related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
