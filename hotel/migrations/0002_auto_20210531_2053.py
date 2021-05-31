# Generated by Django 3.2.3 on 2021-05-31 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room_number',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booked', to='hotel.room'),
        ),
        migrations.AddField(
            model_name='room',
            name='booked_person',
            field=models.ManyToManyField(related_name='booked_room', through='hotel.Booking', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booked_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='is_lux',
            field=models.BooleanField(verbose_name='Люкс'),
        ),
    ]
