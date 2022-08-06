# Generated by Django 2.2.16 on 2022-07-30 14:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220506_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(default=None, validators=[django.core.validators.MaxValueValidator(10, 'Максимальная оценка - 10'), django.core.validators.MinValueValidator(1, 'Минимальная оценка - 1')], verbose_name='Оценка'),
        ),
    ]