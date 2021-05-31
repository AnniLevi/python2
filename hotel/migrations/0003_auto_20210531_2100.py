# Generated by Django 3.2.3 on 2021-05-31 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20210531_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='number_of_people',
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype'),
        ),
    ]