# Generated by Django 2.2.28 on 2022-12-08 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221208_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 8, 22, 20, 11, 572086), verbose_name='Опубликована'),
        ),
    ]