# Generated by Django 4.0.6 on 2022-07-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]