# Generated by Django 2.2.28 on 2022-12-08 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 8, 21, 53, 16, 640699), verbose_name='Опубликована'),
        ),
    ]