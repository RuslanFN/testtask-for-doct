# Generated by Django 5.1.2 on 2024-10-28 09:20

import market.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_product_sub_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8, validators=[market.models.validate_price]),
            preserve_default=False,
        ),
    ]
