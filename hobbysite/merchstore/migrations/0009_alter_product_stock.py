# Generated by Django 5.0.2 on 2024-05-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0008_alter_transaction_amount_alter_transaction_buyer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
