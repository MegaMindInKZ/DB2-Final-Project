# Generated by Django 4.0.1 on 2022-04-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dari', '0005_product_is_acitve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_acitve',
            field=models.BooleanField(default=True),
        ),
    ]
