# Generated by Django 2.1.5 on 2019-12-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_auto_20191204_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetentry',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
