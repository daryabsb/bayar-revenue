# Generated by Django 4.0.6 on 2022-07-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_value_revenue_total_revenue_quantity_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]