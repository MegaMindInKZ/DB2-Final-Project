# Generated by Django 4.0.1 on 2022-04-21 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dari', '0006_alter_product_is_acitve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_acitve',
            new_name='is_active',
        ),
    ]
