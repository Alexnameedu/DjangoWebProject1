# Generated by Django 2.2.28 on 2022-12-08 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20221208_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 8, 23, 22, 31, 872917), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 8, 23, 22, 31, 873918), verbose_name='Дата'),
        ),
    ]