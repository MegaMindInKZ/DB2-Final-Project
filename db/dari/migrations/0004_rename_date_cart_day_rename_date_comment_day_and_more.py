# Generated by Django 4.0.1 on 2022-04-20 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dari', '0003_rating_purchase_price_history_feedback_comment_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='date',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='date',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='price_history',
            old_name='date',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='date',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='date',
            new_name='day',
        ),
    ]