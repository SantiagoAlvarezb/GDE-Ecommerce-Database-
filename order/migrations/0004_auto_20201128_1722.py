# Generated by Django 3.1.2 on 2020-11-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201128_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='product',
            field=models.CharField(max_length=20000),
        ),
    ]
